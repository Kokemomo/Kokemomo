var user_id = "";
$(document).ready(function(){

	$("#login").click(function(){
	    user_id = $('#user_id').val();
	    var loginInfo = user_id + ":" + $('#password').val();
	    send(SendType[2], '/engine/login/auth', loginInfo , login);
	});

	var return_parameter = getParameter("errorcode");
	if (return_parameter == 0) {
	    $("#error_label").removeClass('hidden');
        $("#error_label").text('不正なアクセスです。ログインして下さい。');
    }
});

function login(status, json){
    if(status == 200){
        console.log("logine success!" + json);
        switch(json){
            case 'SUCCESS':
                var location_path = "/engine/top";
                location.href = location_path;
                break;
            case 'FAIL':
                $("#error_label").removeClass('hidden');
                $("#error_label").text('ユーザーIDまたはパスワードが違います。');
                $("#input_form").addClass('has-error');
                break;
        }
    }
}

function getParameter(param_key){
	var ret = null;
	var url = location.href; 
	parameters = url.split("?");

	if( parameters.length > 1 ) {
		var params   = parameters[1].split("&");
		var paramsArray = [];
		for ( i = 0; i < params.length; i++ ) {
		   var param_data = params[i].split("=");
		   paramsArray.push(param_data[0]);
		   paramsArray[param_data[0]] = param_data[1];
		}
		ret = paramsArray[param_key];
	}
    return ret;
};