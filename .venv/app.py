from flask import Flask, render_template

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/noacc")
def noacc():
    return render_template("noacc.html")

@app.route("/botpage")
def botpage():
    return render_template("botpage.html")