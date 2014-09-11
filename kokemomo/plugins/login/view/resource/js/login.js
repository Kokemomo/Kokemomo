var user_id = "";
$(document).ready(function(){

	$("#login").click(function(){
	    user_id = $('#user_id').val();
	    var loginInfo = user_id + ":" + $('#password').val();
	    send(SendType[2], '/login/auth', loginInfo , login);
	});

});

function login(status, json){
    if(status == 200){
        console.log("logine success!" + json);
        switch(json){
            case 'SUCCESS':
                location.href = "/engine";
                document.cookie = "user_id=" + user_id;
                break;
            case 'FAIL':
                $("#error_label").removeClass('hidden');
                $("#error_label").text('ユーザーIDまたはパスワードが違います。');
                $("#input_form").addClass('has-error');
                break;
        }
    }
}