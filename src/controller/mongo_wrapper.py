from pymongo import MongoClient
from . import config


class MongoWrapper:

    def __init__(self):
        self.client = MongoClient(config.DB_URL)
        self.db = self.client.stock

    def get_all_items(self):
        all_items_dict = {
            "all_items": list(self.db.items.find({}))
        }
        return all_items_dict

    def get_item_by_id(self, item_id):
        item = self.db.items.find_one({'_id': item_id})
        if item:
            return item
        return "Item Not Found"

    def create_item(self, item_dict):
        # check id not already exist
        if not self.db.items.find_one({'_id': item_dict["_id"]}):
            self.db.items.insert_one(item_dict)
            item = self.db.items.find_one({'_id': item_dict["_id"]})
            return item
        return "Error: ID provided already exist in DB"

    def delete_item_by_id(self, item_id):
        # check id exists in DB
        item_to_delete = self.db.items.find_one({'_id': item_id})
        if item_to_delete:
            self.db.items.delete_one({'_id': item_id})
            return item_to_delete
        return "ID provided not exist in DB"

    def increase_item_amount(self, item_id, amount):
        item_to_increase = self.db.items.find_one({'_id': item_id})
        if item_to_increase:
            self.db.items.update_one({'_id': item_id}, {'$inc': {'amount': amount}})
            increased_item = self.db.items.find_one({'_id': item_id})
            return increased_item
        return "Item ID does not exist in DB"

    def decrease_item_amount(self, item_id, amount):
        item_to_decrease = self.db.items.find_one({'_id': item_id})
        if item_to_decrease:
            self.db.items.update_one({'_id': item_id}, {'$inc': {'amount': -amount}})
            decreased_item = self.db.items.find_one({'_id': item_id})
            return decreased_item
        return "Item ID does not exist in DB"


