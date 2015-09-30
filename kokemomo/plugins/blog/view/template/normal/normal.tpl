<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{{values['info'].name}}</title>
        <!-- Bootstrap -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
        <script src="http://code.jquery.com/ui/1.11.0/jquery-ui.min.js"></script>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->

        <script src='{{url("engine_static_js", filename="communication.js")}}'></script>
        <script src='{{url("blog_static_normal_js", filename="normal.js")}}'></script>
        <link href='{{url("blog_static_normal_css", filename="normal.css")}}' rel="stylesheet">
    </head>
    <body>
    % info = values['info']
        <div class="header">
        </div>
        <section class="container">
            <div class="col-sm-12">
                <div>
                    <h2>{{info.name}}</h2>
                </div>
                % for article in info.articles:
                <div class="jumbotron">
                    <h2>{{article.title}}</h2>
                    <div>{{!article.article}}</div>
                    % for blog_comment in article.comments:
                        <div class="comment"><span>{{blog_comment.created_at}} : {{blog_comment.comment}}</span></div>
                    % end
                    <form id="form" action="/blog/{{blog_url}}/add_comment" method="post">
                    <input type="hidden" name="id" id="id" value="{{article.id}}">
                    <div class="comment">
                        <input type="text" name="comment" id="comment">
                        <input type="submit" value="コメントする">
                    </div>
                    </form>
                </div>
                % end
            </div>
        </section>
    </body>
</html>
