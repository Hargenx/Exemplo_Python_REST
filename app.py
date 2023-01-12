from flask import Flask, jsonify, request

app = Flask(__name__)

items = [{'name': 'Item 1'}, {'name': 'Item 2'}]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

@app.route('/items', methods=['POST'])
def create_item():
    item = {'name': request.json['name']}
    items.append(item)
    return jsonify({'item': item}), 201

@app.route('/items/<string:name>', methods=['PUT'])
def update_item(name):
    item = next(filter(lambda x: x['name'] == name, items), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item.update(request.json)
    return jsonify({'item': item})

@app.route('/items/<string:name>', methods=['DELETE'])
def delete_item(name):
    global items
    items = list(filter(lambda x: x['name'] != name, items))
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
