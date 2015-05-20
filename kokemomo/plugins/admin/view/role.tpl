% include kokemomo/plugins/admin/view/header url=url, user_id=user_id, menu_list=menu_list
        <section class="container">
            <h3>ロール管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <p>ロール情報</p>
                    <input type="button" value="検索" id="km_role_search"/>
                    <input type="button" value="更新" id="km_role_save"/>
                    <input type="button" value="行追加" id="km_role_add_row"/>
                    <table class="table" id="km_role_list">
                        <thead>
                            <tr>
                                <td  class="column_delete">削除</td>
                                <td  class="column_normal">ID</td>
                                <td  class="column_normal">ロール名</td>
                                <td  class="column_normal">対象URL</td>
                                <td  class="column_normal">許可</td>
                            </tr>
                        </thead>
                    </table>
                </div>
            </div>
        </section>