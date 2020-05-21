$(function() {
  $("#login_btn").bind("click", function() {
    name = $("#username").val();
    $.getJSON(
//      "http://127.0.0.1:5000/verify_user",
      env.base_url + "verify_user",
      {
        name: $('input[id="username"]').val(),
        password: $('input[id="password"]').val()
      },
      function(data) {
        if (data.result != "true") {
          $("#login_error").css("color", "red");
          $("#login_error").css("opacity", "1");
          $("#login_error").text("Wrong username or password!");
        } else {
          username = data.username;
          $("#login_error").css("color", "black");
          $("#login_error").css("opacity", "1");
          $("#login_error").text(
            "Welcome home " + username + "! We are now bring u home!"
          );
          sessionStorage.setItem("access_token", data.token);
          sessionStorage.setItem("username", data.username);
          setTimeout(function() {
            window.location.href = "http://localhost/home.html";
          }, 2000);
        }
      }
    );
    return false;
  });
});
