% include kokemomo/plugins/admin/view/header url=result['url'], user_id=result['user_id'], menu_list=result['menu_list']
    <head>
        <script src='{{result['url']("blog_static_tiny_js", filename="tinymce.min.js")}}'></script>
        <script src='{{result['url']("blog_static_js", filename="blog.js")}}'></script>
        <link href='{{result['url']("blog_static_css", filename="blog.css")}}' rel="stylesheet">
    </head>
        <section class="container">
            <div class="col-sm-3">
                <div class="jumbotron">
                    <ul>
                        <li><a href="/blog/admin">ダッシュボード</a></li>
                        <li><a href="/blog/admin/category_list">カテゴリ一覧</a></li>
                        <li><a href="/blog/admin/article_list">記事一覧</a></li>
                        <li><a href="/blog/admin/subscription">購読一覧</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-sm-9">
                <div class="jumbotron">
                    % if result['type'] == 'dashboard':
                        % include kokemomo/plugins/blog/view/dashboard url=result['url'], result=result
                    % elif result['type'] == 'info':
                        % include kokemomo/plugins/blog/view/info url=result['url'], result=result
                    % elif result['type'] == 'category_list':
                        % include kokemomo/plugins/blog/view/category_list url=result['url'], result=result
                    % elif result['type'] == 'category':
                        % include kokemomo/plugins/blog/view/category url=result['url'], result=result
                    % elif result['type'] == 'article_list':
                        % include kokemomo/plugins/blog/view/article_list url=result['url'], result=result
                    % elif result['type'] == 'article':
                        % include kokemomo/plugins/blog/view/article url=result['url'], result=result
                    % elif result['type'] == 'result':
                        % include kokemomo/plugins/blog/view/result url=result['url'], result=result
                    % end
                </div>
            </div>
        </section>
