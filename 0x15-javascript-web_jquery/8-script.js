#!/usr/bin/nodejs
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movieList = $('#list_movies');

    data.results.forEach(function (movie) {
      const movieTitle = $('<li>').text(movie.title);
      movieList.append(movieTitle);
    });
  });
});
