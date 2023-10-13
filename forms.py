from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class Signup(FlaskForm):
    name = StringField('name',validators=[InputRequired()])
    email = StringField('email',validators=[InputRequired(),Email()])
    password = PasswordField('password',validators=[InputRequired()])
    confirm_password = PasswordField('confirm password', validators=[InputRequired(),EqualTo('password')])
    submit = SubmitField('submit')
