__author__="nhainam"

from flask import Blueprint, render_template

mod_news = Blueprint('news', __name__)

@mod_news.route('/')
def list():
    return render_template('news/index.html')