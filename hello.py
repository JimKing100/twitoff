# Import Flask package

from flask import Flask, render_template

# Create Flask web server, makes the application
app = Flask(__name__)

# Routes determine location
@app.route("/")

def home():
    return render_template("home.html")

@app.route("/about")

def preds():
    return render_template("about.html")

@app.route("/contact")

def cons():
    return render_template("contact.html")
