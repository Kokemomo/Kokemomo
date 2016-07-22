% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% user = result['user']
        <section class="container">
            <h3>ユーザー管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <form action="/admin/user/save" method="post" id="user_save">
                        <input type="submit" value="更新">
                        <div class="detail">
                            <ul>
                                <li>
                                    <span class="detail-header">削除</span><span><input type="checkbox" id="delete" name="delete"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ID</span><span><input type="label" value="{{user.id}}" readonly><input type="hidden" id="id" name="id" value="{{user.id}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ユーザーID</span><span><input type="text" id="user_id" name="user_id" value="{{user.user_id}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ユーザー名</span><span><input type="text" id="name" name="name" value="{{user.name}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">パスワード</span><span><input type="text" id="password" name="password" value="{{user.password}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">メールアドレス</span><span><input type="text" id="mail_address" name="mail_address" value="{{user.mail_address}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">グループID</span><span><input type="text" id="group_id" name="group_id" value="{{user.group_id}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ロールID</span><span><input type="text" id="role_id" name="role_id" value="{{user.role_id}}"></span>
                                </li>
                            </ul>
                        </div>
                    </form>
                </div>
            </div>
        </section>