% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% parameter = result['parameter']
<section class="container">
    <div class="row">
        <div class="col-sm-12">
            <div class="jumbotron">
                <form action="/admin/parameter/save" method="post" id="parameter_save" class="km_form" class="form-horizontal">
                    <fieldset>
                        <legend>パラメータ情報</legend>
                        <div class="form-group">
                            <label for="id" class="col-lg-2 control-label">ID</label>
                            <div class="col-lg-10">
                                <input type="label" value="{{parameter.id}}" class="form-control" readonly><input type="hidden" id="id" name="id" value="{{parameter.id}}">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="key" class="col-lg-2 control-label">Key</label>
                            <div class="col-lg-10">
                                <input type="text" id="key" name="key" value="{{parameter.key}}" class="form-control" placeholder="キー">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="data" class="col-lg-2 control-label">Data</label>
                            <div class="col-lg-10">
                                <input type="text" id="data" name="data" value="{{parameter.data}}" class="form-control" placeholder="データ">
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