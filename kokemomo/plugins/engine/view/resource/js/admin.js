var localPath = "C:\\Users\\shuhei\\PycharmProjects\\CMS"; // set your home directory.
// ex)
// var localPath = "/User/xxx/git/cms/"

var rowCount = 0; // parameter list row count.
var userRowCount = 0; // user list row count.
$(document).ready(function(){

	try{
		window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;
	} catch(e) {
		alert('FileSystem is not supported in this browser');
	}

	// File drop settings.
	var droppable = $("#dropArea");
	droppable.bind("dradenter", cancel);
	droppable.bind("dragover", cancel);
	droppable.bind("drop", handleDroppedFile);

    // Lists the files in a directory.
	$("#dirList").change(function(){
	    send(SendType[2], '/engine/file/change_dir', $("#dirList").val(), changeDir);
	});

    // Save parameter.
    // Format: 'keyName':{"hoge":"fuga"}
    var json = "";
	$("#km_parameter_save").click(function(){
        json = JSON.stringify(createSaveData("km_parameter", rowCount));
	    send(SendType[2], '/engine/parameter/save', encodeURIComponent(json), manualSearch, "km_parameter");
	});

    // Search Parameter
	$("#km_parameter_search").click(function(){
        var option = ["km_parameter", 0, createParameterListRow];
	    send(SendType[1], '/engine/parameter/search', null, search, option);
	});

    // add row
    $("#km_parameter_add_row").click(function(){
        $("#km_parameter_list").append(createParameterListRow(rowCount));
        rowCount++;
	});

	// Save user.
    // Format: 'keyName':{"hoge":"fuga"}
	$("#km_user_save").click(function(){
        json = JSON.stringify(createSaveData("km_user", userRowCount));
	    send(SendType[2], '/engine/user/save', encodeURIComponent(json), manualSearch, "km_user");
	});

    // Search Parameter
	$("#km_user_search").click(function(){
        var option = ["km_user", 0, createUserListRow];
	    send(SendType[1], '/engine/user/search', null, search, option);
	});

    // add row
    $("#km_user_add_row").click(function(){
        $("#km_user_list").append(createUserListRow(userRowCount));
        userRowCount++;
	});


});

function createSaveData(prefix, count){
    var saveData = {};
    for(var i=0; i<count;i++){
        var key = $("#" + prefix + "_key_" + i).val();
        if($("#" + prefix + "_check_" + i + ":checked").val()){
            saveData[key] = "";
        }else{
            saveData[key] = $("#" + prefix + "_json_" + i).val();
        }
    }
    return saveData;
}

function search(status, json, option){
    var count = 0;
    if(status == 200){
        $("#" + option[0] + "_list").children("tbody").remove();
        // view row
        var prefix =option[0];
        count = option[1];
        var func = option[2];
        for(var i in json['result']){
            $("#" + prefix + "_list").append(func(count));
            switch(prefix){
                case "km_parameter":
                    $("#" + prefix + "_key_" + count).val(json['result'][i]['key']);
                    $("#" + prefix + "_json_" + count).val(JSON.stringify(json['result'][i]['json']));
                    count++;
                    rowCount = count;
                    break;
                case "km_user":
                    $("#" + prefix + "_key_" + count).val(json['result'][i]['id']);
                    $("#" + prefix + "_json_" + count).val(json['result'][i]['password']);
                    count++;
                    userRowCount = count;
                    break;
            }
            count++;
        }
    }
}

function manualSearch(status, json, prefix){
    if(status == 200){
        $("#" + prefix + "_search").click();
    }
}

function changeDir(status, json, prefix){
    if(status == 200){
        var options = json['result'].split(',');
        $('#fileList').children().remove();
        $('#fileList').append('<li class="nav-header">files</li>');
        var dirPath = $("#dirList").val();
        for(var option in options) {
            $('#fileList').append('<li><input type="button" value="del" id="del_'+ option +'" class="delete_button" onclick="removeFile(\''+ dirPath +'\', \''+ options[option] +'\')"/>' + options[option] + '</li>');
        }
    }
}

function convertJSON(text){
	var startIndex = text.indexOf("json");
	var endIndex = text.lastIndexOf("'}");
	var value = text.substring(startIndex + 6,endIndex);
	var jsonValue = JSON.parse(value);
	return jsonValue;
}

function createParameterListRow(id){
    return "<tr><td><input type='checkbox' id='km_parameter_check_" + id + "'></td><td><input type='text' id='km_parameter_key_" + id + "'></td><td><input type='text' id='km_parameter_json_" + id + "' style='width:100%;'></td></tr>";
}

function createUserListRow(id){
    return "<tr><td><input type='checkbox' id='km_user_check_" + id + "'></td><td><input type='text' id='km_user_key_" + id + "'></td><td><input type='text' id='km_user_json_" + id + "' style='width:100%;'></td></tr>";
}

// File Drop Event.
function handleDroppedFile(event){
	cancel(event);
	var files = event.originalEvent.dataTransfer.files;
	var path = $("#dirList").val();
	for(var file in files){
        if (files[file].type == 'image/jpeg' || files[file].type == 'image/png') {
            var formData = new FormData();
            formData.append('files', files[file]);
            formData.append('directory', path);
            $.ajax({
                    url: '/engine/file/upload',
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false
                });
        }
    }
	return false;
}

// Drop in the file, I do not want to appear in the browser.
function cancel(event) {
	event.preventDefault();
	event.stopPropagation();
	return false;
}

function removeFile(dirPath, file){
        var request = new XMLHttpRequest();
    	request.open( 'POST', '/engine/file/remove');
    	request.send(dirPath + "," + file);
    	request.onreadystatechange = function() {
            if (request.readyState == 4) {
            }
        }

}

// Local file write.
// Current can not use.
function writeFile(file){
	window.requestFileSystem(window.TEMPORARY, 1024*1024,  function(fs) {
		fs.root.getFile(localPath, {create: true, exclusive: false}, function(fileEntry) {
			fileEntry.file(function(file) {
				recordFile = file;
			}, errorHandler);
			fileEntry.createWriter(function(fileWriter) {
				fileWriter.onwriteend = function(e) { console.log('Write completed.'); };
				fileWriter.onerror = function(e) { console.log('Write failed: ' + e.toString()); };
				writer = fileWriter;
			}, errorHandler);
		}, errorHandler);
	}, errorHandler);
}

// Error handling for local file write.
function errorHandler(e) {
  var msg = '';

  switch (e.code) {
    case FileError.QUOTA_EXCEEDED_ERR:
      msg = 'QUOTA_EXCEEDED_ERR';
      break;
    case FileError.NOT_FOUND_ERR:
      msg = 'NOT_FOUND_ERR';
      break;
    case FileError.SECURITY_ERR:
      msg = 'SECURITY_ERR';
      break;
    case FileError.INVALID_MODIFICATION_ERR:
      msg = 'INVALID_MODIFICATION_ERR';
      break;
    case FileError.INVALID_STATE_ERR:
      msg = 'INVALID_STATE_ERR';
      break;
    default:
      msg = 'Unknown Error';
      break;
  };

  console.log('Error: ' + msg);
}