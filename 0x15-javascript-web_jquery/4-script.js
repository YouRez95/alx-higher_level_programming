/* global $ */

$('div#toggle_header').click(() => {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else {
    $('header').addClass('green');
  }
});
