from flask import Flask, render_template, Response, request, send_from_directory, send_file
from camera import VideoCamera
from camera_recorder import CameraRecorder
import os
from ultrasonic_listener import UltraSonicListener
from pir_listener import PIRListener
import threading


pi_camera = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    try:
        global pi_camera
        if pi_camera is not None:
            pi_camera.delete()
            pi_camera = None
        pi_camera = VideoCamera(flip=False)
        pi_camera.start()
        return Response(gen(pi_camera),mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        return "Camera already in use. Please try again later", 400
    
    
 

@app.route('/recording')
def take_record():
    global pi_camera
    if pi_camera is not None:
        pi_camera.delete()
        pi_camera = None
    
    pi_recorder = CameraRecorder()
    pi_recorder.record()
    return "None"

@app.route('/downloadVideo/<file_name>')
def download(file_name):
    path = "./footage/"+file_name
    return send_file(path, as_attachment=True)



if __name__ == '__main__':

    UltraSonicListener().listen()
    PIRListener().listen()
    app.run(host='0.0.0.0', debug=False)

