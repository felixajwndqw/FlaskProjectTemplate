from flask import render_template  # , url_for, redirect
from app.main import bp


@bp.route("/")
def index():
    return render_template('index.html')