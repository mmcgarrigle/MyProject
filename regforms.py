from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                             ]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ]
                                     )
    submit = SubmitField('Sign Up')

    # def validate_email(self, email):
    # user = Users.query.filter_by(email=email.data).first()

    #  if user:
    #     raise ValidationError('Email already in use')
