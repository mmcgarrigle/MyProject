from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PostsForm(FlaskForm):
    q1 = StringField(
        '1. What kind of coat is always wet when you put it on?',
        validators=[
            DataRequired(),
            Length(min=1, max=10)
        ]
    )

    q2 = StringField(
        '2. What disappears as soon as you speak its name?',
        validators=[
            DataRequired(),
            Length(min=1, max=10)
        ]
    )

    q3 = StringField(
        '3. I can only live where there is light but if a light shines on me, I die. What am I?',
        validators=[
        DataRequired(),
        Length(min=1, max=10)
        ]
    )

    q4 = StringField(
        '4. You walk into a room containing a kerosene lamp, a candle and a fireplace. You only have one match. Which '
        'one do you light first?',
        validators=[
            DataRequired(),
            Length(min=1, max=10)
        ]
    )

    q5 = StringField(
        '5. What five letter word becomes shorter when you add two letters to it?',
        validators=[
            DataRequired(),
            Length(min=1, max=10)
        ]
    )

    submit = SubmitField('Submit')