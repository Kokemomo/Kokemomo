% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
<section class="container">
    <h3>ユーザー管理</h3>
    <div class="row">
        <div class="col-sm-12">
            <form action="/admin/user" id="km_user_search">
                <input type="submit" value="検索" class="btn btn-default km_progress_button">
            </form>
            <table class="table table-striped table-hover ">
                <thead>
                    <tr>
                    <th>ID</th>
                    <th>ユーザーID</th>
                    <th>
                        <form action="/admin/user/edit" id="km_user_edit">
                            <input type="submit" value="追加" class="btn btn-default"/>
                        </form>
                    </th>
                    </tr>
                </thead>
                <tbody>
                    % for user in result['users']:
                    <tr>
                        <form action="/admin/user/edit" id="km_user_edit">
                        <td><label id='km_user_id_" + user.id + "'>{{user.id}}</label></td>
                        <td><label id='km_user_user_id_" + user.id + "'>{{user.user_id}}</label></td>
                        <td>
                                <input type="hidden" value="{{user.id}}" name="km_user_edit_id" id="km_user_edit_id"/>
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