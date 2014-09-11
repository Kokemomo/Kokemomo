$(document).ready(function(){

	$("#save").click(function(){
        json = JSON.stringify(getFormData());
	    send(SendType[2], '/common_entry/save', encodeURIComponent(json), save, null);
	});


});

function save(status, json){

}

function getFormData(){
    var list = $("#input_form :input");
    var formData = {};
    for(var index=0;index<list.length;index++){
        var input = list[index];
        formData[input.id] = input.value;
    }
    return formData;
}