from flask import Flask, request, jsonify, Response, json

from .services import retrieve_item, create_item

app = Flask(__name__)

datos = []
@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello World!'})

# POST <BASE_URL>/api/orders/computers
@app.route('/api/orders/computers', methods=['POST'])
def ordersComputers():
    header_value = request.headers.get('header_demo', None)
    param_value = request.args.get('param_demo', None)
    body_value = request.data.decode('UTF-8')
    obj = json.loads(body_value)
    global datos
    datos.append(obj)
    return {
        "order_id": "1",
        "created_by": obj['created_by'],
        "status": obj['status'],
        "created_at": obj['created_at'],
        "equipment": obj['equipment']
    }
@app.route('/api/orders/computers', methods=['GET'])
def getOrdersComputers():
    return datos

@app.route('/demo/<path_demo>', methods=['POST'])
def demo(path_demo=None):
    # Showcase different ways in which data can be passed
    path_value = path_demo
    header_value = request.headers.get('header_demo', None)
    param_value = request.args.get('param_demo', None)
    body_value = request.data.decode('UTF-8')
    return {
        'result': {
            'path': path_value,
            'header': header_value,
            'param': param_value,
            'body': str(body_value),
        }
    }


@app.route('/api/items/<item_id>', methods=['GET', 'POST'])
def pets(item_id):
    if request.method == 'GET':
        return Response(json.dumps(retrieve_item(item_id)), 200, {'Content-Type': 'application/json'})
    elif request.method == 'POST':
        request_body = request.json
        return Response(json.dumps(create_item(item_id, request_body)))
    else:
        raise Exception('Unsupported HTTP request type.')

if __name__ == '__main__':
    app.run()
