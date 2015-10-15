        <section class="container">
            % info = values['info']
            <div class="col-sm-12">
                <h3>ブログ作成</h3>
                <div class="box">
                    <form id="form" action="/blog/admin/create_info" method="post">
                        <input type="hidden" name="id" id="id" value="{{info.id}}">
                        <table class="table">
                            <tr class="row">
                                <th width="100px">ブログ名<span class="required">*</span></th>
                                <td>
                                    <input type="text" name="name" id="name" value="{{info.name}}">
                                    % if 'error' in values and values['error'].have('name'):
                                        <label class="error">{{values['error'].get('name')['message']}}</label>
                                    % end
                                </td>
                            </tr>
                            <tr class="row">
                                <th width="100px">URL<span class="required">*</span></th>
                                <td>
                                    <input type="text" name="url" id="url" value="{{info.url}}">(/blog/入力したurlになります。)
                                    % if 'error' in values and values['error'].have('url'):
                                        <label class="error">{{values['error'].get('url')['message']}}</label>
                                    % end
                                </td>
                            </tr>
                            <tr class="row">
                                <th width="100px">詳細</th>
                                <td>
                                    <input type="text" name="description" id="description" value="{{info.description}}">
                                </td>
                            </tr>
                        </table>
                        <input type="submit">
                    </form>
                </div>
            </div>
        </section>