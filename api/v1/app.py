#!/usr/bin/python3
"""starting an api"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from os import getenv
from flask_cors import CORS


"""declaring the method"""
app = Flask(__name__)

"""Registering the blueprint"""
app.register_blueprint(app_views)

"""Creates a CORS instance"""
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """Closes the session"""
    storage.close()


@app.errorhandler(404)
def errorhandler(error):
    """handles errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    API_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    API_PORT = getenv("HBNB_API_PORT", 5000)
    app.run(host=API_HOST, port=API_PORT, threaded=True)
