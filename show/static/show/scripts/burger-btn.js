$( document ).ready(function(){
    $('.burger-btn').on('click', function() {
        $('.link-container').toggleClass('open')
        $(this).toggleClass('open')
    });
});