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
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
        <link href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/yeti/bootstrap.min.css" rel="stylesheet" integrity="sha384-HzUaiJdCTIY/RL2vDPRGdEQHHahjzwoJJzGUkYjHVzTwXFQ2QN/nVgX7tzoMW3Ov" crossorigin="anonymous">

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
        <section class="container">
            <div class="col-lg-12">
                <div class="page-header">
                    <h1 class="containers">{{info.name}}</h1>
                </div>
                <div class="bs-component">
                    <div class="row">
                        <div class="col-lg-12">
                            <ul class="nav nav-pills">
                            <li><a href="#">ホーム</a></li>
                            <li><a href="#">カテゴリ一覧</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="row">
                            <div class="col-lg-8">
                            % for article in info.articles:
                                <div class="jumbotron">
                                    <p>{{article.title}}</p>
                                    <small>{{!article.caption}}...</small>
                                    <p>
                                        <a class="btn btn-primary btn-sm">詳細</a>
                                    </p>
                                    <!--
                                    <div>{{!article.article}}</div>
                                    % for blog_comment in article.comments:
                                        <div class="comment"><span>{{blog_comment.created_at}} : {{blog_comment.comment}}</span></div>
                                    % end
                                    <form id="form" action="/blog/{{blog_url}}/add_comment" method="post">
                                    <input type="hidden" name="article_id" id="article_id" value="{{article.id}}">
                                    <div class="comment">
                                        <input type="text" name="comment" id="comment">
                                        <input type="submit" value="コメントする">
                                    </div>
                                    </form>
                                    -->
                                </div>
                            % end
                            </div>
                        </div>
                </div>
            </div>
        </section>
        <footer>
        </footer>
    </body>
</html>
