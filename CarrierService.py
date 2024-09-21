import re
import tkinter as ttk
from FedExStatus import FedExStatus
from UPSStatus import UPSStatus
from variables import *


class CarrierService():
    def __init__(self):
        super().__init__()

        self.determine_carrier()

#---------------------------------------------------------------------------------#
    def determine_carrier(self):
     #---Pull Tracking Number---#       
        self.trackingNum = ShipmentsDict[0]
        service = None

#---Functions------------------------------------------------------------------------------#
        usps_pattern = [
                "^(94|93|92|94|95)[0-9]{20}$",
                "^(94|93|92|94|95)[0-9]{22}$",
                "^(70|14|23|03)[0-9]{14}$",
                "^(M0|82)[0-9]{8}$",
                "^([A-Z]{2})[0-9]{9}([A-Z]{2})$"
            ]
        ups_pattern = [
                "^(1Z)[0-9A-Z]{16}$",
                "^(T)+[0-9A-Z]{10}$",
                "^[0-9]{9}$",
                "^[0-9]{26}$"
            ]        
        fedex_pattern = [
                "^[0-9]{20}$",
                "^[0-9]{15}$",
                "^[0-9]{12}$",
                "^[0-9]{22}$"
            ]
    #---Tracking Number Pattern Matching---#            
        usps = "(" + ")|(".join(usps_pattern) + ")"
        fedex = "(" + ")|(".join(fedex_pattern) + ")"
        ups = "(" + ")|(".join(ups_pattern) + ")"
            
        if re.match(usps, self.trackingNum) != None:
                service = "USPS"
        elif re.match(ups, self.trackingNum) != None:
                service = "UPS"
        elif re.match(fedex, self.trackingNum) != None:
                service = "FedEx"
       
    #---Results of Pattern Matching---#    
        if service == 'FedEx':
            ShipmentCarrierDict.update({0:service}), FedExStatus()

        if service == 'UPS':
            ShipmentCarrierDict.update({0:service}), UPSStatus()

        if service == 'USPS':
            ShipmentCarrierDict.update({0:service}), ShipmentStatusDict.update({0:"USPS Not Available"})
        
        if service == None:
            pass
        