#!/usr/bin/env python3
"""Error handler: Unauthorized"""
from flask import Flask, jsonify
from api.v1.views.index import index_blueprint  # Make sure you import the blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint, url_prefix='/api/v1')


@app.errorhandler(401)
def unauthorized_error(error):
    """Error handler for 401 Unauthorized"""
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run()

