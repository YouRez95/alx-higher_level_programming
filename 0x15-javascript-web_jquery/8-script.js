/* global $ */

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (response) => {
    for (const film of response.results) {
      const text = `<li>${film.title}</li>`;
      $('#list_movies').append(text);
    }
  }
});
