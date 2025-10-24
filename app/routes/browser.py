from flask import Blueprint, render_template

browser = Blueprint("browser", __name__)


@browser.get("/")
def index():
    return render_template("index.html")
