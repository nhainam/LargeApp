__author__="nhainam"

from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import LoginManager, login_required

mod_product = Blueprint('product', __name__)


@mod_product.route('/list', methods=['GET'])
def list():
    return render_template('product/index.html')


@mod_product.route('/detail/<product_id>', methods=['GET'])
def detail(product_id):
    return render_template('product/detail.html', product_id = int(product_id))


@mod_product.route('/cart')
def cart():
    return render_template('product/cart.html')


@mod_product.route('/cart/update/<product_id>')
def cart_add_product(product_id):
    product_id = int(product_id)
    if product_id<=0:
        raise Exception("Product is not found!")
    return redirect(url_for("product.cart"))


@mod_product.route('/order', defaults={'step_id':1})
@mod_product.route('/order/<step_id>')
@login_required
def order(step_id):
    if int(step_id) not in range(1,3):
        return render_template('404.html'), 404
    return render_template('product/order_%s.html' % step_id)
