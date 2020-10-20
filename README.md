# ES質問まとめアプリ
ESの質問に対する自分の回答を一括管理するwebアプリです\
自分で管理するだけではなくて，他人に公開できるGitHubのES版みたいなアプリにしたいです\
Python+Djangoで作成しました

ESの質問に対する自分の回答を効率よく管理することができるwebアプリケーションです．\
使用技術は，Python, Django, HTML, Bootstrap, Herokuです．\
ポスト(ESの質問，回答，タグ，企業，公開or非公開など)を作成し，自分の回答をストックし，後で見返すことができます．\
また，自分の回答を管理するだけでなく，公開に設定したポストを他人に見せることができ，ポートフォリオとして使用することもできます．\
コードの管理と自身のアピールの両方が可能であるGitHubのES版をコンセプトとして作成しています．

Herokuにデプロイしています.

[ES質問まとめアプリ](https://esmanageapp.herokuapp.com/login/)

私が公開にしているESの質問の回答は以下のURLで見ることができます．

[私(junki)の回答](https://esmanageapp.herokuapp.com/list/junki/)
# Features
## 機能
### 実装済み
- ユーザー登録，ログイン，ログアウト
- Post(質問と回答)作成
- Postに対するタグ付
- Post一覧表示
- Post詳細表示
- Post削除
- タグ作成
- 回答の作成者とそれ以外の人で見える情報をかえる
- ユーザー登録をしていなくても他人が公開している回答を見れるようにする．(ゲスト機能)
- 削除機能
- ユーザ検索

### これから実装したいこと
- バージョン管理(同じ質問に対して変更前も保存できるようにする)
- タグ検索
- UI向上
- 表示方法変更(リスト表示，カード表示，など)
- ログイン画面にゲストユーザとして使用するを入れる
- dockerfileとdocker-composeで環境構築
- テストを書く
- アプリ使用方法のwikiを書く

### 問題
- ポストを編集しようとするとタグが初期化されてしまう



# 開発環境
OS
* macOS Catalina バージョン 10.15.6

その他

* Python 3.7.3

# Usage
このレポジトリをクローン
```bash
git clone https://github.com/junkhp/ES_manage.git
```
クローンしたフォルダに移動
```linux
cd ES_manage/
```
仮想環境を起動し，必要なライブラリをインストール
```bash
pip install -r requirents.txt
```

モデルをmigrate
```python
python manage.py migrate
```

アプリを実行
```bash
python manage.py runserver
```

`http://127.0.0.1:8000/`にアクセスするとES質問まとめアプリが起動されています．

# Note
Mac以外ではテストしていません．
