from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    first_name = StringField(validators=[
        InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "First name"}
    )
    last_name = StringField(validators=[
        InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Last name"}
    )
    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    email = EmailField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Email"})
    phone_number = StringField(validators=[
        InputRequired(), Length(min=11, max=20)], render_kw={"placeholder": "Phone number"})
    submit = SubmitField('Register')
