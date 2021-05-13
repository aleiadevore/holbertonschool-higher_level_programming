// fetches the character title of all movies from
// https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (key, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
