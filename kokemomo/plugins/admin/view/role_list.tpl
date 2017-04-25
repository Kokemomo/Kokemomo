% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
<section class="container">
    <h3>ロール管理</h3>
    <div class="row">
        <div class="col-sm-12">
            <form action="/admin/role" id="km_role_search">
                <input type="submit" value="検索" class="btn btn-default km_progress_button">
            </form>
            <table class="table table-striped table-hover ">
                <thead>
                    <tr>
                    <th>ID</th>
                    <th>ロールID</th>
                    <th>
                        <form action="/admin/role/edit" id="km_role_edit">
                            <input type="submit" value="追加" class="btn btn-default"/>
                        </form>
                    </th>
                    </tr>
                </thead>
                <tbody>
                    % for role in result['roles']:
                    <tr>
                        <form action="/admin/role/edit" id="km_role_edit">
                        <td><label id='km_role_id_" + role.id + "'>{{role.id}}</label></td>
                        <td><label id='km_role_name_id_" + role.name + "'>{{role.name}}</label></td>
                        <td>
                                <input type="hidden" value="{{role.id}}" name="km_role_edit_id" id="km_role_edit_id"/>
                                <input type="submit" value="編集" class="btn btn-default"/>
                        </td>
                        </form>
                    </tr>
                    % end
                </tbody>
            </table>
        </div>
    </div>
</section>