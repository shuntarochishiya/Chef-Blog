from datetime import datetime
from application import db, login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


post_cuisine_association = Table(
    'post_cuisine_association',
    db.Model.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('cuisine_id', Integer, ForeignKey('cuisine.id'))
)


post_category_association = Table(
    'post_category_association',
    db.Model.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)


post_ingredient_association = Table(
    'post_ingredient_association',
    db.Model.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id')),
    Column('amount', Integer)
)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.jpg', nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)
    reg_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    bio = db.Column(db.String(200))
    role = db.Column(db.String(15), nullable=False, default='user')
    posts = db.Relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")
    comments = db.Relationship('Comment', backref='author', lazy=True, cascade="all, delete-orphan")
    likes = db.Relationship('Like', backref='author', lazy=True, cascade="all, delete-orphan")

    def get_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
            print(user_id)
        except:
            return None
        return Users.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.role}', '{self.bio}', '{self.image_file}', '{self.reg_date}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.Relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")
    like = db.Relationship('Like', backref='post', lazy=True, cascade="all, delete-orphan")
    calories = db.Column(db.Integer, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    lipids = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)
    cuisines = relationship('Cuisine', secondary=post_cuisine_association, back_populates='posts')
    categories = relationship('Category', secondary=post_category_association, back_populates='posts')
    ingredients = relationship('Ingredient', secondary=post_ingredient_association, back_populates='posts')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.timestamp}', '{self.text}')"


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Ingredient(db.Model):
    name = db.Column(db.String(20), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    expiration_date = db.Column(db.String(20))
    category = db.Column(db.String(20))
    posts = relationship('Post', secondary=post_ingredient_association, back_populates='ingredients')


class Cuisine(db.Model):
    name = db.Column(db.String(20), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    posts = relationship('Post', secondary=post_cuisine_association, back_populates='cuisines')


class Category(db.Model):
    name = db.Column(db.String(20), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    posts = relationship('Post', secondary=post_category_association, back_populates='categories')
