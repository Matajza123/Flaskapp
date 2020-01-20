from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel_nr = db.Column(db.String(9),unique=True, nullable=False)
    age = db.Column(db.String(2), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(5), default='0')

    posts = db.relationship('Post', backref='author', lazy=True)
    info = db.relationship('Info', backref='author')
    photo = db.relationship('Photo', backref='author')

    def __repr__(self):
        return f"User('Imię: {self.username}', 'Wiek: {self.age}', 'Tel: {self.tel_nr}', 'ID: {self.id}')"

class Post(db.Model):
    post_id = db.Column(db.Integer, nullable=False, primary_key=True)
    post_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created = db.Column(db.Text, default="Nie podano")
    choroba = db.Column(db.Text, default="Nie podano")
    objawa = db.Column(db.Text, default="Nie podano")
    notes = db.Column(db.Text, default="Nie podano")

    visit_nr = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Post(Utworzono: '{self.created}', Choroba: '{self.choroba}', Objawa: '{self.objawa}', Notatki: '{self.notes}', Numer wizyty: '{self.visit_nr}')"

class Info(db.Model):
    info_id = db.Column(db.Integer, nullable=False, primary_key=True)
    info_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.Text)

    def __repr__(self):
        return f"Info('{self.info_id}', {self.created}', '{self.last_login}', '{self.last_visit}', '{self.visit_nr}')"


class Photo(db.Model):
    photo_id = db.Column(db.Integer, nullable=False, primary_key=True)
    photo_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.Text, default="")
    photo = db.Column(db.String(20), default="")

    def __repr__(self):
        return f"Photo('{self.photo}')"

class Ban_list(db.Model):
    ban_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer)
    time = db.Column(db.Text)

    def __repr__(self):
        return f"Ban_list('{self.ban_id }', '{self.user_id}','{self.time}')"