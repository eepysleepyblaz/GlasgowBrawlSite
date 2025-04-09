$(document).ready(function() {
    $('.validate_button').click(function() {
        var decklist;
        decklist = $('.deck_box').textContent;

        $.get('/brawl/validate_decklist/',
            {'decklist': decklist},
            function(data) {
                $('.errors').text(data);
            }
        )
    })
})