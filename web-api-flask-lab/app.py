from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Sample in-memory data
items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]


# GET endpoint to retrieve all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


# GET endpoint to retrieve an item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


# POST endpoint to create a new item
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.get_json()
    new_item["id"] = items[-1]["id"] + 1 if items else 1
    items.append(new_item)
    return jsonify(new_item), 201


if __name__ == "__main__":
    app.run(debug=False, port=5001)
