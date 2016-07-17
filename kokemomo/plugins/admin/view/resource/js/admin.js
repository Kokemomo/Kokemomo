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
	    send(SendType[2], '/admin/file/change_dir', $("#dirList").val(), changeDir);
	});

});

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
                    url: '/admin/file/upload',
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
    	request.open( 'POST', '/admin/file/remove');
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