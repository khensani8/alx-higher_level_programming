// Adds the class red to the header element when user clicks

$(document).ready(function(){
  $("#red_header").click(function(){
    $("header").addClass("red");
  });
});