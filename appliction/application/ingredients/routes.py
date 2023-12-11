from flask import render_template, request, Blueprint
from application.database import Ingredient

ingredient = Blueprint('ingredients', __name__)


@ingredient.route('/ingredients')
def all():
    pass
