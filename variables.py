# List and Dictionaries for Software

#---Dictionary of Tracking Numbers---#
ShipmentsDict = {}
ShipmentsDict[0] = ""

#---Dictionary of Carrier---#
ShipmentCarrierDict = {}
ShipmentCarrierDict[0] = ""

#---Dictionary of Stauts---#
ShipmentStatusDict = {}
ShipmentStatusDict[0] = ""

#---List of In Transit Statuses---#
InTransitList = ["In Transit", 
                 "Delivered", 
                 "Ready for Pickup", 
                 "Held for Pickup", 
                 "Awaiting Customer Pickup"]

#---List of No Movement Statuses---#
NoMovementList = ["Label Created", 
                 "Cancelled", 
                 "No Status", 
                 "Voided Pickup", 
                 "Tracking Not Found.",
                 "No Record"]

#---List of Warning Statuses---#
WarningList = ["Delivery Exceptions",
                "Shipping Exceptions",
                "Clearance Delays",
                "In Clearance",
                "Exception",
                "Held in Warehouse",
                "Delivery Change",
                "Future Delivery",
                "Future Delivery Requested",
                "First Attempt",
                "Second Attempt",
                "Final Attempt",
                "Address Change",
                "Exception: Action Required",
                "Delay",
                "Return to Sender",
                "Action Required",
                "Information Required",
                "Rescheduled Delivery",
                "Upgrade Request",
                "Damage Reported",
                "Delivery Attempted",
                "Delivery Refused",
                "Pickup Attempted",
                "Lost and Found",
                "Package Not Claimed"]

#---Dictionary of FedEx Statuses---#
FedExStatusId = {
            '"statusByLocale": "In transit",' : 'In Transit',
            '"statusByLocale": "Delivered",' : 'Delivered', 
            '"statusByLocale": "Picked up",' : 'Delivered',
            '"statusByLocale": "Ready for pickup",' : 'Ready for Pickup',
            '"statusByLocale": "Initiated",' : 'Label Created',
            '"statusByLocale": "Clearance Delay",' : 'Clearance Delays',
            '"statusByLocale": "Delivery exception",' : 'Delivery Exceptions',
            '"statusByLocale": "Shipment exception",' : 'Shipping Exceptions',
            '"statusByLocale": "Cancelled",' : 'Cancelled',
            '"statusByLocale":"Ready for pickup",' : "No Record"}

#Dicitonary of UPS Statuses
UPSStatusId = {
            "'statusCode': '000'" : 'No Status',
            "'statusCode': '003'" : 'Label Created',
            "'statusCode': '005'" : 'In Transit',
            "'statusCode': '006'" : 'Out for Delivery',
            "'statusCode': '007'" : 'Voided',
            "'statusCode': '010'" : 'In Transit',
            "'statusCode': '011'" : 'Delivered',
            "'statusCode': '012'" : 'In Clearance',
            "'statusCode': '013'" : 'Exception',
            "'statusCode': '014'" : 'In Transit',
            "'statusCode': '016'" : 'Held in Warehouse',
            "'statusCode': '017'" : 'Held for Pickup',
            "'statusCode': '018'" : 'Delivery Change',
            "'statusCode': '019'" : 'Future Delivery',
            "'statusCode': '020'" : 'Future Delivery Requested',
            "'statusCode': '021'" : 'Out for Delivery',
            "'statusCode': '022'" : 'First Attempt',
            "'statusCode': '023'" : 'Second Attempt',
            "'statusCode': '024'" : 'Final Attempt',
            "'statusCode': '025'" : 'In Transit',
            "'statusCode': '026'" : 'Delivered',
            "'statusCode': '027'" : 'Address Change',
            "'statusCode': '028'" : 'Address Change',
            "'statusCode': '029'" : 'Exception: Action Required',
            "'statusCode': '030'" : 'Exception',
            "'statusCode': '032'" : 'Delay',
            "'statusCode': '033'" : 'Return to Sender',
            "'statusCode': '034'" : 'Return to Sender',
            "'statusCode': '035'" : 'Return to Sender',
            "'statusCode': '036'" : 'Return to Sender',
            "'statusCode': '037'" : 'Return to Sender',
            "'statusCode': '038'" : 'Delivered',
            "'statusCode': '039'" : 'In Transit',
            "'statusCode': '040'" : 'Awaiting Customer Pickup',
            "'statusCode': '041'" : 'Service Upgrade',
            "'statusCode': '042'" : 'Service Upgrade',
            "'statusCode': '043'" : 'Voided Pickup',
            "'statusCode': '044'" : 'In Transit',
            "'statusCode': '045'" : 'In Transit',
            "'statusCode': '046'" : 'Delay',
            "'statusCode': '047'" : 'Delay',
            "'statusCode': '048'" : 'Delay',
            "'statusCode': '049'" : 'Action Required',
            "'statusCode': '050'" : 'Information Required',
            "'statusCode': '051'" : 'Delay',
            "'statusCode': '052'" : 'Delay',
            "'statusCode': '053'" : 'Delay',
            "'statusCode': '054'" : 'Delivery Change',
            "'statusCode': '055'" : 'Rescheduled Delivery',
            "'statusCode': '056'" : 'Upgrade Request',
            "'statusCode': '057'" : 'In Transit',
            "'statusCode': '058'" : 'Information Required',
            "'statusCode': '059'" : 'Damage Reported',
            "'statusCode': '060'" : 'Delivery Attempted',
            "'statusCode': '061'" : 'Delivery Attempted',
            "'statusCode': '062'" : 'Delivery Attempted',
            "'statusCode': '063'" : 'Delivery Change',
            "'statusCode': '064'" : 'Delivery Refused',
            "'statusCode': '065'" : 'Pickup Attempted',
            "'statusCode': '066'" : 'Delivery Attempted',
            "'statusCode': '067'" : 'Return to Sender',
            "'statusCode': '068'" : 'Lost and Found',
            "'statusCode': '069'" : 'Package Not Claimed',
            "'message': 'Tracking Information Not Found'": 'Tracking Not Found.'}


