__author__="nhainam"

import os
from flask import render_template, redirect, url_for, request, current_app
from app.mod_product.models.mproduct import MProduct
from app.mod_product.models.mimage import MImage
from utils import file as file_utils
from werkzeug import secure_filename

def list():
    product_lists = MProduct().get_list()
    print product_lists
    return render_template('product/index.html', product_lists=product_lists)


def add():
    if request.method == 'POST':
        o_product = MProduct(name=request.form.get('name'),
                             summary=request.form.get('summary'),
                             description=request.form.get('description'),
                             price=request.form.get('price'),
                             status=request.form.get('status'))
        if o_product.validate():
            product_id = o_product.add()
            file = request.files.get('image')
            if file and file_utils.allowed_file(file.filename, current_app.config['ALLOWED_EXTENSION_IMAGES']):
                filename = secure_filename(file.filename)
                directory = current_app.config['UPLOAD_FOLDER']
                if not os.path.exists(directory):
                    os.makedirs(directory)
                file.save(os.path.join(directory, filename))
                o_image = MImage(
                                    product_id=product_id,
                                    file_name=filename,
                                    default=True
                                )
                if not o_image.add():
                    pass
            return redirect(url_for('product.list'))
    return render_template('product/add.html')


def detail(product_id):
    product_detail = MProduct().get_detail(product_id)
    return render_template('product/detail.html', product_detail=product_detail)