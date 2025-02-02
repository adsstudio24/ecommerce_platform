from flask import Flask, request, jsonify

app = Flask(__name__)

products = [{"id": 1, "name": "Ноутбук", "price": 1000}, {"id": 2, "name": "Смартфон", "price": 700}]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
