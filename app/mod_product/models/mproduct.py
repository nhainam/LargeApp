__author__="nhainam"

from app import db
from app.mod_product.models import mbase

# Define a Product model
class MProduct(mbase.Base):

    __tablename__ = 'products'

    # Product Fields
    name        = db.Column(db.String(50), nullable=False, unique=True)
    summary     = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price       = db.Column(db.Integer, nullable=False)
    status      = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, **kwargs):
    	for k, v in kwargs.items():
    		setattr(self, k, v)


    def validate(self):
        o_product =  self.query.filter_by(name=self.name).first()
        if o_product:
            return False
        return True

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self.id


    def __repr__(self):
        return '<Product %r>' % (self.name)