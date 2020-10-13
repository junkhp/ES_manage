# ES質問まとめアプリ
ESの質問に対する自分の回答を一括管理するwebアプリです\
自分で管理するだけではなくて，他人に公開できるGitHubのES版みたいなアプリにしたいです\
Python+Djangoで作成しました

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
- タグ作成
- 回答の作成者とそれ以外の人で見える情報をかえる
- ユーザー登録をしていなくても他人が公開している回答を見れるようにする．(ゲスト機能)
- 削除機能
- ユーザ検索

### これから実装したいこと
- タグ検索
- UI向上
- ログインしている本人，ログインしている他人，ログインしていない他人によってできることをきちんと管理
- 表示方法変更
- ログイン画面にゲストユーザとして使用するを入れる
- dockerfileとdocker-composeで環境構築
- テストを書く

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
