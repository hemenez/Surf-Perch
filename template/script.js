let submit = document.getElementById("submit");
let search = document.getElementById("search");
submit.addEventListener("click", function(event) {
  console.log(search.value);
  event.preventDefault();
});

$('#twitter-connect').click(function() {
  console.log('')
});
