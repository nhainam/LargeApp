__author__ = "nhainam"

from flask import Blueprint, render_template, redirect, url_for, request
from flask.ext.login import login_required
from flask.ext.uploads import UploadSet
from app.mod_product.models.mproduct import MProduct

mod_product = Blueprint('product', __name__)


@mod_product.route('/list', methods=['GET'])
@login_required
def list():
    return render_template('product/index.html')


@mod_product.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        o_product = MProduct(name=request.form.get('name'),
                             summary=request.form.get('summary'),
                             description=request.form.get('description'),
                             image_id=1,
                             price=request.form.get('price'),
                             status=request.form.get('status'))
        if o_product.validate():
            o_product.add()
            return redirect(url_for('product.list'))
    return render_template('product/add.html')


@mod_product.route('/detail/<product_id>', methods=['GET'])
def detail(product_id):
    return render_template('product/detail.html', product_id=int(product_id))


@mod_product.route('/cart')
def cart():
    return render_template('product/cart.html')


@mod_product.route('/cart/update/<product_id>')
def cart_add_product(product_id):
    product_id = int(product_id)
    if product_id <= 0:
        raise Exception("Product is not found!")
    return redirect(url_for("product.cart"))


@mod_product.route('/order', defaults={'step_id': 1})
@mod_product.route('/order/<step_id>')
@login_required
def order(step_id):
    if int(step_id) not in range(1, 3):
        return render_template('404.html'), 404
    return render_template('product/order_%s.html' % step_id)
