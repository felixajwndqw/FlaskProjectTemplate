from flask import redirect  # , render_template, url_for
from app.auth import bp


@bp.route('/auth', methods=['GET', 'POST'])
def auth():
    pass


@bp.route("/callback/q")
def callback():
    pass