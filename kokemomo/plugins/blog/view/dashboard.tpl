        <section class="container">
            <div class="col-sm-12">
                <h3>ブログ一覧</h3>
                <div class="menu">
                   [<a href="/blog/admin?type=info">ブログを作成</a>]
                </div>
                <div class="box">
                % if 'info' in values and len(result['info']) != 0:
                    <ul>
                    % for info in result['info']:
                        <li>
                            <a href="/blog/{{info.url}}">{{info.name}}</a>
                            [<a href="/blog/admin?type=info&id={{info.id}}">編集</a>]
                            [<a href="/blog/admin?type=dashboard&id={{info.id}}&delete=true">削除</a>]
                        </li>
                    % end
                    </ul>
                % else:
                    <p>ブログがありません。</p>
                % end
                </div>
                <br>

            </div>
        </section>