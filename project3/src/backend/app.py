# to start the venv: $ source project3_env/Scripts/activate
# to start flask server: flask run
# to start next.js: npm run dev
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/index", methods=["POST"])
def index():
    req = request.get_json()
    print(req)
    response = {"message": "Data received successfully", "data": req}
    return jsonify(response), 200
