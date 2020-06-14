import pandas as pd
from pathlib import Path

# ipa辞書を読み込み，pandasのdataframeとして返す
# ipa辞書のフォーマットは下記を参照
# https://taku910.github.io/mecab/dic.html
def read_ipadic(ipadic_path):
    words_df = pd.DataFrame()
    csv_files = Path(ipadic_path).glob("**/*.csv")

    for csv_file in csv_files:
        print(csv_file)
        csv_df = pd.read_csv(csv_file, encoding = "cp932", header = None)
        words_df = words_df.append(csv_df)

    words_df.columns = ["表層形", "左文脈ID", "右文脈ID", "コスト", "品詞", "品詞細分類1", "品詞細分類2", "品詞細分類3", "活用型", "活用形", "原形", "読み", "発音"]
    words_df.reset_index(inplace = True, drop = True)

    print(words_df)
    return words_df


words_df = read_ipadic("C:\Program Files (x86)\MeCab\dic\ipadic")
words_df.to_pickle("data\words.pkl") # pickleファイルとして保存
