from app import db

class PetsModel(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)


    # creating a record
    def create_record(self):
        db.session.add()
        db.session.commit()

    # db.Integer
    # db.Float
    # db.Boolean