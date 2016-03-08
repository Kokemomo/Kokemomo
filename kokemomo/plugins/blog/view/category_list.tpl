        <section class="container">
            <div class="col-sm-12">
                <h3>カテゴリ一覧</h3>
                % if 'info' in result and len(result['info']) != 0:
                <div class="menu">
                    [<a href="/blog/admin/category">カテゴリを作成</a>]
                </div>
                % else:
                    [<a href="/blog/admin/info">ブログを作成</a>]
                % end
                <div class="box">
                % if 'info' in result and len(result['info']) != 0:
                    % if 'category' in result and len(result['category']) != 0:
                        <ul>
                        % for category in result['category']:
                            <li>
                                <span>{{category.name}}</span>
                                [<a href="/blog/admin/category?id={{category.id}}">編集</a>]
                                [<a href="/blog/admin/delete_category?id={{category.id}}">削除</a>]
                            </li>
                        % end
                        </ul>
                    % else:
                        <p>カテゴリがありません。</p>
                    % end
                % else:
                    <p>ブログがありません。</p>
                % end
                </div>
            </div>
        </section>