import picamera
import os
from apis import ApiRequest
from datetime import datetime
import subprocess

class CameraRecorder(object):

    def record(self):
        print("hello")
        with picamera.PiCamera() as camera:
            api = ApiRequest()
            now = datetime.now()
            file_name = (str(now)[:19]).replace(" ", "_").replace("-", "_").replace(":", "_") +"_video.h264"
            footage_path = "./footage/"
            camera.resolution = (640, 480)
            camera.start_recording(footage_path+ file_name)
            camera.wait_recording(60)
            camera.stop_recording()
            
            mp4_conversion_command = "MP4Box -add "+ footage_path + file_name + " "+footage_path + file_name.replace(".h264", ".mp4")
            print(mp4_conversion_command)
            subprocess.run([mp4_conversion_command], shell=True)
#             os.rename(str(now)[:19]+"_video.h264", str(now)[:19]+"_video.mp4")
            api.setVideoFileName(file_name.replace(".h264", ".mp4"))

            
            camera.close()