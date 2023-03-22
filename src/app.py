import os
from flask import Flask, jsonify
from lawyer_image.controller import LawyersImages
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/')
def index():
    return "Bienvenido a mi API"

@app.route('/connection')
def api():
    images_lawyers = LawyersImages.get_connection()
    data = {"images": images_lawyers, "status": "success"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

