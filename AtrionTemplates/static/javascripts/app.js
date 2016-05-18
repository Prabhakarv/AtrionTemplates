(function () {
    $('#datetimepicker1').datetimepicker();
})();

$(".dropdown-menu li").click(function () {
    $(this).parents(".btn-group").find('.btn').html(
    $(this).text() + " <span class=\"caret\"></span>"
    );
});
