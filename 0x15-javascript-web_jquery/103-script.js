/* global $ */

$('script').attr('defer', 'defer');

function fetchHello () {
  const value = $('#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${value}`;
  $.ajax({
    url,
    success: (response) => {
      $('#hello').text(response.hello);
    }
  });
}

$(document).ready(function () {
  $('INPUT#language_code').keydown((e) => {
    if (e.originalEvent.key === 'Enter') {
      fetchHello();
    }
  });

  $('INPUT#btn_translate').click(() => {
    fetchHello();
  });
});
