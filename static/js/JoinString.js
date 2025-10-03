$(function() {
    $('input[class="checkboxUpdate"]').on('click', function() {
        var values = [];
        $('input:checked').each(function() {
            values.push($(this).val());
        });
        $('[class="hiddenUpdate"]').attr({value: values.join(', ')});
    });
});