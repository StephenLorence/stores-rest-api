from sqlalchemy.orm import backref
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # items = db.relationship('ItemModel', backref='store')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "id": self.id, "items": [{
                                                                "id": item.id,
                                                                "name": item.name,
                                                                "price": item.price
                                                            } for item in self.items]}

    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.query.filter_by(name=name).first()
        except:
            return {"message": "An error occurred finding the store."}, 500

    @classmethod
    def find_all(cls):
        try:
            return cls.query.all()
        except:
            return {"message": "An error occurred finding the store."}, 500

    def save_to_db(self):
        try:
           db.session.add(self)
           db.session.commit()
        except:
            return {"message": "An error occurred inserting the store."}, 500

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return {"message": "An error occurred deleting the store."}, 500