% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
<section class="container">
    <h3>グループ管理</h3>
    <div class="row">
        <div class="col-sm-12">
            <form action="/admin/group" id="km_group_search">
                <input type="submit" value="検索" class="btn btn-default km_progress_button">
            </form>
            <table class="table table-striped table-hover ">
                <thead>
                    <tr>
                    <th>ID</th>
                    <th>グループID</th>
                    <th>
                        <form action="/admin/group/edit" id="km_group_edit">
                            <input type="submit" value="追加" class="btn btn-default"/>
                        </form>
                    </th>
                    </tr>
                </thead>
                <tbody>
                    % for group in result['groups']:
                    <tr>
                        <form action="/admin/group/edit" id="km_group_edit">
                        <td><label id='km_group_id_" + group.id + "'>{{group.id}}</label></td>
                        <td><label id='km_group_name_id_" + group.name + "'>{{group.name}}</label></td>
                        <td>
                                <input type="hidden" value="{{group.id}}" name="km_group_edit_id" id="km_group_edit_id"/>
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