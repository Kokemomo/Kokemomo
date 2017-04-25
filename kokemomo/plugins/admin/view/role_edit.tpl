% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% role = result['role']
<section class="container">
    <div class="row">
        <div class="col-sm-12">
            <div class="jumbotron">
                <form action="/admin/role/save" method="post" id="role_save" class="km_form" class="form-horizontal">
                    <fieldset>
                        <legend>ロール情報</legend>
                        <div class="form-group">
                            <label for="id" class="col-lg-2 control-label">ID</label>
                            <div class="col-lg-10">
                                <input type="label" value="{{role.id}}" class="form-control" readonly><input type="hidden" id="id" name="id" value="{{role.id}}">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="name" class="col-lg-2 control-label">ロール名</label>
                            <div class="col-lg-10">
                                <input type="text" id="name" name="name" value="{{role.name}}" class="form-control" placeholder="ロール名">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="target" class="col-lg-2 control-label">ターゲット</label>
                            <div class="col-lg-10">
                                <input type="text" id="target" name="target" value="{{role.target}}" class="form-control" placeholder="ターゲット">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="is_allow" class="col-lg-2 control-label">許可</label>
                            <div class="col-lg-10">
                                % if role.is_allow:
                                <input type="checkbox" id="is_allow" name="is_allow" value="{{role.is_allow}}" class="form-control" checked="checked">
                                % else:
                                <input type="checkbox" id="is_allow" name="is_allow" value="{{role.is_allow}}" class="form-control">
                                % end
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