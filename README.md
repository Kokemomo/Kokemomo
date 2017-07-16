# KOKEMOMO CMS

これはPython Bottle Frameworkを使ったCMSです。

## 現在の機能
+ ~~ファイルアップロード~~
+ ~~パラメータの検索、登録（更新）、削除~~
+ ユーザー登録
+ ログイン
+ プラグイン登録
+ ~~Facebook認証~~(現在改修中)
+ ~~レコメンドエンジン~~(現在改修中)
+ ブログ

## 動作環境
+ Python 3.6.1
+ 使用ライブラリはrequirements.txtを参照

## セットアップ
### 依存モジュールをインストールする
pip install -r requirements.txt
### 開発用サーバーを起動する
python simple_cms.py -s common  

※commonはデフォルトの設定ファイル名です。  
任意の設定ファイルを追加し、切り替えることが出来ます。  

### CMSへアクセスする
http://localhost:8861/admin/login  
※テスト用にadmin/adminでログイン可

### ディレクトリ構成
  root  
  ├application … 開発したアプリケーションの格納先  
  │　├data … ファイルアップロードデータ  
  │　├lib … 外部ライブラリ  
  │　├plugins … プラグイン  
  ├kokemomo … KOKEMOMO本体  
  │　├data … ファイルアップロードデータ  
  │　├lib … 外部ライブラリ  
  │　├plugins … プラグイン  
  │　├settings … 設定ファイル  
  └ simple_cms.py … 起動スクリプト  


### CMSの拡張(プラグインの開発)

### 履歴
  0.0.1 新規作成、ファイルアップロード  
  0.0.2 パラメータ管理  
  0.0.3 ユーザー管理、ディレクトリ構成整理  
  0.0.4 Facebook認証  
  0.0.5 レコメンドエンジン追加  
  0.0.6 汎用エントリ機能追加  
  0.1.0 ベータ　開発しやすいようにアーキテクチャの変更、管理画面、ブログプラグイン

### リリース予定
