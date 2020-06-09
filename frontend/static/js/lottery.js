$(function () {
    retrieve_products();
    $(document).on('click', '.buy', function () {
        uid = localStorage.getItem("uid");
        pid = $(this).attr("data-pid");
        alert("Product id is " + pid + " and uid is t1 " + uid)
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
                console.log($("#car").html())
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
    column = `<div class="col-sm-6 col-md-4" id=${product.id}>`
    current_column_id = `${product.id}`
    thumbnail = "<div class='thumbnail'>"
    img = `<img src='./static/product_images/${product.pics}.jpg'>`
    caption = '<div class="caption">'
    desc = `<h4>${product.desc}`
    shares_avai = `<p>Shares available: ${product.shares_avai}`
    total_shares = `<p>Total shares: ${product.total_shares}`
    product_id = `<p>Product ID: ${product.id}`
    buttons = `<p><a data-pid=${product.id} class="btn btn-primary buy" role="button">Buy shares</a> <a data-pid=${product.id} class="btn btn-default favor" role="button">Add to favorite<i class="heart fa fa-heart-o"></i></a></p>`
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
    $("#" + current_column_id + " div div").append(buttons)
}

function is_favor(pid, uid) {

}