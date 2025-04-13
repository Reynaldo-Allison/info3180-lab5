# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[
        InputRequired(message='Movie title is required')
    ])
    
    description = TextAreaField('Description', validators=[
        InputRequired(message='Description is required')
    ])
    
    poster = FileField('Poster', validators=[
        FileRequired(message='Poster image is required'),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Only JPG, JPEG, and PNG images are allowed')
    ])
