# Import flask dependencies
from flask import Blueprint, request, render_template,\
                  flash, session, redirect, url_for, abort
from flask.ext.login import LoginManager, login_required, logout_user, login_user, current_user

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)

from app import app
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@mod_auth.route('/register', methods=['GET','POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    user = User(request.form['username'],request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('auth.login'))


@mod_auth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('product.list'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email==request.form["email"]).first()
        login_user(user)
        flash('Logged in successfully!')
        next = request.args.get('next')
        return redirect(next or url_for('product.list'))
    return render_template('auth/login.html', form=form)


@mod_auth.route('/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@mod_auth.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    if request.method == 'GET':
        return render_template('auth/profile.html')
    return redirect(url_for('auth.login'))
