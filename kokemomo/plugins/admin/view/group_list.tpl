% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
        <section class="container">
            <h3>グループ管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <form action="/admin/group" id="km_group_search">
                    <input type="submit" value="検索">
                    </form>
                    <div class="list">
                        <ul class="header">
                            <li>
                                <span>ID</span>
                                <span>グループ名</span>
                                <span>
                                <form action="/admin/group/edit" id="km_group_edit">
                                    <input type="submit" value="追加"/>
                                </form>
                                </span>
                            </li>
                        </ul>
                        <ul class="body">
                            % for group in result['groups']:
                                <li>
                                    <form action="/admin/group/edit" id="km_group_edit">
                                    <span><label id='km_group_id_" + group.id + "'>{{group.id}}</label></span>
                                    <span><label id='km_group_name_" + group.name + "'>{{group.name}}</label></span>
                                    <span>
                                            <input type="hidden" value="{{group.id}}" name="km_group_edit_id" id="km_group_edit_id"/>
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