var km_process = false;
$(document).ready(function(){
    // progress
    $('.km_progress').hide();
    $('.km_progress_button').click(function(){
        if(km_process){
            $('.km_progress').hide();
            km_process = false;
        }else{
            $('.km_progress').show();
            km_process = true;
        }
    });
    // dialog
    var km_form = $('.km_form');
    km_form.submit(function(e){
        $('#km_dialog_block').modal('show');
        $('#km_dialog_ok').click(function(){
            $('#km_dialog_block').modal('hide');
            km_form.off( 'submit' );
            km_form.submit();
        });
        return false;
    });
});