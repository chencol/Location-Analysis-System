from flask import request, jsonify

from backend import app


@app.route('/')
def hello_world():
    return 'Hello, World! Remove unnecessary Test!'

@app.route('/b1')
def b1():
    return 'Branch 1 for testing purpose! New Modification! Again!'

# @app.route('/verify_user')
# def verify_user():
#     name = request.args.get("name")
#     password = request.args.get("password")
#
#     if name == "Colin" and password == "exceptional":
#         result = "true"
#     else:
#         result = "false"
#     return jsonify(result=result)

    # resp = make_response("home page", 404)
    # resp = make_response(json.dumps({"name":"tom"}),200)
    # resp.headers["Content-type"] = "application/json"
    # resp = make_response()
    # # resp.response = "abc"
    # resp.response = render_template("index.html")
    # resp.status_code = 200
    # resp.status = "200"
    # return "Hello world"

    # return "home page"
    # return(String, response code)
    # return ("Home page", 404)
    # return "Home page"


# @app.route("/a/")
# def rq_a():
#     return render_template("page_a.html")
    # return redirect("/b/")
    # Redirect to the route that correspond to the end point "rq_b"
    # return redirect(url_for("rq_b"))
    # return redirect("http://www.baidu.com")


# @app.route("/user_info/")
# def user_info():
#     user_list = []
#     for user in User.query.all():
#         user_list.append(user)
#     return render_template("user_info.html", user_list=user_list)
#
#
# @app.route("/login/")
# def login():
#     return render_template("login.html")
#
#
# @app.route("/register/")
# def register():
#     return render_template("register.html")
#
#
# @app.route("/test_sss/")
# def test_css():
#     return render_template("grid inside grid.html")
#
#
# @app.route("/about/")
# def rq_b():
#     return render_template("page_b.html")
#
#
# @app.route("/ajax_test/")
# def ajax_request():
#     return render_template("test_ajax.html")
#
#
# @app.route("/base")
# def show_base():
#     return render_template("base.html")
#
#
# @app.route("/child")
# def show_child():
#     return render_template("child.html")
#
#
# # @app.route('/greet/')
# # def add_numbers():
# #     name = request.args.get("name")
# #     password = request.args.get("password")
# #
# #     if name == "Colin" and password == "exceptional":
# #         result = "true"
# #     else:
# #         result = "false"
# #     return jsonify(result=result)
#
#
# @app.route("/help/")
# def req_help():
#     abort(404)
#
#
# @app.route('/set/')
# def set():
#     session['key'] = 'interesting'
#     session["username"] = "Colin"
#     res = make_response("Setting a cookie")
#     res.set_cookie('foo', 'bar', max_age=60 * 60 * 24 * 365 * 2)
#     return res
#
#
# @app.route('/get/')
# def get():
#     return session.get('key', 'not set')
#
#
# @app.route("/test_session/")
# def test_session():
#     return render_template("page_c.html")
#
#
# @app.route("/rq/")
# def test_rq():
#     data = {}
#     data["ip"] = request.remote_addr
#     data["full_path"] = request.full_path
#     data["url"] = request.url
#     data["is_xhr"] = request.is_xhr
#     data["endpoint"] = request.endpoint
#     return str(data)
#
#
# @app.route("/reg/")
# def reg():
#     return render_template("reg.html")
#
#
# @app.route("/reg1/")
# def reg1():
#     return render_template("reg1.html")
#
#
# @app.route("/add_user1/", methods=['POST'])
# def add_user1():
#     name = request.form['name']
#     email = request.form['email']
#     result = "This is from server side " + name + " : " + email
#     return jsonify(result=result)


# @app.route("/add_user/")
# def add_user():
#     user = {}
#     name = request.args.get("name")
#     email = request.args.get("email")
#     phone_number = request.args.get("phone_number", type=int)
#     password = request.args.get("password")
#     error_msg = check_duplication(name=name, phone=phone_number, email=email)
#     if error_msg == None:
#         n_user = User(name=name, pwd=password, email=email, phone=phone_number)
#         db.session.add(n_user)
#         # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
#         db.session.commit()
#         result = name + " has been added to DB successfully!"
#     else:
#         result = error_msg
#     return jsonify(result=result)
