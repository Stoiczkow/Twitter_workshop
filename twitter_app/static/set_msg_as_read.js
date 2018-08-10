$(document).ready(function(){
    var messages = $( ".list-group-item.active" );
    var unread_count = $("#unread_msgs")
        messages.each(function(){
            $( this ).click(function() {
                $.get('/change_msg/', {id: $(this).attr("value")});
                unread_count.text(unread_count.text() - 1);
                $(this).toggleClass('active');
            });
        });
     });





