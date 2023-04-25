from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import current_user, login_user, login_required

from app import db
from app.models import User, Message, Discussion
from app.forms import SignupForm, SignInForm

bp = Blueprint("main", __name__)

# main interface
@bp.route("/")
def index():
    """
    The main page with connection to the dashboard (if logged in)
    """
    return render_template("index.html")

@bp.route("/dashboard")
@login_required
def dashboard():
    """
    User dashboard with all their past discussions
    """
    # retrieve the user's username
    username = current_user.username

    # retrieve the user's email
    email = current_user.email

    # retrieve past's discussions with the user
    discussions = Discussion.query.filter_by(user_id=current_user.id).all() # this is full json files

    return render_template("dashboard.html", username=username, email=email, discussions=discussions)

@bp.route("/discussion/<int:discussion_id>")
@login_required
def discussion(discussion_id):
    """
    Discussion page with all the messages
    """
    # retrieve the discussion
    discussion = Discussion.query.filter_by(id=discussion_id).first()

    # retrieve the messages
    messages = Message.query.filter_by(discussion_id=discussion_id).all()

    return render_template("discussion.html", discussion=discussion, messages=messages)