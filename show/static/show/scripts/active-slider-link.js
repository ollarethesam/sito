$(document).ready(function() {
    // Select all anchor links with href starting with #
    $('a[href^="#slide"]').on('click', function(e) {
        $('a[href^="#slide"]').not($(this)).removeClass('active');
        $(this).addClass('active')
    });
  });