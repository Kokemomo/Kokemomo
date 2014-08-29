var SendType = {
    1:"GET",
    2:"POST"
}
// To communicate by using the Ajax under the specified conditions.
// type : Send type.
// url  : Target url.
// value : Send value.
// callbackFunc : Function to be called at the end of communication.
//                Args is Status and JSON Data ans Option.
//
// Example
// function success(status, json, option){
//    if(status == 200){
//        console.log("success! result=" + json['result']);
//    }
// }
//
// send(SendType[2], '/target/action', "hoge", success);
//
function send(type, url, value, callbackFunc, option){
    var request = new XMLHttpRequest();
    if(type == SendType[1]){
        url = url + "?user_id=" + getUserId() + "&value=" + value;
    }
    console.log(url);
    request.open(type, url);
//    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.send(value);
    request.onreadystatechange = function() {
        switch(request.readyState){
            case 4: // complete
                var result = "";
                if(request.responseText != ""){
                    console.log("res:" + request.responseText);
                    try{
                        result = JSON.parse(request.responseText);
                    }catch(e){
                        result = request.responseText;
                    }
                }
                callbackFunc(request.status, result, option);
                break;
        }
    }
}

// Get userid from cookie.
// key is 'user_id'.
function getUserId(){
    var result = '';
    var cookieStr = document.cookie;
    console.log(cookieStr);
    if(cookieStr != ''){
        var cookies = cookieStr.split(";");
        for(var i=0; i<cookies.length; i++){
            var cookie = cookies[i].replace(/\s+/g, "").split('=');
            if(cookie[0]=='user_id'){
                result = cookie[1];
            }
        }
    }
    return result;
}