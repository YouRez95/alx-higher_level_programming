/* global $ */

$('script').attr('defer', 'defer');

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const value = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${value}`;
    $.ajax({
      url,
      success: (response) => {
        $('#hello').text(response.hello);
      }
    });
  });
});
