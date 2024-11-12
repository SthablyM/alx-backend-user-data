#!/usr/bin/env python3
"""Error handler: Unauthorized"""
from flask import Blueprint, abort

index_blueprint = Blueprint('index', __name__)

# Define the unauthorized endpoint
@index_blueprint.route('/unauthorized', methods=['GET'])
def unauthorized():
    """the unauthorized endpoint"""
    abort(401)
