$(document).ready(function() {
  $("#register-form").hide();
  $("#login-form").show();
  changeSelection();
  $(".register-button").click(function() {
    $("#login-form").slideUp();
    $("button").removeClass('selected');
    $("#register-form").slideDown();
    $('.register-button').addClass('selected');
    changeSelection();
  });
  $(".login-button").click(function() {
    $("#register-form").slideUp();
    $("button").removeClass('selected');
    $("#login-form").slideDown();
    $('.login-button').addClass('selected');
    changeSelection();
  });
});

function changeSelection() {
  $('button').css('background', '#ccc');
  $('.selected').css('background', '#6dccfd');
}