$(document).ready(function () {
  token = localStorage.getItem("access_token");
  $("body").hide();
  // $("body").mouseenter(function () {
  //     if (token != null) {
  //         $.ajax({
  //             url: env.base_api_url + "access_control",
  //             xhrFields: {
  //                 withCredentials: true
  //             },
  //             method: "GET",
  //             data: {
  //                 token: token
  //             },
  //             success: function (data) {
  //                 pathname = window.location.pathname
  //                 if (data.status == "Successful") {
  //                     if (pathname != "/login.html") {
  //                         $("body").show();
  //                     } else {
  //                         window.location.href = env.base_url + "home.html";
  //                     }
  //                 } else {
  //                     if (pathname != "/login.html") {
  //                         window.location.href = env.base_url + "login.html";
  //                     } else {
  //                         $("body").show();
  //                     }
  //                 }
  //             },
  //             error: function () {
  //                 alert(msg.backend_error_msg);
  //             }
  //         })
  //     } else {
  //         window.location.href = env.base_url + "login.html"
  //     }
  // });
  pathname = window.location.pathname;
  if (pathname != "/login.html") {
    localStorage.setItem("destination", pathname);
  }

  if (token != null) {
    $.ajax({
      url: env.base_api_url + "access_control",
      xhrFields: {
        withCredentials: true,
      },
      method: "GET",
      data: {
        token: token,
      },
      success: function (data) {
        if (data.status == "Successful") {
          if (pathname != "/login.html") {
            $("body").show();
          } else {
            window.location.href = env.base_url + "home.html";
          }
        } else {
          if (pathname != "/login.html") {
            window.location.href = env.base_url + "login.html";
          } else {
            $("body").show();
          }
        }
      },
      error: function () {
        alert(msg.backend_error_msg);
      },
    });
  } else {
    if (pathname != "/login.html") {
      window.location.href = env.base_url + "login.html";
    } else {
      $("body").show();
    }
  }
});
