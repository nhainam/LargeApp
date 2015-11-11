__author__="nhainam"

def allowed_file(filename, allowed_file):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowed_file