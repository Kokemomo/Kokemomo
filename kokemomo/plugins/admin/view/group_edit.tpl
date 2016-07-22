% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% group = result['group']
        <section class="container">
            <h3>グループ管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <form action="/admin/group/save" method="post" id="group_save">
                        <input type="submit" value="更新">
                        <div class="detail">
                            <ul>
                                <li>
                                    <span class="detail-header">削除</span><span><input type="checkbox" id="delete" name="delete"></span>
                                </li>
                                <li>
                                    <span class="detail-header">ID</span><span><input type="label" value="{{group.id}}" readonly><input type="hidden" id="id" name="id" value="{{group.id}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">グループ名</span><span><input type="text" id="name" name="name" value="{{group.name}}"></span>
                                </li>
                                <li>
                                    <span class="detail-header">親グループ</span><span><input type="text" id="parent_id" name="parent_id" value="{{group.parent_id}}"></span>
                                </li>
                            </ul>
                        </div>
                    </form>
                </div>
            </div>
        </section>