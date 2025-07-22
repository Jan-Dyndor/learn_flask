from app import app
from flask import redirect, render_template, url_for, request, make_response


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog/<int:postID>")
def show_blog_post(postID):
    return "PostID: %d" % postID


@app.route("/rev/<float:rev>")
def show_rev(rev):
    return "Movie rating is: %f" % rev


### Dynamically Builded URL
@app.route("/admin")
def welcome_admin():
    return "hello admin"


@app.route("/<name>")
def welcome_guest(name):
    return "hello guest %s" % name


@app.route("/user")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("welcome_admin"))
    else:
        return redirect(url_for("welcome_guest"))


# Cookies


@app.route("/setcookie", methods=["GET", "POST"])
def setcookie():
    if request.method == "POST":
        user_ID = request.form["ID"]
        response = make_response(render_template("cookie.html"))
        response.set_cookie(
            "userID", user_ID
        )  # we end up with key-value pair userID : user_ID
        return response
    return render_template("index.html")


@app.route("/getcookie")
def getcookie():
    user_ID = request.cookies.get("userID")
    return f"<h1>Welcome {user_ID}</h1>"
