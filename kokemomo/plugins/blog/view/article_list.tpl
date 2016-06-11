        <section class="container">
            <div class="col-sm-12">
                <h3>記事一覧</h3>
                <div class="box">
                % if 'info' in result and len(result['info']) != 0:
                    % for info in result['info']:
                        <h4>{{info.name}}の記事</h4>
                        <div class="menu">
                            [<a href="/blog/admin/article?info_id={{info.id}}">記事を作成</a>]
                        </div>
                        <div class="box">
                            <ul>
                            % if len(info.articles) == 0:
                                <li>記事がありません。</li>
                            % end
                            % for article in info.articles:
                                <li>
                                    <span>{{article.title}}</span>
                                    [<a href="/blog/admin/article?info_id={{info.id}}&id={{article.id}}">編集</a>]
                                    [<a href="/blog/admin/delete_article?id={{article.id}}">削除</a>]
                                </li>
                            % end
                            </ul>
                        </div>
                    % end
                % else:
                    [<a href="/blog/admin/info">ブログを作成</a>]
                    <p>ブログがありません。</p>
                % end
                </div>
            </div>
        </section>