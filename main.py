import MeCab
from convert_kana_to_kanji import convert_kana_to_kanji

#t = MeCab.Tagger()
#sentence = "太郎はこの本を彼女に渡した"
#print(t.parse(sentence))

print(convert_kana_to_kanji("これはしぜんげんごしょりのかだいです。"))
print(convert_kana_to_kanji("NHKきょういくてれび"))
