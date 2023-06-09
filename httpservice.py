import os
from werkzeug.routing import BaseConverter
from flask import Flask,send_from_directory,render_template,redirect

app = Flask(__name__)
class ReConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(ReConverter,self).__init__(url_map)
        self.regex=items[0]
app.url_map.converters['re']=ReConverter

def get_content(path):
    content = ""
    try:
        content = render_template(path)
    except:
        content = render_template("default.html")
    return content
# @app.route("/favicon.ico")
# def get_favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
# @app.route("/<re(r'.*'):url_path>/favicon.ico")
# def get_favicon2(url_path):
#     print("url_path = "+url_path)
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route("/logo.png")
# def get_logo():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'logo.png')

@app.errorhandler(404)
def page_not_found(error):
    return redirect("/page404")\
    
@app.route("/page404")
def page_404():
    return render_template("index.html",content=get_content("default.html"))

@app.route("/")
def index():
    return render_template("index.html",content=get_content("indexcontent.html"))

@app.route("/index")
def index_2():
    return redirect("/")
# === background === #
# @app.route("/background/logo.png")
# def get_logo_bg():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'logo.png')

@app.route("/background/apocalypse")
def bg_apocalypse():
    return render_template("index.html",content=get_content("/background/apocalypse.html"))
# === post-apocalypse-life === #
@app.route("/post-apocalypse-life/economic")
def pal_economic():
    return render_template("index.html",content=get_content("/post-apocalypse-life/economic.html"))
@app.route("/post-apocalypse-life/science")
def pal_science():
    return render_template("index.html",content=get_content("/post-apocalypse-life/science.html"))
@app.route("/post-apocalypse-life/politics")
def pal_politics():
    return render_template("index.html",content=get_content("/post-apocalypse-life/politics.html"))
# === worldinfo === #
@app.route("/worldinfo/the-world")
def wd_info_theworld():
    return render_template("index.html",content=get_content("/worldinfo/the-world.html"))
@app.route("/worldinfo/china")
def wd_info_china():
    return render_template("index.html",content=get_content("/worldinfo/china.html"))
# === game-concept === #
# === available-information === #
# === about-us === #
@app.route("/about-us/community")
def au_community():
    return render_template("index.html",content=get_content("/about-us/community.html"))

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=False)