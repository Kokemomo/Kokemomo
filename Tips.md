# *Kokemomo Tips*
### テスト用ログイン

設定ファイルのTEST_LOGINがTrueの場合、/admin/loginで
admin/adminまたはadmin2/admin2でログインができます。

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


### モデルには以下のメソッドを定義しておく

### 他のモデルと結合している場合はJSON生成を以下のようにする

## Ajax通信

モジュール：
kokemomo/plugins/engine/view/resource/js/communication.js
kokemomo/plugins/engine/util/km_utils.py

GETの場合

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

POSTの場合

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

※コールバック関数にオプションを指定する方法

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

※結果としてモデルのリストを返す場合

    　list = [model1,model2]
    　return create_result_4_array(list)

　結果のJSON：{"result":[model1から生成されたJSON,model2から生成されたJSON]}


## ログインユーザーIDの取得

モジュール：kokemomo/plugins/engine/view/resource/js/communication.js

### クライアント側

    user_id = getUserId();

### サーバー側

    user_id = request.cookies['user_id'] # ログインユーザーIDの取得


## ブログプラグインについて

・ブログは以下の様なデータで構成されます。

ブログ
├info ブログの情報
├subscription 購読情報　※現在未使用
└category カテゴリ
　└article 記事
　└comment コメント

### ブログプラグインのテンプレートについて

ブログプラグインのテンプレートでは以下の値が使用できます。

・ブログのurl
blog_url

・ブログ情報
info.id ブログのID
info.name ブログ名
info.url ブログのurl
info.description ブログの詳細

・記事
info.articles 記事の配列
info.articles[index].id 記事のID
info.articles[index].info_id ブログ情報のID
info.articles[index].title 記事のタイトル
info.articles[index].article 記事の内容
info.articles[index].post_date 投稿日

・コメント
info.articles[index].comments コメントの一覧
info.articles[index].comments[index].id コメントのID
info.articles[index].comments[index].article_id 記事のID
info.articles[index].comments[index].comment コメントの内容
info.articles[index].comments[index].created_at コメントの作成日時



