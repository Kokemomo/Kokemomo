% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
% user = result['user']
        <section class="container">
            <div class="row">
                <div class="col-sm-12">
                    <form action="/admin/user/save" method="post" id="user_save" class="km_form" class="form-horizontal">
                        <fieldset>
                            <legend>ユーザー情報</legend>
                            <div class="form-group">
                                <label for="delete" class="col-lg-2 control-label">削除</label>
                                <div class="col-lg-10">
                                    <input type="checkbox" id="delete" name="delete" class="form-control">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="id" class="col-lg-2 control-label">ID</label>
                                <div class="col-lg-10">
                                    <input type="label" value="{{user.id}}" class="form-control" readonly><input type="hidden" id="id" name="id" value="{{user.id}}">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="user_id" class="col-lg-2 control-label">ユーザーID</label>
                                <div class="col-lg-10">
                                    <input type="text" id="user_id" name="user_id" value="{{user.user_id}}" class="form-control" placeholder="UserID">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="user_name" class="col-lg-2 control-label">ユーザー名</label>
                                <div class="col-lg-10">
                                    <input type="text" id="user_name" name="user_name" value="{{user.name}}" class="form-control" placeholder="UserName">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="password" class="col-lg-2 control-label">パスワード</label>
                                <div class="col-lg-10">
                                    <input type="text" id="password" name="password" value="{{user.password}}" class="form-control" placeholder="Password">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="mail_address" class="col-lg-2 control-label">メールアドレス</label>
                                <div class="col-lg-10">
                                    <input type="text" id="mail_address" name="mail_address" value="{{user.mail_address}}" class="form-control" placeholder="MailAddress">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="group_id" class="col-lg-2 control-label">グループID</label>
                                <div class="col-lg-10">
                                    <input type="text" id="group_id" name="group_id" value="{{user.group_id}}" class="form-control" placeholder="GroupID">
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="role_id" class="col-lg-2 control-label">ロールID</label>
                                <div class="col-lg-10">
                                    <input type="text" id="role_id" name="role_id" value="{{user.role_id}}" class="form-control" placeholder="RoleID">
                                </div>
                            </div>
                            <div class="form-group">
                                <input type="submit" value="更新" class="btn btn-default">
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </section>