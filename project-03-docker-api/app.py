from flask import Flask, jsonify, request

app = Flask(__name__)

items = {}
next_id = 1

@app.route("/items", methods=["POST"])
def create_item():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    item = {"id": next_id, "name": data["name"], "description": data.get("description", "")}
    items[next_id] = item
    next_id += 1
    return jsonify(item), 201

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": list(items.values()), "total": len(items)})

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    deleted = items.pop(item_id)
    return jsonify({"message": f"Item {item_id} deleted", "item": deleted})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
