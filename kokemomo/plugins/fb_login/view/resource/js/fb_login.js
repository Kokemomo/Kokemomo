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
        if(json == 'SUCCESS'){
            location.href = "/engine";
            document.cookie = "user_id=" + user_id;
            console.log(document.cookie);
        }
    }
}

function facebooklogin(){
    location.href = "/fb_login_auth";
//    send(SendType[1], '/fb_login_auth', null , facebook_login);
}

function facebook_login(){

}

//function checkLoginState() {
//    FB.getLoginStatus(function(response) {
//        statusChangeCallback(response);
//    });
//}

// facebook login settings.
//window.fbAsyncInit = function() {
//    FB.init({
//    appId      : '{app-id}',
//    cookie     : true,  // enable cookies to allow the server to access
//                        // the session
//    xfbml      : true,  // parse social plugins on this page
//    version    : 'v2.1' // use version 2.1
//    });
//};

//(function(d, s, id) {
//    var js, fjs = d.getElementsByTagName(s)[0];
//    if (d.getElementById(id)) return;
//    js = d.createElement(s); js.id = id;
//    js.src = "//connect.facebook.net/en_US/sdk.js";
//    fjs.parentNode.insertBefore(js, fjs);
//}(document, 'script', 'facebook-jssdk'));

//function statusChangeCallback(response){
//    send(SendType[1], '/fb_login_auth', response.status , facebook_login);
//}

//function facebook_login(status, json){
//    if(status==200){
//        console.log(json);
//    }
//}