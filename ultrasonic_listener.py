import threading
from ultrasonic import UltrasonicSensor

class UltraSonicListener(object):
    
    def get_distance(self):
        ultrasonicSensor = UltrasonicSensor(27, 22)
        api = ApiRequest()

        available = 0

        while True:
            print("calledultra")
            distance = ultrasonicSensor.get_distance()


            if distance <= 100 and available == 1:
                

                api.setAvailability(0)
                available =0
                print("slot marked as unavailable. distance in cm = " + str(distance))
                
            elif distance > 100 and available == 0:
                api.setAvailability(1)
                available =1
                print("slot marked as available distance in cm = " + str(distance))
                
    def listen(self):
        t1 = threading.Thread(target=get_distance)
        t1.start()
            
                
                
