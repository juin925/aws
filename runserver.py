from flask import Flask, request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename
import runfile as rf
import subprocess
import os
import dload

results = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST']) 
def upload_file(): 
    img_address = []
    img = []
    num1 = request.form['message4'] # 이미지 주소 몇개 받았는지
    for i in range(1, int(num1) + 1) :
        img_address.append(request.form[f'message{i}'])

    if request.method == 'POST':
        for i in range(1, int(num1) + 1):
            dload.save(img_address[i-1], f"yolo_image{i}.jpg")

    num2 = request.form['message5'] # 사람수가 몇명인지
    print(num2)
    for i in range(1, int(num1) + 1):
        name = f'yolo_image{i}.jpg'
        img.append(name)
    print(img)
    results = rf.yolo(img, num2)
    results = img_address[results]
    img_address = []
    img = []
    for i in range(1, int(num1) + 1):
        os.remove(f'yolo_image{i}.jpg')
    return redirect('127.0.0.1:5000/returnData')

@app.route('/getData', methods = ['POST', 'GET'])
def getData():
    data = request.get_json()

    return data

@app.route('/returnData', methods = ['POST'])
def returnData():
    url = '127.0.0.1:5000'
    global results
    data = {
        'img' : f'{results}'
    }
    response = request.post(url, data=data)
    print(response.text)
    return redirect('127.0.0.1:5000/getData')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)


