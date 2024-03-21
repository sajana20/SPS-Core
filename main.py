#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, send_file
from camera import VideoCamera
from camera_recorder import CameraRecorder
import os
from ultrasonic_listener import UltraSonicListener
from pir_listener import PIRListener


pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),mimetype='multipart/x-mixed-replace; boundary=frame')
 
# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"

@app.route('/record')
def take_record():
    pi_camera.__del__()
    pi_recorder = CameraRecorder()
    pi_recorder.record()
    return "None"

@app.route('/downloadVideo/<file_name>')
def download(file_name):
    print("called download")
    path = "./footage/"+file_name
    return send_file(path, as_attachment=True)



if __name__ == '__main__':
    print('start')

    app.run(host='0.0.0.0', debug=False)
    UltraSonicListener().listen()
    PIRListener().listen()
