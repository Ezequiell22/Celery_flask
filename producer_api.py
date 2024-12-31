from worker_tasks import task_x
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/stock', method=['POST'])
def stock():
  data = request.get_json()
  stock = data.get('stock_name')

  if not stock:
    return jsonify({'error' : "nome não encontrado"}), 200
  
  task_x.delay(stock)
  return jsonify({'message': 'processamento adicionado a fila com sucesso'}), 200

if __name__ == '__main__':
  app.run(debug=True)