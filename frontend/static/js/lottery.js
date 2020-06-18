$(function () {
    retrieve_products();

    $(document).on('click', '.buy', function () {
        var uid = localStorage.getItem("uid")
        var pid = $(this).attr("data-pid")
        /////////////////////////////
        var docHeight = $(document).height(); //grab the height of the page
        var scrollTop = $(window).scrollTop(); //grab the px value from the top of the page to where you’re scrolling
        $(".overlay-bg").show().css({
            "height":
            docHeight
        });
        $('body').css({'overflow': 'hidden'}); //this will prevent the entire page to scroll

        //display your popup background and set height to the page height
        // $(".popup" + whichpopup).show().css({
        //     "top": scrollTop + 20 + "px"
        // })
        // ; //show the appropriate popup and set the content 20px from the window top
        /////////////////////////////
        // $("#purchase_popup").show(1000).css({
        //     // "top": scrollTop + 20 + "px"
        // })

        $("#purchase_popup").show("drop", {direction: "up"}, "slow");
    });

    $(document).on('click', '#purchase_close_btn', function () {
        $(".overlay-bg").hide(); //hide the overlay
        $("#purchase_popup").hide("drop", {direction: "up"}, "slow")
        $('body').css({'overflow': 'auto'}); //allow you to scroll the page again
    });


    $("#btn_close_alert").click(function () {
        $("#favor_alert").hide("fade");
    });

    $(document).on("click", '.heart.fa', function () {
        var uid = localStorage.getItem("uid")
        var pid = $(this).attr("data-pid")
        favor_action(pid)
        console.log(uid + pid)
        // $(this).toggleClass("fa-heart fa-heart-o");
    });

    $('.t').on('click', function (e) {
        // alert("s")
        // uid = localStorage.getItem(uid)
        // pid = $(".buy").getAttribute("data-pid")
        // alert(pid)
        // pid =
        //     $.ajax({
        //         type: 'post',
        //         url: url,
        //         xhrFields: {
        //             withCredentials: true
        //         },
        //         headers: {'token': token},
        //         processData: false,
        //         contentType: false,
        //         data: files,
        //         success: function (response) {
        //             if (response.status = "Successful") {
        //                 alert("Your data has been imported to database!")
        //             } else {
        //                 alert("Data import failed!")
        //             }
        //         },
        //         error: function (err) {
        //             alert("Server error")
        //         }
        //     });
    });
})

function retrieve_products() {
    $.ajax({
        url: env.base_api_url + "api/products",
        xhrFields: {
            withCredentials: true
        },
        method: "GET",
        data: {
            token: token
        },
        success: function (data) {
            if (data.status == 200) {
                row_index = 1;
                current_row_id = "";
                for (i = 0; i < data.result.length; i++) {
                    product = data.result[i]
                    // generate row
                    if (i % 3 == 0) {
                        console.log("in")
                        row = `<div class="row product" id="${product.category}_row_${row_index}">`;
                        current_row_id = `${product.category}_row_${row_index}`;
                        $(`#car`).append(row)
                        row_index++;
                    }
                    // retriving info
                    column = `<div class="col-sm-6 col-md-4" id=${product.id}>`
                    current_column_id = `${product.id}`
                    generate_product_html(product, current_row_id, current_column_id)
                }
                // console.log($("#car").html())
            } else {
                console.log("here")
            }
        }
        ,
        error: function () {
            alert(msg.backend_error_msg);
        }
    })
}

function generate_product_html(product, current_row_id, current_column_id) {
    var column = `<div class="col-sm-6 col-md-4" id=${product.id}>`
    var current_column_id = `${product.id}`
    var thumbnail = "<div class='thumbnail'>"
    var img = `<img src='./static/product_images/${product.pics}.jpg'>`
    var caption = '<div class="caption">'
    var desc = `<h4>${product.desc}`
    var shares_avai = `<p>Shares available: ${product.shares_avai}`
    var total_shares = `<p>Total shares: ${product.total_shares}`
    var product_id = `<p>Product ID: ${product.id}`
    var btn_grp = `<p class="control_btn">`
    var purchase_btn = `<a data-pid=${product.id} class="btn btn-primary buy" role="button">Buy shares`
    var favor_btn = `<a data-pid=${product.id} class="btn btn-default favor" role="button">Add to favorite<i data-pid=${product.id} class="heart fa fa-heart-o">`
    // buttons = `<p><a data-pid=${product.id} class="btn btn-primary buy" role="button">Buy shares</a> <a data-pid=${product.id} class="btn btn-default favor" role="button">Add to favorite<i data-pid=${product.id} class="heart fa fa-heart-o"></i></a></p>`
    console.log(i + "#" + current_row_id)
    // append to html element
    $("#" + current_row_id).append(column)
    $("#" + current_column_id).append(thumbnail)
    $("#" + current_column_id + " div").append(img)
    $("#" + current_column_id + " div").append(caption)
    $("#" + current_column_id + " div div").append(desc)
    $("#" + current_column_id + " div div").append(shares_avai)
    $("#" + current_column_id + " div div").append(total_shares)
    $("#" + current_column_id + " div div").append(product_id)
    // $("#" + current_column_id + " div div").append(buttons)
    ////////////////////////////////////
    $("#" + current_column_id + " div div").append(btn_grp)
    $("#" + current_column_id + " div div .control_btn").append(purchase_btn)
    $("#" + current_column_id + " div div .control_btn").append(favor_btn)
    /////////////////////////////////
    display_favor(product.id)
}

function favor_action(pid) {
    selected_favor = $("#" + pid + " i")
    fid = selected_favor.attr("data-fid")
    if (fid != null) {
        console.log("fid is " + fid)
        unfavor(selected_favor);
    } else {
        favor(selected_favor);
    }
}

function unfavor(favor) {
    fid = favor.attr("data-fid")
    $.ajax({
        type: 'DELETE',
        url: env.base_api_url + "api/favor/" + fid,
        xhrFields: {
            withCredentials: true
        },
        headers: {'token': token},
        success: function (response) {
            if (response.status == "200") {
                console.log("Successfuly unfavored fid " + fid + "!")
                favor.removeAttr("data-fid");
                favor.attr("class", "heart fa fa-heart-o")
            } else {
                console.log("Unfavor for fid " + fid + " failed!")
            }
        },
        error: function (err) {
            alert("Server error")
        }
    })
}

function favor(selected_favor) {
    pid = selected_favor.attr("data-pid")
    $.ajax({
        type: 'POST',
        url: env.base_api_url + "api/favor",
        xhrFields: {
            withCredentials: true
        },
        headers: {'token': token},
        data: {
            "pid": pid,
            "uid": localStorage.getItem("uid")
        },
        success: function (response) {
            if (response.status == "200") {
                $("#" + pid + " i").attr("class", "heart fa fa-heart")
                $("#" + pid + " i").attr("data-fid", response.result.favor.id)
                $("#favor_alert").show("fade");
            }
        },
        error: function (err) {
            alert("Server error")
        }
    })
}

function display_favor(pid) {
    console.log("product " + pid)
    $.ajax({
        type: 'GET',
        url: env.base_api_url + "api/favor/is_favored",
        xhrFields: {
            withCredentials: true
        },
        headers: {'token': token},
        data: {
            "pid": pid,
            "uid": localStorage.getItem("uid")
        },
        success: function (response) {
            if (response.status == "200") {
                $("#" + pid + " i").attr("class", "heart fa fa-heart")
                $("#" + pid + " i").attr("data-fid", response.result.favor.id)
            }
        },
        error: function (err) {
            alert("Server error")
        }
    })
}
