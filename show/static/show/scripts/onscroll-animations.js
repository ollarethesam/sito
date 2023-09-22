$(document).ready(function() {
    $('.section1').waypoint(function(){
        const cc = $('.section1').children('.text-block').children()
        cc.each(function(index) {
            const child = $(this);
            setTimeout(function() {
                child.addClass('animate');
            }, index * 700);
        });
    }, {offset: "100%"})
    $('.section2').waypoint(function(){
        $('.section2').children().addClass('animate')
    }, {offset: "80%"})

    $('.partners').waypoint(function(){
        const cc = $('.partners').children();
        cc.each(function(index) {
            const child = $(this);
            setTimeout(function() {
                child.addClass('popup');
            }, index * 300);
        });
    }, {offset: "100%"})
});
