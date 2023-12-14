from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    carbohydrates = IntegerField('Carbohydrates', validators=[DataRequired()], render_kw={"placeholder": "Carbohydrates"})
    lipids = IntegerField('Lipids', validators=[DataRequired()], render_kw={"placeholder": "Lipids"})
    proteins = IntegerField('Proteins', validators=[DataRequired()], render_kw={"placeholder": "Proteins"})
    calories = IntegerField('Calories', validators=[DataRequired()], render_kw={"placeholder": "Calories"})
    submit = SubmitField('Post')
    cuisine = SelectMultipleField('Select origin (one or several)', choices=[], coerce=int)
    category = SelectMultipleField('Select category (one or several)', choices=[], coerce=int)
    ingredient = SelectMultipleField('Select ingredients (one or several)', choices=[], coerce=int)


class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField('Search')
