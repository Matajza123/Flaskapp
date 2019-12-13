from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flaskapp.models import User, Post
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NoneOf


class RegistrationForm(FlaskForm):
    username = StringField('Imię i Nazwisko', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    tel_nr = StringField('Numer telefonu', validators=[DataRequired(), Length(min=9, max=9)])
    age = StringField('Wiek', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    confirm_password = PasswordField('Potwierdź Hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Ten email jest już zajęty. Wybierz inny.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj')


class MngForm(FlaskForm):
    choroba = StringField('Choroby')
    objawa = StringField('Objawy')
    notes = StringField('Notatki')
    picture = FileField('Picture')
    submit = SubmitField('Potwierdz')
