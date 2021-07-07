from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Blog
from . import db
import json


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

@views.route('/delete-blog', methods=['POST'])
def delete_blog():
    blog = json.loads(request.data)
    blogId = blog['blogId']
    blog = Blog.query.get(blogId)

    if blog:
        if blog.user_id == current_user.id:
            db.session.delete(blog)
            db.session.commit()
    return jsonify({})


    

# @views.route('/login')
# def login():
#     return render_template("login.html")

# @views.route('/register')
# def register():
#     return render_template("register.html")

