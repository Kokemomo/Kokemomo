% include kokemomo/plugins/admin/view/header url=url, user_id=user_id, menu_list=menu_list
        <section class="container">
            <h3>グループ管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <p>グループ情報</p>
                    <input type="button" value="検索" id="km_group_search"/>
                    <input type="button" value="更新" id="km_group_save"/>
                    <input type="button" value="行追加" id="km_group_add_row"/>
                    <table class="table" id="km_group_list">
                        <thead>
                            <tr>
                                <td class="column_delete">削除</td>
                                <td class="column_normal">ID</td>
                                <td class="column_normal">グループ名</td>
                                <td class="column_normal">親ID</td>
                            </tr>
                        </thead>
                    </table>
                </div>
            </div>
        </section>