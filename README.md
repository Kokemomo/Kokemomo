# KOKEMOMO CMS

これはPython Bottle Frameworkを使ったCMSです。

## 現在の機能
+ ファイルアップロード
+ パラメータの検索、登録（更新）、削除
+ ユーザー登録
+ ログイン
+ プラグイン登録
+ Facebook認証
+ レコメンドエンジン

## 動作環境
+ Python 2.7.6
+ pip 1.5.4
+ SQLAlchemy 0.9.4
+ Beaker 1.6.4
+ bottle-auth 0.3.3
+ nose 1.3.4(テストのみ)

## セットアップ
### 開発用サーバーを起動する
python simple_cms.py
### CMSへアクセスする
http://localhost:8861/login
※テスト用にadmin/adminでログイン可

### ディレクトリ構成
  root
  ├kokemomo … KOKEMOMO本体
  │　├data … ファイルアップロードデータ
  │　├lib … 外部ライブラリ
  │　├plugins … プラグイン
  │　├templates … テンプレート
  └ simple_cms.py … 起動スクリプト


### CMSの拡張(プラグインの開発)

### 履歴
  0.1.0 新規作成、ファイルアップロード
  0.2.0 パラメータ管理
  0.3.0 ユーザー管理、ディレクトリ構成整理
  0.4.0 Facebook認証
  0.5.0 レコメンドエンジン追加
  0.6.0 汎用エントリ機能追加
