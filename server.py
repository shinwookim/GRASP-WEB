from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/experiment")
def experiment():
    return render_template("experiment.html")


@app.route("/results")
def sample_results():
    return render_template("results.html")
