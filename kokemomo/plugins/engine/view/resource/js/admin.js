var localPath = "C:\\Users\\shuhei\\PycharmProjects\\CMS"; // set your home directory.
// ex)
// var localPath = "/User/xxx/git/cms/"

var parameterRowCount = 0; // parameter list row count.
var userRowCount = 0; // user list row count.
var groupRowCount = 0; // group list row count.
var roleRowCount = 0; // role list row count.
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

    // -- File --
    // Lists the files in a directory.
	$("#dirList").change(function(){
	    send(SendType[2], '/engine/file/change_dir', $("#dirList").val(), changeDir);
	});

	// -- User --
	$("#km_user_save").click(function(){
        json = JSON.stringify(createSaveData("km_user", userRowCount));
	    send(SendType[2], '/engine/user/save', encodeURIComponent(json), manualSearch, "km_user");
	});
	$("#km_user_search").click(function(){
        var option = ["km_user", 0, createUserListRow];
	    send(SendType[1], '/engine/user/search', null, search, option);
	});
    $("#km_user_add_row").click(function(){
        $("#km_user_list").append(createUserListRow(userRowCount));
        userRowCount++;
	});

	// -- Group --
	$("#km_group_save").click(function(){
        json = JSON.stringify(createSaveData("km_group", groupRowCount));
	    send(SendType[2], '/engine/group/save', encodeURIComponent(json), manualSearch, "km_group");
	});
	$("#km_group_search").click(function(){
        var option = ["km_group", 0, createGroupListRow];
	    send(SendType[1], '/engine/group/search', null, search, option);
	});
    $("#km_group_add_row").click(function(){
        $("#km_group_list").append(createGroupListRow(groupRowCount));
        groupRowCount++;
	});

	// -- Role --
	$("#km_role_save").click(function(){
        json = JSON.stringify(createSaveData("km_role", roleRowCount));
	    send(SendType[2], '/engine/role/save', encodeURIComponent(json), manualSearch, "km_role");
	});
	$("#km_role_search").click(function(){
        var option = ["km_role", 0, createRoleListRow];
	    send(SendType[1], '/engine/role/search', null, search, option);
	});
    $("#km_role_add_row").click(function(){
        $("#km_role_list").append(createRoleListRow(roleRowCount));
        roleRowCount++;
	});

    // -- Parameter --
    var json = "";
	$("#km_parameter_save").click(function(){
        // Format: 'keyName':{"hoge":"fuga"}
        json = JSON.stringify(createSaveData("km_parameter", parameterRowCount));
	    send(SendType[2], '/engine/parameter/save', encodeURIComponent(json), manualSearch, "km_parameter");
	});
	$("#km_parameter_search").click(function(){
        var option = ["km_parameter", 0, createParameterListRow];
	    send(SendType[1], '/engine/parameter/search', null, search, option);
	});
    $("#km_parameter_add_row").click(function(){
        $("#km_parameter_list").append(createParameterListRow(parameterRowCount));
        parameterRowCount++;
	});

});

function createSaveData(prefix, count){
    var saveData = {};
    for(var i=0; i<count;i++){
        switch(prefix){
            case "km_user":
                var key = $("#" + prefix + "_id_" + i).val();
                if($("#" + prefix + "_check_" + i + ":checked").val()){
                    saveData[key] = "";
                }else{
                    var user = {};
                    user["id"] = key;
                    user["name"] = $("#" + prefix + "_name_" + i).val();
                    user["password"] = $("#" + prefix + "_password_" + i).val();
                    user["mail_address"] =$("#" + prefix + "_mail_address_" + i).val();
                    user["group_id"] =$("#" + prefix + "_group_id_" + i).val();
                    user["role_id"] =$("#" + prefix + "_role_id_" + i).val();
                    saveData[key] = user;
                }
                break;
            case "km_group":
                var key = $("#" + prefix + "_id_" + i).val();
                if($("#" + prefix + "_check_" + i + ":checked").val()){
                    saveData[key] = "";
                }else{
                    var group = {};
                    group["id"] = $("#" + prefix + "_id_" + i).val();
                    group["name"] = $("#" + prefix + "_name_" + i).val();
                    group["parent_id"] = $("#" + prefix + "_parent_id_" + i).val();
                    saveData[key] = group;
                }
                break;
            case "km_role":
                var key = $("#" + prefix + "_id_" + i).val();
                if($("#" + prefix + "_check_" + i + ":checked").val()){
                    saveData[key] = "";
                }else{
                    var role = {};
                    role["id"] = $("#" + prefix + "_id_" + i).val();
                    role["name"] = $("#" + prefix + "_name_" + i).val();
                    role["target"] = $("#" + prefix + "_target_" + i).val();
                    role["is_allow"] = $("#" + prefix + "_is_allow_" + i).val();
                    saveData[key] = role;
                }
                break;
            case "km_parameter":
                var key = $("#" + prefix + "_key_" + i).val();
                if($("#" + prefix + "_check_" + i + ":checked").val()){
                    saveData[key] = "";
                }else{
                    saveData[key] = $("#" + prefix + "_json_" + i).val();
                }
                break;
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
                case "km_user":
                    $("#" + prefix + "_id_" + count).val(json['result'][i]['id']);
                    $("#" + prefix + "_name_" + count).val(json['result'][i]['name']);
                    $("#" + prefix + "_password_" + count).val(json['result'][i]['password']);
                    $("#" + prefix + "_mail_address_" + count).val(json['result'][i]['mail_address']);
                    $("#" + prefix + "_group_id_" + count).val(json['result'][i]['group_id']);
                    $("#" + prefix + "_role_id_" + count).val(json['result'][i]['role_id']);
                    count++;
                    userRowCount = count;
                    break;
                case "km_group":
                    $("#" + prefix + "_id_" + count).val(json['result'][i]['id']);
                    $("#" + prefix + "_name_" + count).val(json['result'][i]['name']);
                    $("#" + prefix + "_parent_id_" + count).val(json['result'][i]['parent_id']);
                    count++;
                    groupRowCount = count;
                    break;
                case "km_role":
                    $("#" + prefix + "_id_" + count).val(json['result'][i]['id']);
                    $("#" + prefix + "_name_" + count).val(json['result'][i]['name']);
                    $("#" + prefix + "_target_" + count).val(json['result'][i]['target']);
                    $("#" + prefix + "_is_allow_" + count).val(json['result'][i]['is_allow']);
                    count++;
                    roleRowCount = count;
                    break;
                case "km_parameter":
                    $("#" + prefix + "_key_" + count).val(json['result'][i]['key']);
                    $("#" + prefix + "_json_" + count).val(JSON.stringify(json['result'][i]['json']));
                    count++;
                    parameterRowCount = count;
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

function createUserListRow(id){
    var row = "<tr><td><input type='checkbox' id='km_user_check_" + id + "'></td>" +
            "<td><input type='text' id='km_user_id_" + id + "'></td>" +
            "<td><input type='text' id='km_user_name_" + id + "'></td>" +
            "<td><input type='text' id='km_user_password_" + id + "'></td>" +
            "<td><input type='text' id='km_user_mail_address_" + id + "'></td>" +
            "<td><input type='text' id='km_user_group_id_" + id + "'></td>" +
            "<td><input type='text' id='km_user_role_id_" + id + "'></td>" +
            "</tr>";
    return row;
}

function createGroupListRow(id){
    var row = "<tr><td><input type='checkbox' id='km_group_check_" + id + "'></td>" +
            "<td><input type='text' id='km_group_id_" + id + "'></td>" +
            "<td><input type='text' id='km_group_name_" + id + "'></td>" +
            "<td><input type='text' id='km_group_parent_id_" + id + "'></td>" +
            "</tr>";
    return row;
}

function createRoleListRow(id){
    var row = "<tr><td><input type='checkbox' id='km_role_check_" + id + "'></td>" +
            "<td><input type='text' id='km_role_id_" + id + "'></td>" +
            "<td><input type='text' id='km_role_name_" + id + "'></td>" +
            "<td><input type='text' id='km_role_target_" + id + "'></td>" +
            "<td><input type='text' id='km_role_is_allow_" + id + "'></td>" +
            "</tr>";
    return row;
}

function createParameterListRow(id){
    var row = "<tr><td><input type='checkbox' id='km_parameter_check_" + id + "'></td>" +
            "<td><input type='text' id='km_parameter_key_" + id + "'></td>" +
            "<td><input type='text' id='km_parameter_json_" + id + "' style='width:100%;'></td></tr>";
    return row;
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