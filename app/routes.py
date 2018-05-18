from app import app
from flask import jsonify, request
import json

@app.route('/save_keyword', strict_slashes=False, methods=['GET', 'POST'])
def keyword():
    """
    Save the keyword to a file in a POST request
    Serve the keyword to a GET request
    """
    if request.method == 'POST':
        post_dict = request.get_json()
        with open('file.json', 'w') as f:
            json.dump(post_dict, f)

    if request.method == 'GET':
        with open('file.json') as f:
            data = json.load(f)
        return jsonify(data)
