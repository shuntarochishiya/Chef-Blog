from flask import render_template, request, Blueprint
from application.database import Post, Ingredient, Category, Cuisine

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/ingredients")
def ingredients():
    page = request.args.get('page', 1, type=int)
    ingredients = Ingredient.query.order_by(Ingredient.name.asc()).paginate(page=page, per_page=10)
    return render_template('ingredients.html', ingredients=ingredients)


@main.route("/categories")
def categories():
    page = request.args.get('page', 1, type=int)
    categories = Category.query.order_by(Category.name).paginate(page=page, per_page=10)
    return render_template('categories.html', categories=categories)


@main.route("/cuisines")
def cuisines():
    page = request.args.get('page', 1, type=int)
    cuisines = Cuisine.query.order_by(Cuisine.name).paginate(page=page, per_page=10)
    return render_template('cuisines.html', cuisines=cuisines)
