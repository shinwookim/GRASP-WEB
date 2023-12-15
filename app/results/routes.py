from flask import render_template, redirect, url_for, flash, request, jsonify, current_app
from app.results import bp
import os
from app.results import report
from app.models.result import Result
from app.extensions import db

@bp.route("/<filename>") # Decorator for the index function, which is the view function for the index page
def index(filename): # View function for the index page
    # find all png files in the static folder with the filename
    files = []
    #print current working directory
    print(os.getcwd())
    for file in os.listdir(os.path.join(current_app.config['CHARTS_FOLDER'])):
        # if the filename is in the file name, and it is a png file
        if filename in file and file.endswith('.png'):
            files.append(file)

    run_png = None
    box_png = None
    time_png = None
    for file in files:
        if 'run' in file:
            run_png = file
        elif 'box' in file:
            box_png = file
        elif 'time' in file:
            time_png = file
    
    for file in files:
        print(file)

    # Add the results to the database
    return render_template("results/results-bkup.html")
    # return render_template("results/results.html", run_png = run_png, box_png = box_png, time_png = time_png) # Render the results template, which will fill any jinja2 template tags with the values provided in the render_template function call

@bp.route("/history")
def history():
    results = Result.query.all()
    return render_template("results/history.html", results=results)

# @bp.route("/history/<filename>")
# def history_file(filename):
#     return render_template("results/history_file.html", filename=filename)