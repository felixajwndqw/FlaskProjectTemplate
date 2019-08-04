from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
import json


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()

    # For post request
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            return json.dumps(
                {
                    'success': False
                }), 200, {'ContentType': 'application/json'}
        if user.check_password(form.password.data):
            login_user(user, remember=True)
            return json.dumps(
                {
                    'success': True,
                    'username': user.username
                }), 200, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'success': False
                }), 200, {'ContentType': 'application/json'}
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()

    # For post request
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return json.dumps(
            {
                'success': True,
                'username': user.username
            }), 200, {'ContentType': 'application/json'}
    return render_template('register.html', title='Register', form=form)
