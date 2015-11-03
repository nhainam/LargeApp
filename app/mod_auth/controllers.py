# Import flask dependencies
from flask import Blueprint, request, render_template,\
                  flash, session, redirect, url_for
from flask.ext.login import LoginManager, login_required

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

from app import app
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@mod_auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('auth.login'))


@mod_auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    return redirect(url_for('home.index'))


@mod_auth.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    if request.method == 'GET':
        return render_template('auth/profile.html')
    return redirect(url_for('auth.login'))