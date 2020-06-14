import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import jaconv


words_list=pd.read_pickle("data/words.pkl")


# 隣接する単語間のコストを計算して返す
def calc_cost(prev_node, current_node):
    prev_word = prev_node["word"]
    current_word = current_node["word"]
    # wordの中身は次のような形:
    # Index=8945, 表層形='楽しい', コスト=4117, 品詞='形容詞', 品詞細分類1='自立', 品詞細分類2='*', 品詞細分類3='*', 活用型='形容詞・イ段', 活用形='基本形', 原形='楽しい', 読み='タノシイ', 発音='タノシイ'
    # current_word.品詞 のようにしてアクセスする

    # startとendのノードはlabelで判定
    if prev_node["label"] == "START":
        return current_word.コスト
    if current_node["label"] == "END":
        return 0

    # ここでコスト計算をしてほしいです
    # 現状ipa辞書の単語コストをそのまま返しています
    return current_word.コスト


# 単語リストに存在しない単語を生成
# startノードや数字・記号などで使う
# 品詞を＊としているのでコスト計算と干渉する恐れあり
def create_empty_word(word, cost):
    empty_word = pd.DataFrame([[word, 0, 0, cost, "*", "*", "*", "*", "*", "*", word, word, word]],
        columns = ["表層形", "左文脈ID", "右文脈ID", "コスト", "品詞", "品詞細分類1", "品詞細分類2", "品詞細分類3", "活用型", "活用形", "原形", "読み", "発音"])
    return empty_word    


# 読みに一致する単語をdataframeで返す
def get_words_by_kana(kana_word):
    kana_word = jaconv.hira2kata(kana_word) # ひらがなをカタカナに変換
    words = words_list[words_list["読み"] == kana_word]
    
    # 入力によって経路が存在しなくなるのを防ぐため，
    # 単語リストに存在しない1文字の場合には十分高いコストで読みのまま返す
    if len(kana_word) == 1 and len(words) == 0:
        words = create_empty_word(kana_word, 9999999)
    return words


# かな文を漢字に変換
def convert_kana_to_kanji(kana_sentence, should_show_graph = False):

    length = len(kana_sentence)
    node_id = 0
    lattice = nx.DiGraph()
    connecting_nodes = {i: list() for i in range(length + 1)} # connecting_nodes[i]にはi文字目で終わるノードのIDが格納される

    # ノードを追加し前ノードからエッジをつなぐメソッド
    def add_node(word, begin, end):
        nonlocal node_id

        label = word.表層形
        pos = (begin*10 + end, begin*end + node_id*10) # 表示位置
        lattice.add_node(node_id, word = word, label = label, pos=pos)

        # 現在のノードにつながるノードから重み付きエッジを生成
        for prev_node_id in connecting_nodes[begin]:
            cost = calc_cost(lattice.nodes[prev_node_id], lattice.nodes[node_id])
            lattice.add_edge(prev_node_id, node_id, weight = cost)
        
        connecting_nodes[end].append(node_id)
        node_id += 1
    

    # 入力文を走査しラティスを生成
    add_node(create_empty_word("START", 0).iloc[0], 0, 0)
    for begin in range(length + 1):
        for end in range(begin + 1, length + 1):
            # 入力文の一部に一致する単語をノードとして追加
            part_of_sentence = kana_sentence[begin:end]
            words = get_words_by_kana(part_of_sentence)
            for word in words.itertuples():
                add_node(word, begin, end)
    add_node(create_empty_word("END", 0).iloc[0], length, length)

    # ダイクストラ法で最短経路を計算
    # 他のアルゴリズムは以下参照
    # https://networkx.github.io/documentation/stable/reference/algorithms/shortest_paths.html
    shortest_path = nx.shortest_path(lattice, source = 0, target = lattice.number_of_nodes() - 1, weight = "weight")

    # 最短経路をつないで漢字の文を出力
    converted_sentence = ""
    for id in shortest_path[1:-1]:
        lattice.nodes[id]
        converted_sentence += lattice.nodes[id]["word"].表層形

    # グラフを表示(デバッグ用)
    if should_show_graph:
        pos=nx.get_node_attributes(lattice,'pos')
        labels={id: lattice.nodes[id]["label"] for id in lattice.nodes}
        nx.draw(lattice, pos, labels=labels, with_labels=True, node_shape="s", node_size=1000, font_size=10, font_family="Meiryo")
        plt.show()
    
    return converted_sentence
