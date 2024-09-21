import json
import requests 
import tkinter as tk 
from variables import *

class FedExStatus():
   def __init__(self):
        super().__init__()

        self.fedex_info()

#---------------------------------------------------------------------------------#
   def fedex_info(self):
        id = ShipmentsDict[0]
        status=tk.StringVar()
#TODO -- Add this to server to grab---------------------------------------------------------------------------------#
    #---Authorization---#            
        secretKey = "34beb5df32e246fb8e143a990495a3b6" 
        publicKey = "l7807fd372290045a6b50466423b3a7b14"
    
    #---Sandbox for FedEx - Not Live - Ref- Tracking Numbers---#                    
        authURL = "https://apis-sandbox.fedex.com/oauth/token" 

        authKeys = {
            "client_id": publicKey,
            "client_secret": secretKey,
            "grant_type": "client_credentials"}
        
        AuthResponse = requests.request("POST",url=authURL,data=authKeys)
        AuthToken = json.loads(AuthResponse.text)["access_token"]

        TrackURL = "https://apis-sandbox.fedex.com/track/v1/trackingnumbers"
        TrackHeader = {
            "content-type": "application/json",
            "authorization": "Bearer "+ AuthToken}
        TrackBody = {
            "includeDetailedScans": False, 
            "trackingInfo": [{"trackingNumberInfo": {"trackingNumber":id}}]}
        
    #---Retrieve JSON Response---#            
        trackingResponse = requests.request("POST",url = TrackURL,data = json.dumps(TrackBody), headers = TrackHeader)
    #---Convert JSON to String---#            
        trackInfo = (str(trackingResponse.text))
 
    #---Extract Status from JSON and Convert to Status to String---#            
        for key in list(FedExStatusId):
            if key in trackInfo:
                status = f'{FedExStatusId[key]}'
    #---Add Status to Dict---#            
        ShipmentStatusDict.update({0:status})                
         