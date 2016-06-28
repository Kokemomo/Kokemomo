% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
        <section class="container">
            <h3>ユーザー管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <p>ユーザー情報</p>
                    <input type="button" value="検索" id="km_user_search"/>
                    <input type="button" value="更新" id="km_user_save"/>
                    <input type="button" value="行追加" id="km_user_add_row"/>
                    <div class="box">
                    <ul>
                        <li>
                            <span>削除</span>
                            <span>ID</span>
                            <span>ユーザーID</span>
                            <span>ユーザー名</span>
                            <span>パスワード</span>
                            <span>メールアドレス</span>
                            <span>グループID</span>
                            <span>ロールID</span>
                        </li>
                    </ul>
                    <ul>
                        % for user in result['users']:
                            <li>
                                <input type='checkbox' id='km_user_check_" + user.id + "'>
                                <input type='text' id='km_user_id_" + user.id + "' value="{{user.id}}" readonly>
                                <input type='text' id='km_user_user_id_" + user.id + "' value="{{user.user_id}}">
                                <input type='text' id='km_user_name_" + user.id + "' value="{{user.name}}">
                                <input type='text' id='km_user_password_" + user.id + "' value="{{user.password}}">
                                <input type='text' id='km_user_mail_address_" + user.id + "' value="{{user.mail_address}}">
                                <input type='text' id='km_user_group_id_" + user.id + "' value="{{user.group_id}}">
                                <input type='text' id='km_user_role_id_" + user.id + "' value="{{user.role_id}}">
                            </li>
                        % end
                    </ul>
                </div>
            </div>
        </section>