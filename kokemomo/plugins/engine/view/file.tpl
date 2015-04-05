% include kokemomo/plugins/engine/view/header url=url, user_id=user_id, menu_list=menu_list
        <section class="container">
            <h3>ファイル管理</h3>
            <div class="row">
                <div class="col-sm-3">
                    <div class="panel panel-default">
                        <div class="panel-body">
                            <select id="dirList" name="dirList">
                                %for dir in dirs:
                                <option>{{dir}}</option>
                                %end
                            </select>
                        </div>
                        <div class="panel-footer">
                            <ul id="fileList" class="nav nav-list">
                                <li class="nav-header">files</li>
                                %for file in files:
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
