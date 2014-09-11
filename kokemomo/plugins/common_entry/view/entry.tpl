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
        <script src='{{url("common_entry_static_js", filename="entry.js")}}'></script>
        <link href='{{url("common_entry_static_css", filename="entry.css")}}' rel="stylesheet">
    </head>
    <body>
        <section class="container">
            <div class="col-sm-12">
                <div class="jumbotron">
                    <h2>{{title}}</h2>
                    <div class="form-group" id="input_form">
                        <label class="control-label hidden" for="user_id" id="error_label">Input with error</label>
                        %for column in columns:
                        <input type="text" class="form-control" placeholder="{{column}}" id="{{column}}"/>
                        %end
                    </div>
                    <input type="button" value="登録" id="save"/>
                </div>
            </div>
        </section>
    </body>
</html>
