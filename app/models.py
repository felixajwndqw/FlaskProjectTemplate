from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(u_id):
    return User.query.get(int(u_id))


class User(UserMixin, db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # # Foreign relation example:
    # <table_name> = db.relationship('<Table_name>', backref='user', lazy='dynamic')

    def get_id(self):
        return self.u_id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
