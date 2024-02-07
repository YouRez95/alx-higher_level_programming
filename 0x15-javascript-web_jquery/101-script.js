/* global $ */

$('script').attr('defer', 'defer');

$(document).ready(function () {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(() => {
    if ($('.my_list')[0].lastElementChild !== null) {
      $('.my_list')[0].lastElementChild.remove();
    }
  });

  $('#clear_list').click(() => {
    while ($('.my_list')[0].children.length > 0) {
      $('.my_list')[0].lastElementChild.remove();
    }
  });
});
