$(document).ready(function() {
    $('.validate_button').click(function() {
        var decklist;
        decklist = $('#deck_box').val();
        $.get('/brawl/validate_decklist/',
            {'deck': decklist},
            function(data) {
                $('.errors').text(data);
            }
        )
    })
})