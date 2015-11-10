__author__="nhainam"

from flask import Blueprint, render_template

mod_home = Blueprint('home', __name__, url_prefix='/')

@mod_home.route('/')
def home_page():
    print __name__
    return render_template('home/index.html')