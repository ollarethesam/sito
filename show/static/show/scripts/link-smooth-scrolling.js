$(document).ready(function() {
    // Select all anchor links with href starting with #
    $('a[href^="#"]').on('click', function(e) {
  
      var targetId = $(this).attr('href').substring(1);
      var targetElement = $('#' + targetId);
  
      if (targetElement.length) {
        $('html, body').animate({
          scrollTop: targetElement.offset().top - ($(window).height() - targetElement.outerHeight(true)) / 2
        }, 1000); // Adjust the duration as needed
      }
    });
  });