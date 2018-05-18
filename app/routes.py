from flask import jsonify, request, Flask
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)


cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
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

if __name__ == "__main__":
    app.run('127.0.0.1', 5000)
