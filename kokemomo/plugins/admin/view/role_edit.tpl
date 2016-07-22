% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% role = result['role']
        <section class="container">
            <h3>ロール管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <form action="/admin/role/save" method="post" id="user_save">
                        <input type="submit" value="更新">
                        <div class="detail">
                            <ul>
                                <li>
                                    <span class="detail-header">削除</span><span><input type="checkbox" id="delete" name="delete"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ID</span><span><input type="label" value="{{role.id}}" readonly><input type="hidden" id="id" name="id" value="{{role.id}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ロール名</span><span><input type="text" id="name" name="name" value="{{role.name}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ターゲット</span><span><input type="text" id="target" name="target" value="{{role.target}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">許可</span><span><input type="checkbox" id="is_allow" name="is_allow" value="{{role.is_allow}}"></span>
                                </li>
                            </ul>
                        </div>
                    </form>
                </div>
            </div>
        </section>