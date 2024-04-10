import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ApiRequest():
    
    def setAvailability(self,availability):
        

        api_url = os.getenv('API_URL')+"/availability"
        data = {
            "user_id":0,
            "slot_id": os.getenv('SLOT_ID'),
            "availability": availability}
        response = requests.post(api_url, data=data)
        
    def setVideoFileName(self,file_name):

        api_url = os.getenv('API_URL')+"/footage"
        data = {"slot_id": os.getenv('SLOT_ID'),"file_name": file_name}
        response = requests.post(api_url, data=data)
        
    def startRecording(self):

        api_url = os.getenv('RASPBERRYPI_SEVICE_URL')+"/recording"
        response = requests.get(api_url)
        
    def checkAvailability(self):

        api_url = os.getenv('API_URL')+"/checkAvailability/"+ os.getenv('SLOT_ID')
        response = requests.get(api_url)
        print("responseAvail")
        print(response.json())
        return response.json()['availability']
        
    def sendPushNotification(self):
        
        api_url = os.getenv('API_URL')+"/pushNotification"
        data = {"slot_id": os.getenv('SLOT_ID'),"title": "Security Alert","message": "Please keep an eye on the live camera feed; as there appears to be suspicious activity occurring around your vehicle at the moment."}
        response = requests.post(api_url, data=data)
    
       
