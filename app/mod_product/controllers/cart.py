__author__="nhainam"

from flask import render_template, redirect, url_for, session

def list():
    cart_items = []
    if session.has_key('cart'):
        cart_items = session['cart']
    else:
        session['cart'] = [
            {
                'id': '01',
                'name': 'test 1',
                'price': 2000,
                'image': 'image.gif'
            },
            {
                'id': '02',
                'name': 'test 2',
                'price': 3000,
                'image': 'image.gif'
            }
        ]
    return render_template('product/cart.html', cart_items=cart_items)


def add(product_id):
    product_id = int(product_id)
    if product_id <= 0:
        raise Exception("Product is not found!")
    return redirect(url_for("product.cart_list"))