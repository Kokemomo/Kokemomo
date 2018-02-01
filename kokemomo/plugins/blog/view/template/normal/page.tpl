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
        <script src='{{url("blog_template_static_js", filename="normal.js")}}'></script>
        <link href='{{url("blog_template_static_css", filename="normal.css")}}' rel="stylesheet">
    </head>
    <body>
        % info = values['info']
        % article = values['article']
        % category = values['category']
        <header>
            <nav class="navbar navbar-default header-nav">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <a class="navbar-brand" href="/blog/{{info.name}}">Home</a>
                    </div>
                </div>
            </nav>
            <div class="header-wrapper">
                <img src='{{url("blog_template_static_img", filename="header.png")}}'>
                <p id="blog-name">{{info.name}}</p>
                <p id="blog-description">{{info.description}}</p>
            </div>
        </header>
        <section class="container tab-list">
            <div class="col-lg-8">
                <div class="bs-component">
                    <div class="row">
                        <ul class="breadcrumb">
                            <li><a href="/blog/{{info.name}}">Home</a></li>
                            <li class="active">{{category.name}}</li>
                        </ul>
                    </div>
                    <div class="row">
                        <div id="blogTabContent" class="tab-content">
                            <div id="article" class="jumbotron">
                                <h3>{{article.title}}</h3>
                                <p>{{!article.article}}</small>
                                % if article.post_date is None:
                                <small>--/--/--</small>
                                % else:
                                <small>{{article.post_date}}</small>
                                % end
                                % for blog_comment in article.comments:
                                    <div class="comment"><span>{{blog_comment.created_at}} : {{blog_comment.comment}}</span></div>
                                % end
                                <form id="form" action="/blog/{{blog_url}}/add_comment" method="post">
                                <input type="hidden" name="article_id" id="article_id" value="{{article.id}}">
                                <div class="comment">
                                    <input type="text" name="contributor" id="contributor" class="form-control" placeholder="投稿者">
                                    <textarea name="comment" id="comment" class="form-control" placeholder="コメント" rows="5"></textarea>
                                    <input type="submit" class="btn-primary" value="コメントする">
                                </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="bs-component">
                    <div class="panel panel-default">
                        <div class="panel-heading">サブコンテンツのヘッダー</div>
                        <div class="panel-body subcontent">
                            サブコンテンツの内容
                        </div>
                    </div>
                    <div class="panel panel-default">
                        <div class="panel-heading">サブコンテンツのヘッダー</div>
                        <div class="panel-body subcontent">
                            サブコンテンツの内容
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <footer>
            <div class="container footer">
            </div>
        </footer>
    </body>
</html>
