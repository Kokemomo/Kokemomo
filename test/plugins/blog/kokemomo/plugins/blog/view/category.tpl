        <section class="container">
            % category = values['category']
            % info_list = values['info']
            <div class="col-sm-12">
                <h3>カテゴリ作成</h3>
                <div class="box">
                    <form id="form" action="/blog/admin/create_category" method="post">
                        <input type="hidden" name="id" id="id" value="{{category.id}}">
                        <table class="table">
                            <tr class="row">
                                <th width="100px">ブログ</th>
                                <td>
                                    <select id="info_id" name="info_id">
                                    % for info in info_list:
                                        % if info.id == category.info_id:
                                        <option value="{{info.id}}" selected>{{info.name}}</option>
                                        % else:
                                        <option value="{{info.id}}">{{info.name}}</option>
                                        % end
                                    % end
                                    </select>
                                </td>
                            </tr>
                            <tr class="row">
                                <th width="100px">カテゴリ名<span class="required">*</span></th>
                                <td>
                                    <input type="text" name="name" id="name" value="{{category.name}}">
                                    % if 'error' in values and values['error'].have('name'):
                                        <label class="error">{{values['error'].get('name')['message']}}</label>
                                    % end
                                </td>
                            </tr>
                        </table>
                        <input type="submit">
                    </form>
                </div>
            </div>
        </section>