#coding:utf-8

import MeCab
from convert_kana_to_kanji import convert_kana_to_kanji
import option as op

if __name__ == '__main__':

    #引数チェック
    args=op.parser()

    if args.firstarg.rsplit(".")[-1]!="txt":
        print(convert_kana_to_kanji(args.firstarg))

    #ファイルから一行ずつ変換
    else:
        f=open(args.firstarg,"r")
        line=f.readline()
        while line:
            print(convert_kana_to_kanji(line.strip()))
            line=f.readline()
        f.close()
