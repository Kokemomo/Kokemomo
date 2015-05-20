% include kokemomo/plugins/admin/view/header url=url, user_id=user_id, menu_list=menu_list
        <section class="container">
            <h3>ユーザー管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <p>ユーザー情報</p>
                    <input type="button" value="検索" id="km_user_search"/>
                    <input type="button" value="更新" id="km_user_save"/>
                    <input type="button" value="行追加" id="km_user_add_row"/>
                    <table class="table" id="km_user_list">
                        <thead>
                            <tr>
                                <td class="column_delete">削除</td>
                                <td class="column_normal">ID</td>
                                <td class="column_normal">ユーザーID</td>
                                <td class="column_normal">ユーザー名</td>
                                <td class="column_normal">パスワード</td>
                                <td class="column_normal">メールアドレス</td>
                                <td class="column_normal">グループID</td>
                                <td class="column_normal">ロールID</td>
                            </tr>
                        </thead>
                    </table>
                </div>
            </div>
        </section>