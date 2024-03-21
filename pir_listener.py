from gpiozero import MotionSensor
from apis import ApiRequest
from camera_recorder import CameraRecorder

class PIRListener(object):
    
    def wait_for_motion(self):
        pir = MotionSensor(27)
        print("MotionSensor")
        camera_recorder = CameraRecorder()

        while True:
            print("hello")
            pir.wait_for_motion()
            print("Motion Detected")
            camera_recorder.record()
            pir.wait_for_no_motion()
            print("Motion Stopped")
        
    def listen(self):
        t1 = threading.Thread(target=wait_for_motion)
        t1.start()
    
    
    