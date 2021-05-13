// adds <li> element to list on DIV#add_item click
$('DIV#add_item').click(function () {
  $('ul').append('<li>New item</li>');
});
