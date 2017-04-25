% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% group = result['group']
<section class="container">
    <div class="row">
        <div class="col-sm-12">
            <div class="jumbotron">
                <form action="/admin/group/save" method="post" id="group_save" class="km_form" class="form-horizontal">
                    <fieldset>
                        <legend>グループ情報</legend>
                        <div class="form-group">
                            <label for="id" class="col-lg-2 control-label">ID</label>
                            <div class="col-lg-10">
                                <input type="label" value="{{group.id}}" class="form-control" readonly><input type="hidden" id="id" name="id" value="{{group.id}}">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="name" class="col-lg-2 control-label">グループ名</label>
                            <div class="col-lg-10">
                                <input type="text" id="name" name="name" value="{{group.name}}" class="form-control" placeholder="グループ名">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="parent_id" class="col-lg-2 control-label">親ID</label>
                            <div class="col-lg-10">
                                <select class="form-control" id="parent_id" name="parent_id">
                                    <option value="None">---</option>
                                    % for parent_group in result['groups']:
                                    %   if parent_group.id is group.parent_id:
                                    <option value={{parent_group.id}} selected>{{ parent_group.name }}</option>
                                    %   elif parent_group.id is not group.id:
                                    <option value={{parent_group.id}}>{{ parent_group.name }}</option>
                                    %   end
                                    % end
                                </select>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="delete" class="col-lg-2 control-label">削除</label>
                            <div class="col-lg-10">
                                <input type="checkbox" id="delete" name="delete" class="form-control">
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="col-lg-10">
                                <input type="submit" value="更新" class="btn btn-default">
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>
    </div>
</section>