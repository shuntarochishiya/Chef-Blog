from flask import Blueprint, render_template
from application.posts.forms import SearchForm

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    form = SearchForm()
    return render_template('errors/404.html', form=form), 404


@errors.app_errorhandler(403)
def error_403(error):
    form = SearchForm()
    return render_template('errors/403.html', form=form), 403


@errors.app_errorhandler(500)
def error_500(error):
    form = SearchForm()
    return render_template('errors/500.html', form=form), 500


@errors.app_errorhandler(405)
def error_405(error):
    form = SearchForm()
    return render_template('errors/405.html', form=form), 405
