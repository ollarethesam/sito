$( document ).ready(function(){
  const navbar = $('nav')
  let prevScrollPos = $(window).scrollTop()
  $(window).scroll(function() {
    const currentScrollPos = $(window).scrollTop()

    if (prevScrollPos > currentScrollPos) {
      navbar.removeClass('scrolling-down')
    } else {
      $('.link-container').removeClass('open')
      $('.burger-btn').removeClass('open')
      navbar.addClass('scrolling-down')
    }
    prevScrollPos = currentScrollPos
  });
});