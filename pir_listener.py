from gpiozero import MotionSensor
from apis import ApiRequest
from camera_recorder import CameraRecorder
import threading
import time

class PIRListener(object):
    
    def wait_for_motion(self):
        pir = MotionSensor(17)
        print("MotionSensor")
        camera_recorder = CameraRecorder()
        api = ApiRequest()

        while True:
            print("wait for motion")
            pir.wait_for_motion()
            print("current_thread: " + threading.current_thread().name+ " Motion Detected")
            api.sendPushNotification()
            availability = api.checkAvailability()
            if availability == 0:
                api.startRecording()
            pir.wait_for_no_motion()
            print("current_thread: " + threading.current_thread().name + " Motion Stopped")
            time.sleep(50)
        
    def listen(self):
        t1 = threading.Thread(target=self.wait_for_motion)
        t1.start()
    
    
    