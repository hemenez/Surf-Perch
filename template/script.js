let submit = document.getElementById("submit");
let search = document.getElementById("search");
submit.addEventListener("click", function(event) {
  $.ajax ({
    method: 'POST',
    url: 'surfperch.holberton.us/save_keyword',
    data: { "keyword": search.value }
  })
  console.log(search.value);
  console.log(search.name);
  event.preventDefault();
});

$('#twitter-connect').click(function() {
  console.log('')
});
//
// $("#submit").click( function() {
//   console.log($('#search').val());
//   let text = $("#search").val();
//   const filename = 'tweet-keyword'
//   let blob = new Blob([text], {type: "text/plain;charset=utf-8"});
//   saveAs(blob, filename+".txt");
// });
