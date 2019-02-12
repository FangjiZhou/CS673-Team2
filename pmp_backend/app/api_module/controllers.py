import datetime
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import Blueprint, render_template, flash, g, session, \
    redirect, url_for, Flask, request, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db


# Import module models (i.e. User)
from app.api_module.models import User

# Define the blueprint: 'api', set its url prefix: app.url/auth
api_mod = Blueprint('api', __name__, url_prefix='/api')

from app import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# Set the route and accepted methods
@api_mod.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the rest api for the software engineering, BU-Spring-2019-Team-2'}), 200


@api_mod.route('/doc/', methods=['GET'])
def doc():
    return render_template("docstring.html")


# @api_mod.route('/signin/', methods=['GET', 'POST'])
# def signin():
#
#     # If sign in form is submitted
#     form = LoginForm(request.form)
#
#     # Verify the sign in form
#     if form.validate_on_submit():
#
#         user = User.query.filter_by(email=form.email.data).first()
#
#         if user and check_password_hash(user.password, form.password.data):
#
#             session['user_id'] = user.id
#
#             flash('Welcome %s' % user.name)
#
#             return redirect(url_for('auth.home'))
#
#         flash('Wrong email or password', 'error-message')
#
#     return render_template("auth/signin.html", form=form)