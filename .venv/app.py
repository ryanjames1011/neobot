from flask import Flask, render_template

# configure application
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# index page 
@app.route("/")
def index():
    return render_template("index.html")

# the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

# make an account page
@app.route("/create")
def create():
    return render_template("create.html")

# continue with no account
@app.route("/noacc")
def noacc():
    return render_template("noacc.html")

# the actual chatbot page
@app.route("/botpage")
def botpage():
    return render_template("botpage.html")