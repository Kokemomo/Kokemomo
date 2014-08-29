<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>KOKEMOMO CMS ADMIN</title>
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

        <script src='{{url("static_js", filename="communication.js")}}'></script>
        <script src='{{url("static_js", filename="admin.js")}}'></script>
        <link href='{{url("static_css", filename="custom.css")}}' rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-inverse" role="navigation">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">KOKEMOMO</a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-9">
                <ul class="nav navbar-nav">
                <li class="active"><a href="/engine/admin">Admin</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">管理メニュー<b class="caret"></b></a>
                    <ul class="dropdown-menu">
                      <li><a href="/engine/user">ユーザー</a></li>
                      <li><a href="/engine/parameter">パラメータ</a></li>
                      <li><a href="/engine/file">ファイル</a></li>
                      <li><a href="/engine/plugin">プラグイン</a></li>
                      <li><a href="/engine/log">ログ</a></li>
                    </ul>
                </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>

        <section class="container">
            <h3>ユーザー管理</h3>
            <div class="row">
                <div class="col-sm-12">
                    <p>ユーザー情報</p>
                    <input type="button" value="検索" id="km_user_search"/>
                    <input type="button" value="更新" id="km_user_save"/>
                    <input type="button" value="行追加" id="km_user_add_row"/>
                    <table class="table" id="km_user_list">
                        <thead>
                            <tr>
                                <td style="width:5%;">削除</td>
                                <td style="width:10%;">ID</td>
                                <td>PASSWORD</td>
                            </tr>
                        </thead>
                    </table>
                </div>
            </div>
        </section>
    </body>
</html>
