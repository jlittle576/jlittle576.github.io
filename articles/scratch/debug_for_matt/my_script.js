$(function () {
    $(document).tooltip({
        content: function () {
            return $(this).prop('title');
        },
        show: null, 
        close: function (event, ui) {
            ui.tooltip.hover(

            function () {
                $(this).stop(true).fadeTo(400, 1);
            },

            function () {
                $(this).fadeOut("400", function () {
                    $(this).remove();
                })
            });
        }
    });
});