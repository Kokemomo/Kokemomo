//
// This is a script that collected the verification function of the input value.
//

// Validates value whether a JSON.
function isJson(target){
    try{
        JSON.parse(target);
    }catch(e){
        return false;
    }
    return true;
}