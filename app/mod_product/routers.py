__author__ = "nhainam"

from flask import Blueprint
from flask.ext.login import login_required
from app.mod_product.controllers import product, cart, order

mod_product = Blueprint('product', __name__)


@mod_product.route('/list', methods=['GET'])
@login_required
def list():
    return product.list()


@mod_product.route('/add', methods=['GET', 'POST'])
def add():
    return product.add()


@mod_product.route('/detail/<product_id>', methods=['GET'])
def detail(product_id):
    return product.detail(product_id)


@mod_product.route('/cart', methods=['GET'])
def cart_list():
    return cart.list()


@mod_product.route('/cart/update/<product_id>', methods=['GET'])
def cart_add_product(product_id):
    return cart.add(product_id)


@mod_product.route('/order', defaults={'step_id': 1})
@mod_product.route('/order/<step_id>')
@login_required
def order(step_id):
    return order.step(step_id)
