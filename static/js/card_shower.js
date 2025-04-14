$(document).ready(function() {
    $('.list_card').hover(function(e) {
        var link = $(this).attr('id');
        $('#cursor_image').css('left',e.pageX+"px");
        $('#cursor_image').css('top',e.pageY+"px");
        $('#cursor_image').attr("src", `https://api.scryfall.com/cards/named?exact=${link}&format=image`);
        $('#cursor_image').attr("width", "252");
        $('#cursor_image').attr("height", "352");
    }, function() {

    })

    $('#cursor_image').hover(function() {},
    function() {
        $('#cursor_image').removeAttr("src");
        $('#cursor_image').removeAttr("width");
        $('#cursor_image').removeAttr("height");
    })

    $('#cursor_image').click(function() {
        $('#cursor_image').removeAttr("src");
        $('#cursor_image').removeAttr("width");
        $('#cursor_image').removeAttr("height");
    })
})