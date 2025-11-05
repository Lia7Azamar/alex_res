from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    json_path = 'comparison_results.json'

    if not os.path.exists(json_path):
        return "❌ No se encontró el archivo comparison_results.json. Genera primero los resultados.", 404

    with open(json_path, 'r', encoding='utf-8') as f:
        results = json.load(f)

    return render_template('comparacion.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
