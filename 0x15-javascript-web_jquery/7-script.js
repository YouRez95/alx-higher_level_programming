/* global $ */

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: (response) => {
    if ('name' in response) {
      $('#character').text(response.name);
    }
  }
});
