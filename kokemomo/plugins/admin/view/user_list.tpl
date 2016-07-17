% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
        <section class="container">
            <h3>ユーザー管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <p>ユーザー情報</p>
                    <form action="/admin/user" id="km_user_search">
                    <input type="submit" value="検索">
                    </form>
                    <div class="list">
                        <ul class="header">
                            <li>
                                <span>ID</span>
                                <span>ユーザーID</span>
                                <span>
                                <form action="/admin/user/edit" id="km_user_edit">
                                    <input type="submit" value="追加"/>
                                </form>
                                </span>
                            </li>
                        </ul>
                        <ul class="body">
                            % for user in result['users']:
                                <li>
                                    <form action="/admin/user/edit" id="km_user_edit">
                                    <span><label id='km_user_id_" + user.id + "'>{{user.id}}</label></span>
                                    <span><label id='km_user_user_id_" + user.id + "'>{{user.user_id}}</label></span>
                                    <span>
                                            <input type="hidden" value="{{user.id}}" name="km_user_edit_id" id="km_user_edit_id"/>
                                            <input type="submit" value="編集"/>
                                    </span>
                                    </form>
                                </li>
                            % end
                        </ul>
                    </div>
                </div>
            </div>
        </section>