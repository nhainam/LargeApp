__author__="nhainam"

def step(step_id):
    if int(step_id) not in range(1, 3):
        return render_template('404.html'), 404
    return render_template('product/order_%s.html' % step_id)