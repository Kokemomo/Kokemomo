        <section class="container">
            <div class="col-sm-12">
                <h3>カテゴリ一覧</h3>
                <div class="menu">
                    [<a href="/blog/admin?type=category">カテゴリを作成</a>]
                </div>
                <div class="box">
                % if 'category' in values and len(values['category']) != 0:
                    <ul>
                    % for category in values['category']:
                        <li><span>{{category.name}}</span>[<a href="/blog/admin?type=category&id={{category.id}}">編集</a>]</li>
                    % end
                    </ul>
                % else:
                    <p>カテゴリがありません。</p>
                % end
                </div>
            </div>
        </section>