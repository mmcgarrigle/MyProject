from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length, length


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=4, max=30)
                             ]
                             )

    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=4, max=30)
                            ]
                            )
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               length(min=4, max=30)
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
