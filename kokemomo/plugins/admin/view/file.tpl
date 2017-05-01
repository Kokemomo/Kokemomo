% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']<section class="container">
    <h3>ファイル管理</h3>
    <div class="row">
        <div class="col-sm-3">
            <div class="panel panel-default">
                <div class="panel-body">
                    <select id="dirList" name="dirList">
                        %for dir in result['dirs']:
                        <option>{{dir}}</option>
                        %end
                    </select>
                </div>
                <div class="panel-footer">
                    <ul id="fileList" class="nav nav-list">
                        <li class="nav-header">files</li>
                        %for file in result['files']:
                        <li>{{file}}</li>
                        %end
                    </ul>
                </div>
            </div>
        </div>
        <div class="col-sm-6">
            <div id="dropArea" name="dropArea" class="jumbotron">File Drop Area</div>
        </div>
    </div>
</section>
