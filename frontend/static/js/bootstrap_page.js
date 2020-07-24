$(function () {
  $("#upload_file_btn").on("click", function (e) {
    //files will store the file data but it will be access as a whole in the backend.
    let files = new FormData(), // you can consider this as 'data bag'
      url = env.base_api_url + "upload_files";
    files.append("file", $("#file")[0].files[0]); // append selected file to the bag named 'file'
    $.ajax({
      type: "post",
      url: url,
      xhrFields: {
        withCredentials: true,
      },
      headers: { token: token },
      processData: false,
      contentType: false,
      data: files,
      success: function (response) {
        if ((response.status = "Successful")) {
          alert("Your data has been imported to database!");
        } else {
          alert("Data import failed!");
        }
      },
      error: function (err) {
        alert("Server error");
      },
    });
  });
});
