from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found."}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"A store with name {name} already exists."}, 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": f"Store {name} deleted."}
        return {"message": f"No store with name {name} exists."}, 400


class StoreList(Resource):
    def get(self):
        stores = StoreModel.query.all()
        return {"stores": [store.json() for store in stores]}