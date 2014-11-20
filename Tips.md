# *~~~~~Kokemomo Tips~~~~~~~~~*
## kokemomo.iniのセクション一覧

各セクションにアクセスするモジュール：kokemomo/plugins/engine/utils/config.py


### データベース接続
get_database_setting(アプリケーション名)で取得
-----------------------------
[Database_アプリケーション名]
rdbms=sqlite
schema=data.db
-----------------------------

### データベースプーリング
get_database_pool_setting()で取得
-----------------------------
[Database_Pool_アプリケーション名]
recycle=3600
-----------------------------

### アプリケーション文字コード
get_character_set_setting()で取得
-----------------------------
[Character_Set]
charset=utf-8
-----------------------------

### テスト用ログイン
ログイン時にadmin/adminまたはadmin2/admin2でログインできるかどうか(falseでOFF)
-----------------------------
[Test_Setting]
test_login=true
-----------------------------

## データベースのセッション操作
モジュール：kokemomo/plugins/engine/controller/km_db_manager.py

### コントローラの先頭でマネージャを定義
db_manager = KMDBManager("アプリケーション名")

### 各メソッドで以下のように利用
try:
    session = db_manager.get_session()
    ～DBアクセス～
finally:
    session.close()

## エラー発生時のログ出力
モジュール：kokemomo/plugins/engine/controller/km_exception.py

@route('パス')
@log
def get():
　～メソッドの処理～

## ログインチェック
モジュール：kokemomo/plugins/engine/controller/km_access_check.py

@route('パス')
@check_login(request, response)
def get():
　～メソッドの処理～

## アクセスチェック
モジュール：kokemomo/plugins/engine/controller/km_access_check.py
※現状ロールの判定のみ、グループの判定は未実装

@route('パス')
@access_check(request)
def get():
　～メソッドの処理～

### アクセスチェックの仕組み
ログインユーザーに紐づくロール情報(KMRole)を元にチェックを行う。
※KMRoleの定義
name:ロール名
target:チェック対象(/アプリケーション/機能/サブ機能まで設定可)
is_allow:許可するかどうか

例：
target：/app/document/find
is_allow：False
http://localhost:8861/app/document/findでアクセスした場合はエラーになる


## モデルの作成
詳細はkokemomo/plugins/engine/model/の各モデルを参照

### 以下の定義でDBマネージャとユーティリティをインポート
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_db_manager import Base

### モデルには以下のメソッドを定義しておく
　　def __repr__(self):
　　　　return create_repr_str(self) # モデルの文字列表現を生成

　　def get_json(self):
　　　　return create_json(self) # モデルのJSONを生成

### 他のモデルと結合している場合はJSON生成を以下のようにする
　　def get_json(self):
　　　　result = "{"
　　　　result += '"結合元モデルクラス名":' + create_json(self)
　　　　result += ',"結合先モデルクラス名":' + create_json(self.モデルクラス変数)
　　　　result += "}"
　　　　return result




## Ajax通信
モジュール：
kokemomo/plugins/engine/view/resource/js/communication.js
kokemomo/plugins/engine/util/km_utils.py

GETの場合
-----------------------------------
### クライアント側
$("#btn").click(function(){
　　var value="hoge";
　　send(SendType[1], '/app/action', value, func);
});

function func(status, json){
　　if(status == 200){
　　　　// 成功処理
		console.log(json); // {"result":"hoge"}
　　}
}

### サーバー側
@route('/app/action', method='POST')
def post():
　　result = request.params.get('value') # GETパラメータの取得
　　return create_result(result) # 結果をJSONへ変換
-----------------------------------

POSTの場合
-----------------------------------
### クライアント側
$("#btn").click(function(){
　　var value="hoge";
　　send(SendType[2], '/app/action', value, func);
});

function func(status, json){
　　if(status == 200){
　　　　// 成功処理
		console.log(json); // {"result":"hoge"}
　　}
}

### サーバー側
@route('/app/action', method='POST')
def post():
　　result = request.forms.get('value') # GETパラメータの取得
　　return create_result(result) # 結果をJSONへ変換
-----------------------------------

※コールバック関数にオプションを指定する方法
-----------------------------------
### クライアント側
$("#btn").click(function(){
　　var value="hoge";
	var option = "fuga";
　　send(SendType[2], '/app/action', value, func, option);
});

function func(status, json, option){
	console.log(option); // fuga
　　if(status == 200){
　　　　// 成功処理
　　}
}
-----------------------------------

※結果としてモデルのリストを返す場合
　list = [model1,model2]
　return create_result_4_array(list)

　結果のJSON：{"result":[model1から生成されたJSON,model2から生成されたJSON]}


## ログインユーザーIDの取得
モジュール：kokemomo/plugins/engine/view/resource/js/communication.js
-----------------------------------
### クライアント側
user_id = getUserId();

### サーバー側
user_id = request.cookies['user_id'] # ログインユーザーIDの取得
-----------------------------------

