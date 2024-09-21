from variables import *
import tkinter as tk 
import requests
import json

class UPSStatus():
    def __init__(self):
        super().__init__()

        self.ups_info()

#---------------------------------------------------------------------------------#
    def ups_info(self):
        id = ShipmentsDict[0]
        status=tk.StringVar()

    #---Authorization---#            
        client_ID = "stMSHwnTtORwszLqtuk75Psec68WFfxtYBHh6yPOyzaO4IRk" #Authorization
        client_Secret = "SDGDXnUXXb7E05vnhbNFACaUMg0Apb239FwTAMp3UGZ3zYGXP8Eb9srrG3e9EMj6"
        authURL = "https://wwwcie.ups.com/security/v1/oauth/token"

        payload = {"grant_type": "client_credentials"}
        headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-merchant-id": "G0478G"}

        AuthResponse = requests.post(authURL, data = payload, headers = headers, auth = (client_ID, client_Secret))
        AuthToken = json.loads(AuthResponse.text)["access_token"]

        url = "https://onlinetools.ups.com/api/track/v1/details/"+ id
        query = {
        "locale": "en_US",
        "returnSignature": "false"}
        headers = {
        "transId": "string",
        "transactionSrc": "testing",
        "Authorization": "Bearer " + AuthToken}

    #---Retrieve JSON Response---#            
        response = requests.get(url, headers = headers, params = query)
    #---Convert JSON to String---#            
        trackInfo = (str(response.json()))
        latestStatus = trackInfo[0 :900]

        
    #---Extract Status from JSON and Convert to Status to String---#            
        for key in list(UPSStatusId):
            if (key) in latestStatus:
                status = f'{UPSStatusId[key]}'
    #---Add Status to Dict---#            
                ShipmentStatusDict.update({0:status}) 
            