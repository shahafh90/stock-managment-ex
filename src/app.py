from flask import Flask, request, jsonify
from controller.mongo_wrapper import MongoWrapper

app = Flask(__name__)
mongo = MongoWrapper()  # Singleton ?


@app.route("/")
def hello_stock_app():
    return "Hello Stock App"


@app.route("/all-items")
def get_all_items():
    return jsonify(mongo.get_all_items())


@app.route("/item/<item_id>")
def get_item_by_id(item_id):
    return jsonify(mongo.get_item_by_id(item_id))


@app.route('/create-item', methods=['GET', 'POST'])
def create_item():
    # TDL: check validity of input json with jsonschema. (or some mongo mapping restriction). for now assume valid json.
    return jsonify(mongo.create_item(request.json))


@app.route("/item/delete/<item_id>")
def delete_item_by_id(item_id):
    return jsonify(mongo.delete_item_by_id(item_id))


@app.route('/item/inc-amount/<item_id>', methods=['GET', 'POST'])
def increase_item_amount(item_id):
    amount = request.json["amount"]
    return jsonify(mongo.increase_item_amount(item_id, amount))


@app.route('/item/dec-amount/<item_id>', methods=['GET', 'POST'])
def decrease_item_amount(item_id):
    amount = request.json["amount"]
    return jsonify(mongo.decrease_item_amount(item_id, amount))


if __name__ == "__main__":
    app.run()
