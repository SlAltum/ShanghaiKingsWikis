import os
import werkzeug
from flask import Flask,send_from_directory,render_template,redirect

app = Flask(__name__)

def get_content(path):
    content = ""
    try:
        content = render_template(path)
    except:
        content = render_template("default.html")
    return content
@app.route("/favicon.ico")
def get_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/logo.png")
def get_logo():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'logo.png')

@app.route("/")
def index():
    return render_template("index.html",content=get_content("indexcontent.html"))

@app.route("/index")
def index_2():
    return redirect("/")
# === background === #
@app.route("/background/favicon.ico")
def get_favicon_bg():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/background/logo.png")
def get_logo_bg():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'logo.png')

@app.route("/background/apocalypse")
def bg_apocalypse():
    return render_template("index.html",content=get_content("background/apocalypse.html"))
# === post-apocalypse-life === #
@app.route("/post-apocalypse-life/favicon.ico")
def get_favicon_pal():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
# === worldinfo === #
@app.route("/worldinfo/favicon.ico")
def get_favicon_worldinfo():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/worldinfo/the-world")
def wd_info_theworld():
    return render_template("index.html",content=get_content("/worldinfo/the-world.html"))
# === game-concept === #
@app.route("/game-concept/favicon.ico")
def get_favicon_gc():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
# === available-information === #
@app.route("/available-information/favicon.ico")
def get_favicon_ai():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
# === about-us === #
@app.route("/about-us/favicon.ico")
def get_favicon_au():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=False)