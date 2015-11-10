__author__ = "nhainam"

from app import db
from app.mod_product.models import mbase


# Define a Product model
class MImage(mbase.Base):
    __tablename__ = 'images'

    # Product Fields
    product_id = db.Column(db.Integer, nullable=False)
    file_name = db.Column(db.String(250), nullable=False)
    default = db.Column(db.Boolean, nullable=False)

    # New instance instantiation procedure
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def validate(self):
        o_image = self.query.filter(self.name == self.name, self.file_name = self.file_name).first()
        if o_image:
            return False
        return True

    def add(self):
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<Product %r>' % (self.name)
