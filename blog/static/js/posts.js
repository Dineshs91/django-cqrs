$(function() {
    // Initialize modal
    $('#modal1').modal();

    $('form').submit(function(e) {
        e.preventDefault();

        var action = $(this).attr('action');
        var data = $(this).serialize();
        $.post(action, data, function(data) {
            // Replace the entire content
            document.open();
            document.write(data);
            document.close();
        });
    });
});
