function makeReadable(number) {
    var result = '';
    for (var i = 0; i < number.length; i++) {
        if (i >= 1 && (number.length - i) % 3 === 0)
            result += ' ';
        result += number[i];
    }
    return result;
}

$(function () {
    $('.amount-input')
        .keypress(function (event) {
            if (event.which !== 0 && event.which !== 8 &&
                !('0'.charCodeAt(0) <= event.which && event.which <= '9'.charCodeAt(0)))
                event.preventDefault();
        })
        .keyup(function (event) {
            var selStartOffset = $(this).val().length - $(this).prop('selectionStart');
            var selEndOffset = $(this).val().length - $(this).prop('selectionEnd');

            var value = makeReadable($(this).val().replace(/ /g, ''));
            $(this)
                .val(value)
                .prop('selectionStart', value.length - selStartOffset)
                .prop('selectionEnd', value.length - selEndOffset);
        });

    var MAX_STEP = 5;
    var step = 1;

    function validate() {
        if (step === 1) {
            var creditAmountInput = $('#credit_amount');
            var creditAmount = parseInt(creditAmountInput.val().replace(/ /g, ''));
            if (1e5 <= creditAmount && creditAmount <= 5e6)
                creditAmountInput.removeClass('is-invalid');
            else {
                creditAmountInput.addClass('is-invalid');
                return false;
            }
        }
        return true;
    }

    function changeStep(value) {
        if (!validate())
            return;

        $('#step' + step).hide();
        step = value;
        $('#step' + step).show();

        if (step === 1)
            $('#prev-page-btn').hide();
        else
            $('#prev-page-btn').show();
        if (step === MAX_STEP)
            $('#next-page-btn').hide();
        else
            $('#next-page-btn').show();
    }

    $('#prev-page-btn').click(function (event) {
        event.preventDefault();
        changeStep(step - 1);
    });
    $('#next-page-btn').click(function (event) {
        event.preventDefault();
        changeStep(step + 1);
    });

    function changeHandler(list, select) {
        var newRow = list.find('.row:last-child').clone(true);
        list.append(newRow);
        newRow.find('.amount-input').val('0');

        select.off('change');
    }

    $('.extending-list').each(function (_, item) {
        var list = $(item);
        var select = list.find('.row:last-child select');
        select.change(function () {
            return changeHandler(list, $(this));
        });
    });
});
