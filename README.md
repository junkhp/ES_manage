# ES質問まとめアプリ
ESの質問に対する自分の回答を一括管理するwebアプリです

Python+Djangoで作成しました．

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
### これから実装したいこと
- 検索機能(ユーザー検索, タグ検索)
- UI向上


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
