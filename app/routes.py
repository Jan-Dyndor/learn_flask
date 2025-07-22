from app import app
from flask import redirect, render_template, url_for


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
