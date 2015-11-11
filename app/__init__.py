# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_home.controllers import mod_home as home_module
from app.mod_product.routers import mod_product as product_module
from app.mod_news.controllers import mod_news as news_module

# Register blueprint(s)

app.register_blueprint(product_module, url_prefix='/product')
app.register_blueprint(auth_module, url_prefix='/auth')
app.register_blueprint(news_module, url_prefix='/news')
app.register_blueprint(home_module, url_prefix='/')

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
