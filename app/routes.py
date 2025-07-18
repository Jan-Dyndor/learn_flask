from app import app


@app.route("/")
def home():
    return "hello"


@app.route("/<name>")
def welcome_name(name):
    return "Welcome %s" % name


@app.route("/blog/<int:postID>")
def show_blog_post(postID):
    return "PostID: %d" % postID


@app.route("/rev/<float:rev>")
def show_rev(rev):
    return "Movie rating is: %f" % rev
