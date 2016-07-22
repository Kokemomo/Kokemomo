% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
        <section class="container">
            <h3>ロール管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <form action="/admin/role" id="km_role_search">
                    <input type="submit" value="検索">
                    </form>
                    <div class="list">
                        <ul class="header">
                            <li>
                                <span>ID</span>
                                <span>ロール名</span>
                                <span>
                                <form action="/admin/role/edit" id="km_role_edit">
                                    <input type="submit" value="追加"/>
                                </form>
                                </span>
                            </li>
                        </ul>
                        <ul class="body">
                            % for role in result['roles']:
                                <li>
                                    <form action="/admin/role/edit" id="km_role_edit">
                                    <span><label id='km_role_id_" + role.id + "'>{{role.id}}</label></span>
                                    <span><label id='km_role_name_" + role.name + "'>{{role.name}}</label></span>
                                    <span>
                                            <input type="hidden" value="{{role.id}}" name="km_role_edit_id" id="km_role_edit_id"/>
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