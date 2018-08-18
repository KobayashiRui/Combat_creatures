#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response,request

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_opencv import Camera

key_code_dict = {65:'A',87:'W',83:'S',68:'D',37:'←',38:'↑',39:'→',40:'↓'}

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print("post")
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/controler.html',methods=['GET','POST'])
def controler():
    if request.method == 'POST':
        print("post")
        key = int(request.form['text'])
        print(key)
        if key in key_code_dict.keys():
            key_data = key_code_dict[key]
        else:
            key_data = "key_code over dictrange"
        print(key_data)
    else:
        key_data = "not_key"

    """Video streaming home page."""
    return render_template('controler.html',key_data = key_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,threaded=True)
