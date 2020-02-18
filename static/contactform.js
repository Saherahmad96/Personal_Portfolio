$(document).ready(function() {
    $("#my-form").validate({
      rules: {
        name : {
          required: true,
          minlength: 3
        },
        email: {
            required: true,
            email: true
        },
        phone: {
          required: true,
          phone: true,
          minlength: 10

        },
      }
    });
  });