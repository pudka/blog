from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
    TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, \
    ValidationError
from blog.models import User


class RegistrationForm(FlaskForm):
    """ Registration new user's."""
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. \
            Please choose a different one.')

    def validate_email(self, email):
        email_exist = User.query.filter_by(email=email.data).first()
        if email_exist:
            raise ValidationError('That email is taken. \
            Please choose a different one.')


class LoginForm(FlaskForm):
    """ Login user's."""
    email = StringField('Email',
                        validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Email address"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class PostForm(FlaskForm):
    """ Post form """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
