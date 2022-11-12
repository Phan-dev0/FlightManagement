import sys
sys.path.append("./")
from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("pages/index.html")


if __name__ == "__main__":
    app.run()
