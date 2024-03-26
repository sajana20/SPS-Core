import RPi.GPIO as GPIO
import time

class UltrasonicSensor(object):
    def __init__(self, trig_pin, echo_pin):
        
        self.trig = trig_pin
        self.echo = echo_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, False)
       


    def get_distance(self):
        time.sleep(2)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)


        while GPIO.input(self.echo)==0:
            start_time = time.time()
        while GPIO.input(self.echo)==1:
            end_time = time.time()

        duration = end_time - start_time
        distance = duration * 17150
        distance = round(distance, 2)
        return distance

            
            
    
