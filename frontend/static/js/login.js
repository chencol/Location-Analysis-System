$(function () {
    // $("body").show();
    $("#login_btn").bind("click", function (event) {
        event.preventDefault();
        $.ajax({
            url: env.base_api_url + "verify_user",
            xhrFields: {
                withCredentials: true
            },
            method: "POST",
            data: {
                name: $('input[id="username"]').val(),
                password: $('input[id="password"]').val()
            },
            success: function (data) {
                if (data.status != "Successful") {
                    $("#login_error").css("color", "red");
                    $("#login_error").css("opacity", "1");
                    $("#login_error").text("Wrong username or password!");
                } else {
                    username = data.username;
                    $("#login_error").css("color", "black");
                    $("#login_error").css("opacity", "1");
                    $("#login_error").text(
                        "Welcome home! Dear " + username + "! We are now bring u home!"
                    );
                    localStorage.setItem("access_token", data.token);
                    localStorage.setItem("username", data.username);
                    localStorage.setItem("role", data.role);
                    localStorage.setItem("uid", data.id);


//              sessionStorage.setItem("access_token", data.token);
//              sessionStorage.setItem("username", data.username);
                    destination = localStorage.getItem("destination");
                    setTimeout(function () {
                        if (destination != null) {
                            destination = destination.substring(1);
                            window.location.href = env.base_url + destination;
                        } else {
                            window.location.href = env.base_url + "home.html";
                        }
                    }, 2000);
                }
            },
            error: function () {
                alert(msg.backend_error_msg);
            }
        });
    })
})



