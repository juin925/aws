from werkzeug.utils import secure_filename
from flask_cors import CORS
import runfile as rf
import subprocess
import os
import dload
import json

results = ''

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.is_json)
    data = request.get_json()
    photo_list = data['photoList']
    len_photo = len(photo_list)

    print(photo_list)
    results = rf.yolo(photo_list, int(data['num']))
    results = photo_list[results]

    print(jsonify(results))
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)