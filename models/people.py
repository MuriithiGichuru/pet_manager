# import the db object from app.py file
from app import db

#use the Model class, which is the base declarative class used to declare your models
# use Column() to define a column. the name of the column is the name that you assign it.
# primary keys are marked using the primary_key=True
# the type of column are passed in as the first argument inside the Column() eg String(), Integer, DateTime etc

class PeopleModel(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    phone_number = db.Column(db.String(45), nullable=False, unique=True)


    # create
    def create_record(self):
        db.session.add(self)
        db.session.commit()


    # db.Integer
    # db.Float
    # db.Boolean