# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    oid           = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name    = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email    = db.Column(db.String(128), nullable=False,
                                            unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role     = db.Column(db.SmallInteger, nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):
        self.name     = name
        self.email    = email
        self.password = password

    # def get_user(self, user_id):
    #     return db.session.query(User).get(user_id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
       return unicode(self.oid)

    def get_list_user(self):
        return self.query.all()

    def add_user(self):
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<User %r>' % (self.name)
