from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Blog
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
       
        blog = request.form.get('blog')

        if len(blog) < 1:
            flash('blog or title is too short', category='error')
        else:
            new_blog = Blog(content=blog, user_id=current_user.id)
            db.session.add(new_blog)
            db.session.commit()
            flash('Blog added!', category='success')


    return render_template("home.html", user=current_user)

# @views.route('/login')
# def login():
#     return render_template("login.html")

# @views.route('/register')
# def register():
#     return render_template("register.html")

