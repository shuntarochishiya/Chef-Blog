from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from application import db
from application.database import Post, Comment, Like, Cuisine, Category, Ingredient, post_ingredient_association
from application.posts.forms import PostForm, SearchForm

posts = Blueprint('posts', __name__)


@posts.context_processor
def navbar():
    form = SearchForm()
    return dict(form=form)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    form.category.choices = [(ca.id, ca.name) for ca in Category.query.order_by(Category.name.asc()).all()]
    form.cuisine.choices = [(cu.id, cu.name) for cu in Cuisine.query.order_by(Cuisine.name.asc()).all()]
    form.ingredient.choices = [(i.id, i.name) for i in Ingredient.query.order_by(Ingredient.name.asc()).all()]
    if form.validate_on_submit():
        flash("Your post has been created!", 'success')
        post = Post(title=form.title.data, content=form.content.data, author=current_user, calories=form.calories.data,
                    lipids=form.lipids.data, carbohydrates=form.carbohydrates.data, proteins=form.proteins.data)

        categories = Category.query.filter(Category.id.in_(form.category.data)).all()
        cuisines = Cuisine.query.filter(Cuisine.id.in_(form.cuisine.data)).all()

        post.cuisines.extend(cuisines)
        post.categories.extend(categories)

        db.session.add(post)
        db.session.commit()

        for i in range(len(request.form.getlist('ingredient'))):
            ingredient_id = int(request.form.getlist('ingredient')[i])
            amount = int(request.form.getlist('amount')[i])

            post_ingredients = post_ingredient_association.insert().values(post_id=post.id, ingredient_id=ingredient_id, amount=amount)
            db.session.execute(post_ingredients)
            db.session.commit()

        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    cuisines = Cuisine.query.all()
    categories = Category.query.all()
    ingredients = Ingredient.query.all()
    return render_template('post.html', title=post.title, post=post, cuisines=cuisines, categories=categories, ingredients=ingredients)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and current_user.role != 'admin':
        abort(403)
    form = PostForm()
    form.category.choices = [(ca.id, ca.name) for ca in Category.query.all()]
    form.cuisine.choices = [(cu.id, cu.name) for cu in Cuisine.query.all()]
    form.ingredient.choices = [(i.id, i.name) for i in Ingredient.query.all()]
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.calories = form.calories.data
        post.lipids = form.lipids.data
        post.carbohydrates = form.carbohydrates.data
        post.proteins = form.proteins.data

        post.cuisines = []
        post.ingredients = []
        post.categories = []

        categories = Category.query.filter(Category.id.in_(form.category.data)).all()
        cuisines = Cuisine.query.filter(Cuisine.id.in_(form.cuisine.data)).all()

        for i in range(len(request.form.getlist('ingredient'))):
            ingredient_id = int(request.form.getlist('ingredient')[i])
            amount = int(request.form.getlist('amount')[i])

            post_ingredients = post_ingredient_association.insert().values(post_id=post.id, ingredient_id=ingredient_id, amount=amount)
            db.session.execute(post_ingredients)
            db.session.commit()

        post.cuisines.extend(cuisines)
        post.categories.extend(categories)
        db.session.commit()
        flash("Your post has been updated!", 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.lipids.data = post.lipids
        form.calories.data = post.calories
        form.carbohydrates.data = post.carbohydrates
        form.proteins.data = post.proteins
        form.ingredient.data = post.ingredients
        form.cuisine.data = post.cuisines
        form.category.data = post.categories
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and current_user.role != 'admin':
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post has been deleted!", 'info')
    return redirect(url_for('main.home'))


@posts.route("/create-comment/<int:post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')
    post = Post.query.get_or_404(post_id)
    if not text:
        flash("Comment can not be empty!", 'warning')
    else:
        comment = Comment(text=text, author=current_user, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash("Comment has been added successfully!", 'success')

    return redirect(url_for('posts.post', post_id=post.id))


@posts.route("/delete-comment/<int:comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if current_user != comment.author and current_user != comment.post.author and current_user.role != 'admin':
        abort(403)
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('main.home'))


@posts.route("/like-post/<int:post_id>", methods=['GET'])
@login_required
def like(post_id):
    post = Post.query.get_or_404(post_id)
    like = Like.query.filter_by(author=current_user, post_id=post_id).first()
    if like:
        db.session.delete(like)
    else:
        like = Like(author=current_user, post_id=post_id)
        flash("Post added to favourites", 'info')
        db.session.add(like)
    db.session.commit()

    return redirect(url_for('posts.post', post_id=post.id))


@posts.route("/cuisine/<int:cuisine_id>")
def dish_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('dish_cuisines.html', posts=posts, cuisine=cuisine)


@posts.route("/category/<int:category_id>")
def dish_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('dish_categories.html', posts=posts, category=category)
