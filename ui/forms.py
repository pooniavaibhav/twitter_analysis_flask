from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):

    twitter_handle = StringField('Twitter Handle', validators=[DataRequired()])
    count =  IntegerField('Number of records', validators=[DataRequired()])
    submit = SubmitField('Submit')