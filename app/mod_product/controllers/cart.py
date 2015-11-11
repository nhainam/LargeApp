__author__="nhainam"

from flask import render_template, redirect, url_for

def list():
    return render_template('product/cart.html')


def add(product_id):
    product_id = int(product_id)
    if product_id <= 0:
        raise Exception("Product is not found!")
    return redirect(url_for("product.cart"))