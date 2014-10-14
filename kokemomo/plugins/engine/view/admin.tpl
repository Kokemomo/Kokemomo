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
        <link href='{{url("static_css", filename="admin.css")}}' rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-inverse" role="navigation">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">KOKEMOMO</a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-9">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="/engine">Admin</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">管理メニュー<b class="caret"></b></a>
                        <ul class="dropdown-menu">
                          <li><a href="/engine?type=user">ユーザー</a></li>
                          <li><a href="/engine?type=group">グループ</a></li>
                          <li><a href="/engine?type=role">ロール</a></li>
                          <li><a href="/engine?type=parameter">パラメータ</a></li>
                          <li><a href="/engine?type=file">ファイル</a></li>
                          <li><a href="/engine?type=plugin">プラグイン</a></li>
                          <li><a href="/engine?type=log">ログ</a></li>
                        </ul>
                    </li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">{{user_id}}さん</a></li>
                    <li><a href="/logout">Logout</a></li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>

        % if type == 'info':
            % include kokemomo/plugins/engine/view/info
        % elif type == 'user':
            % include kokemomo/plugins/engine/view/user
        % elif type == 'group':
            % include kokemomo/plugins/engine/view/group
        % elif type == 'role':
            % include kokemomo/plugins/engine/view/role
        % elif type == 'parameter':
            % include kokemomo/plugins/engine/view/parameter
        % elif type == 'file':
            % include kokemomo/plugins/engine/view/file dirs=dirs, files=files
        % elif type == 'plugin':
            % include kokemomo/plugins/engine/view/plugin
        % elif type == 'log':
            % include kokemomo/plugins/engine/view/log
        % end
    </body>
</html>
