// adds the class red to <header> on DIV#red_header click
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
