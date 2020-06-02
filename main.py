import MeCab

t = MeCab.Tagger()
sentence = "太郎はこの本を彼女に渡した"
print(t.parse(sentence))