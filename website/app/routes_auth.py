from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import current_user, login_user

from app import db
from app.models import User
from app.forms import SignupForm, SignInForm

bp = Blueprint("auth", __name__)

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Sign up a user
    """
    form = SignupForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            created_at=datetime.utcnow(),
            confirmed=False,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.index"))

    return render_template("signup.html", form=form)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Sign in a user
    """
    form = SignInForm()

    if form.validate_on_submit():
        # Get the user with the given email from the database
        user = User.query.filter_by(email=form.email.data).first()

        # If the user exists and the password is correct, log them in
        if user is not None and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))

    return render_template('signin.html', form=form)