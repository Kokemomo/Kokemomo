% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
<section class="container">
    <h3>汎用パラメータ管理</h3>
    <div class="row">
        <div class="col-sm-12">
            <form action="/admin/parameter" id="km_parameter_search">
                <input type="submit" value="検索" class="btn btn-default km_progress_button">
            </form>
            <table class="table table-striped table-hover ">
                <thead>
                    <tr>
                    <th>ID</th>
                    <th>Key</th>
                    <th>Data</th>
                    <th>
                        <form action="/admin/parameter/edit" id="km_parameter_edit">
                            <input type="submit" value="追加" class="btn btn-default"/>
                        </form>
                    </th>
                    </tr>
                </thead>
                <tbody>
                    % for parameter in result['parameters']:
                    <tr>
                        <form action="/admin/parameter/edit" id="km_parameter_edit">
                        <td><label id='km_parameter_id_" + parameter.id + "'>{{parameter.id}}</label></td>
                        <td><label id='km_parameter_key_" + parameter.id + "'>{{parameter.key}}</label></td>
                        <td><label id='km_parameter_data_" + parameter.id + "'>{{parameter.data}}</label></td>
                        <td>
                                <input type="hidden" value="{{parameter.id}}" name="km_parameter_edit_id" id="km_parameter_edit_id"/>
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