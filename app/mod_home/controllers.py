__author__="nhainam"

from flask import Blueprint, render_template

mod_home = Blueprint('home', __name__, url_prefix='/home')

@mod_home.route('/')
@mod_home.route('/index')
def home():
    return render_template('home/index.html')