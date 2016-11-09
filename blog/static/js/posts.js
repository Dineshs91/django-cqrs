$(function() {
    // Initialize modal
    $('#modal1').modal();

    $('.create_post').submit(function(e) {
        e.preventDefault();

        var action = $(this).attr('action');
        var data = $(this).serialize();
        $.post(action, data, function(res) {
            // Replace the entire content
            document.open();
            document.write(res);
            document.close();
        });
    });

    var post_id;
    $('.secondary-content').click(function(e) {
        post_id = $(this).attr('data');

        $('#post_id').val(post_id);
    });

    $('.update_post').submit(function(e) {
        e.preventDefault();

        var action = $(this).attr('action') + post_id + '/';
        var data = $(this).serialize();
        $.ajax({url: action, type: 'POST', data: data, success: function(res) {
            // Iterate through the entire list and find the element
            // Whose element's data matches with the data value.
            $('.collection-item').each(function() {
                var data = $(this).find('a').attr('data');
                if (data === post_id) {
                    // Replace the content of this list.
                    $(this).html(res);
                    return;
                }
            });
        }});
    });
});
