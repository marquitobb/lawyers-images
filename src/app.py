import os
from flask import Flask, jsonify, request
from lawyer_image.controller import LawyersImages
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

PROJECT = "lawyers-images"
VERSION = "v1"
PATH_API = f"/api/{VERSION}/{PROJECT}"

@app.route('/welcome')
def index():
    return "Bienvenido a mi API"

@app.route(f'{PATH_API}', methods=['POST'])
def upload_image():
    data = request.get_json()
    # images_lawyers = LawyersImages().get_connection()
    # data = {"images": images_lawyers, "status": "success"}
    response_data = LawyersImages().save_image(lawyer_id=data["id_lawyer"], image_file=data["image_base"])
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')

