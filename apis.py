import requests

class ApiRequest():
    
    def setAvailability(self,availability):

        api_url = "https://4e9f-112-134-153-239.ngrok-free.app/availability"
        data = {
            "slot_id": 1,
            "availability": availability}
        response = requests.post(api_url, json=data)
        
    def setVideoFileName(self,file_name):

        api_url = "https://a89a-112-134-157-97.ngrok-free.app/footage"
        data = {"slot_id": 1,"file_name": file_name}
        response = requests.post(api_url, data=data)
       
