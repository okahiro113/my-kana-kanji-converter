# kana-kanji-converter

## 導入(Windows)

1. MeCabをインストール  
http://taku910.github.io/mecab/#download  
文字コードはUTF-8を指定

2. 環境変数を設定  
http://realize.jounin.jp/path.html  
環境変数PathにMeCabのインストールフォルダ\binを指定 (例: `C:\Program Files (x86)\MeCab\bin`)

3. Python 3.8をインストール  
https://www.python.org/downloads/

4. Pipenvをインストール    
```pip install pipenv```  
PipenvはPython用のパッケージマネージャです．
開発中新しいパッケージをインストールするときは`pipenv install numpy`のようにしてください (`pip install`を使うと他の人の環境で再現できないので非推奨)．

5. このリポジトリをクローン  
```git clone https://github.com/kana-kanji-sit2020/kana-kanji-converter.git```

6. プロジェクトの初期化  
```pipenv install```  
これで必要なパッケージがインストールされます．
リモートで新たなパッケージが追加された場合にもこれが必要．


## 実行

次のように実行してください．  
```pipenv run python main.py```

`pipenv run`を使うとインストールしたパッケージがスクリプトから使えることが保証されます．
これをつけないとimportしたパッケージが使えないことがあります (`pipenv install`してからターミナルを新しく開けば使えるっぽい)．


## 開発

開発中新しいパッケージをインストールするときは`pipenv install`を利用してください (例: `pipenv install numpy`)．
`pip install`を使うと他の人の環境で再現できないのでよくない．