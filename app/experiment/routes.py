import os
from flask import current_app, render_template, redirect, request, session, url_for
from werkzeug.utils import secure_filename
from app.experiment import bp
import pandas as pd
import hpo.src.main as hpo

@bp.route("/", methods=["GET", "POST"]) # Decorator for the index function, which is the view function for the index page
def index(): # View function for the index page
    if request.method == "POST":
        # session["experiment_metadata"] = request.form
        return redirect(url_for("experiment.upload_dataset"))
    return render_template("experiment/new_experiment.html") # Render the experiment template (experiment.html), which will fill any jinja2 template tags with the values provided in the render_template function call




@bp.route("/upload_dataset", methods=["GET", "POST"])
def upload_dataset():
    if request.method == "POST":
        file = request.files["dataset"]
        file_name = secure_filename(file.filename)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], file_name))
        hpo.Main.main()
        return redirect(url_for("results.index", filename=file_name))
    return render_template("experiment/upload_dataset.html")

# @bp.route("/configure_dataset/<file_name>")
# def configure_dataset(file_name):
#     df = pd.read_csv(os.path.join(current_app.config["UPLOAD_FOLDER"], file_name))
#     return render_template("experiment/configure_dataset.html", file_name=file_name, tables=df.to_html())
