% include kokemomo/plugins/admin/view/header url=url, user_id=user_id, menu_list=menu_list
    <head>
        <script src='{{url("blog_static_tiny_js", filename="tinymce.min.js")}}'></script>
        <script src='{{url("blog_static_js", filename="blog.js")}}'></script>
        <link href='{{url("blog_static_css", filename="blog.css")}}' rel="stylesheet">
    </head>
        <section class="container">
            <div class="col-sm-3">
                <div class="jumbotron">
                    <ul>
                        <li><a href="/blog/admin?type=dashboard">ダッシュボード</a></li>
                        <li><a href="/blog/admin?type=category_list">カテゴリ一覧</a></li>
                        <li><a href="/blog/admin?type=article_list">記事一覧</a></li>
                        <li><a href="/blog/admin?type=subscription">購読一覧</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-sm-9">
                <div class="jumbotron">
                    % if type == 'dashboard':
                        % include kokemomo/plugins/blog/view/dashboard url=url, values=values
                    % elif type == 'info':
                        % include kokemomo/plugins/blog/view/info url=url, values=values
                    % elif type == 'category_list':
                        % include kokemomo/plugins/blog/view/category_list url=url, values=values
                    % elif type == 'category':
                        % include kokemomo/plugins/blog/view/category url=url, values=values
                    % elif type == 'article_list':
                        % include kokemomo/plugins/blog/view/article_list url=url, values=values
                    % elif type == 'article':
                        % include kokemomo/plugins/blog/view/article url=url, values=values
                    % elif type == 'result':
                        % include kokemomo/plugins/blog/view/result url=url, values=values
                    % end
                </div>
            </div>
        </section>
