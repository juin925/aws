from flask import Flask, request, render_template, redirect, jsonify
import runfile as rf
import subprocess

results = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    img = []
    global results
    num = request.form['message4']
    num = int(num)
    for i in range(1, 4):
        data = request.form[f'message{i}']
        img.append(data)
    
    results = rf.yolo(img, num)
    img = []
    return redirect('/results')

@app.route('/results', methods = ['POST', 'GET'])
def results():
    global results
    return results

@app.route('/getData', methods = ['POST', 'GET'])
def getData():
    data = request.get_json()

    return data

@app.route('/returnData', methods = ['POST'])
def returnData():
    url = 'http://192.168.219.102:5000'
    global results
    data = jsonify(results)
    response = request.post(url, data=data)
    print(response.text)
    return redirect('/getData')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)


