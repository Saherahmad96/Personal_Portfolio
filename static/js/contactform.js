$(document).ready(function() {
  
  $("#submit").click(function(){
    var name = $("#name").val();
    var email = $("#email").val();
    var phone = $("#phone").val();
    var place = $("#place").val();
    var where = $("#description").val();
  
  var cfdata = {'name':name, 'email':email, 'phone':phone, 'place':place, 'description':where};

  var baseURL = window.location.origin;           
  var Post_URL = baseURL + '/handleContactForm';
  
  $.ajax({
    method: 'POST',
    url: Post_URL,
    data: JSON.stringify(cfdata),
    contentType: "application/json",
    dataType: 'json',
    success: function(msg) {
      console.log(msg)

      if (msg === 'Failed') {
        alert ('Failed to insert data!');

      } else if (msg === "Successful") {
         alert('Submitted!');
      }
    }, 
    error: function(error) {
        console.log(error);
        alert('Failed to reach backend!');
      }
    });
  });

var baseURL = window.location.origin;
var mainURL = baseURL + '/contactform';
  
  $.ajax({
    method: 'GET',
    url: mainURL,
    success: function(serverData) {
      console.log(serverData);
    },
    error: function(error) {
      console.log(error);
    }
  });