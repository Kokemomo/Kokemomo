        <section class="container">
            <div class="col-sm-12">
                <h3>カテゴリ一覧</h3>
                % if 'info' in values and len(values['info']) != 0:
                <div class="menu">
                    [<a href="/blog/admin?type=category">カテゴリを作成</a>]
                </div>
                % else:
                    [<a href="/blog/admin?type=info">ブログを作成</a>]
                % end
                <div class="box">
                % if 'info' in values and len(values['info']) != 0:
                    % if 'category' in values and len(values['category']) != 0:
                        <ul>
                        % for category in values['category']:
                            <li>
                                <span>{{category.name}}</span>
                                [<a href="/blog/admin?type=category&id={{category.id}}">編集</a>]
                                [<a href="/blog/admin?type=category_list&id={{category.id}}&delete=true">削除</a>]
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