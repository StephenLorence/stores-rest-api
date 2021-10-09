from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel', backref='items')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "store_id": self.store_id
            }

    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.query.filter_by(name=name).first()
        except:
            return {"message": "An error occurred finding the item."}, 500
    
    @classmethod
    def find_all(cls):
        try:
            return cls.query.all()
        except:
            return {"message": "An error occurred finding the item."}, 500

    def save_to_db(self):
        try:
           db.session.add(self)
           db.session.commit()
        except:
            return {"message": "An error occurred inserting the item."}, 500

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return {"message": "An error occurred deleting the item."}, 500