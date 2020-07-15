from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import Comment, User, Pitch
from flask_login import login_required
from .forms import PitchForm, CommentForm
from .. import db

# Main page
@main.route('/')
def index():
    '''
    Homepage
    '''

    return render_template('index.html')

@main.route('/pitch/comment/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    pass

@main.route('/pitch/<uname>/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch(uname):
    form = PitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data
        category = form.category.data
        upvotes = 0
        downvotes = 0
        submitted_by = user = User.query.filter_by(username = uname).first()

    return render_template('pitch.html', uname=uname)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)