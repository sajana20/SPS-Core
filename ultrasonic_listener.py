import threading
import time
from ultrasonic import UltrasonicSensor
from apis import ApiRequest

class UltraSonicListener():
    
    distance_threshold = 50
    
    def get_distance(self):
        ultrasonicSensor = UltrasonicSensor(27, 22)
        api = ApiRequest()

        available = 0

        while True:
            
            distance = ultrasonicSensor.get_distance()
            if distance <= self.distance_threshold:
                available = 0
                print("current_thread: " + threading.current_thread().name + ". slot marked as unavailable. distance in cm = " + str(distance))
                
            elif distance > self.distance_threshold and available == 0:
                
                api.setAvailability(1)
                available = 1
                print("current_thread: " + threading.current_thread().name + ". slot marked as available distance in cm = " + str(distance))
                
            else:
                print("current_thread: " + threading.current_thread().name + " else " + str(distance) + " : " + str(available))
                
                
            time.sleep(10)
                
    def listen(self):
        
        t1 = threading.Thread(target=self.get_distance)
        t1.start()
            
                
                
