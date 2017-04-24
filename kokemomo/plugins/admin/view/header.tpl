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
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
        <link href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/united/bootstrap.min.css" rel="stylesheet" integrity="sha384-pVJelSCJ58Og1XDc2E95RVYHZDPb9AVyXsI8NoVpB2xmtxoZKJePbMfE4mlXw7BJ" crossorigin="anonymous">

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
        <script src='{{url("engine_static_js", "communication.js")}}'></script>
        <script src='{{url("engine_static_js", "info.js")}}'></script>
        <script src='{{url("admin_static_js", "admin.js")}}'></script>
        <link href='{{url("admin_static_css", "admin.css")}}' rel="stylesheet">
        <link href='{{url("engine_static_css", "info.css")}}' rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-default" role="navigation">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">KOKEMOMO</a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-9">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="/admin/top">Top</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">管理メニュー<b class="caret"></b></a>
                        <ul class="dropdown-menu">
                        % for menu in menu_list:
                            <li><a href="{{menu.url}}">{{menu.name}}</a></li>
                        % end
                        </ul>
                    </li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">{{user_id}}さん</a></li>
                    <li><a href="/admin/logout">Logout</a></li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>
        % include kokemomo/plugins/engine/view/info url=result['url']
    </body>
</html>
