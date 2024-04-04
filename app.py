from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mike")
def mike():
    n1 = 10
    n2 = 20
    sum = n1 + n2
    return str(sum)


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 4444)), debug=True
    )