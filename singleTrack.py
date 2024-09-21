import tkinter
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from variables import *
from CarrierService import CarrierService
from assetPath import relative_to_assets
from styles import *
import todo_Task




class singleTrack(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width=1125, height=700)
        self.place(width=1125, height=700, x=75)

        self.create_widgets()

#---------------------------------------------------------------------------------#
    def create_widgets(self):
        self.place(width=1125, height=700, x=75)
        todo_Task.Frame.place_forget

#---Images------------------------------------------------------------------------------#
    #---Background Image---#
        self.frame_bg=PhotoImage(
            file=relative_to_assets("frame_single_bg.png"))
    #---Search Button Background---#
        self.icon_btn_search= PhotoImage(
            file=relative_to_assets("btn_search.png"))
    #---In Transit Icon (Check)---#    
        self.in_transit_icon= PhotoImage(
            file=relative_to_assets("in_transit_icon.png"))
    #---No Movement Icon (X)---#
        self.no_movement_icon= PhotoImage(
            file=relative_to_assets("no_movement_icon.png"))
    #---Warning Icon (Hazard)---#    
        self.warning_icon= PhotoImage(
            file=relative_to_assets("warning_icon.png"))
        
#---Image Placements------------------------------------------------------------------------------#
    #---Background Image Placement---#
        bg_image=tkinter.Label(
            self,
            image=self.frame_bg, 
            background="#26294b")
        bg_image.place(relheight=1,relwidth=1)
    #---In Transit Icon (Check) Placement---#    
        self.transitIcon=tkinter.Label(
            self, 
            image=self.in_transit_icon,
            background="#212443")
    #---No Movement Icon (X) Placement---#
        self.noMovementIcon=tkinter.Label(
            self, 
            image=self.no_movement_icon,
            background="#212443")
    #---Warning Icon (Hazard) Placement---#    
        self.warningIcon=tkinter.Label(
            self, 
            image=self.warning_icon,
            background="#212443")

#---Entry------------------------------------------------------------------------------#
    #---Tracking Number Variable---#
        self.trackingNum = tk.StringVar()
    #---Single Track Entry---#
        self.search_entry=Entry(
            self, 
            textvariable=self.trackingNum,
            width=399, 
            font=font1, 
            fg="white", 
            background="#181933", 
            borderwidth=0,)
        self.search_entry.pack(pady=(132,0), padx=(380,395))

#---Buttons------------------------------------------------------------------------------#
    #---Search Button---#  
        self.btn_search=Button(
            self, 
            image=self.icon_btn_search, 
            borderwidth=0,
            background="#26294b", 
            activebackground="#26294b", 
            text="Search", 
            fg="white", 
            font=font1, 
            command=lambda: (buttonpress()))
        self.btn_search.pack(pady=(30,0))

#---Labels & Results------------------------------------------------------------------------------#
    #---Tracking Label---#        
        tracking_label=tkinter.Label(
            self, 
            text="Tracking", 
            fg="white", 
            font=font3, 
            background="#222543")
        tracking_label.pack(pady=(189,0))
    #---Tracking Result---#        
        self.tracking_results=Entry(
            self, 
            justify=CENTER, 
            width=17, 
            fg="white", 
            font=font2, 
            borderwidth=0,
            background="#15162d")
        self.tracking_results.pack(pady=(5,0)) 

    #---Carrier Label---#
        carrier_label=tkinter.Label(
            self, 
            text="Carrier", 
            fg="white", 
            font=font3, 
            background="#222543")
        carrier_label.pack(pady=(3,0))
    #---Carrier Result---#
        self.carrier_results=Entry(
            self,
            justify=CENTER, 
            width=17, 
            fg="white", 
            font=font2, 
            borderwidth=0,
            background="#15162d")
        self.carrier_results.pack(pady=(2,0))   

    #---Status Label---#
        status_label=tkinter.Label(
            self, 
            text="Status", 
            fg="white", 
            font=font3, 
            background="#222543")
        status_label.pack(pady=(4,0))
    #---Status Result---#
        self.status_results=Entry(
            self, 
            justify=CENTER, 
            width=17, 
            fg="white", 
            font=font2, 
            borderwidth=0,
            background="#15162d")
        self.status_results.pack(pady=(2,0))

#---Functions------------------------------------------------------------------------------#
    #---Icon Associated with Tracking Status---#
        def iconStatus():
            status = str(ShipmentStatusDict[0])
        #---In Transit (Check)---#
            transit = any(status in sublist for sublist in InTransitList)
            if transit == True:
                self.transitIcon.place(x=523, y=305)
        #---No Movement (X)---#
            noMove = any(status in sublist for sublist in NoMovementList)
            if noMove == True:
                self.noMovementIcon.place(x=523,y=305)
        #---Warning (Hazard)---#
            warning = any(status in sublist for sublist in WarningList)
            if warning == True:
                self.warningIcon.place(x=523,y=305)
    
    #---Clear Entry after Searching---#
        def clearEntry():
            ShipmentsDict.update({0:""})
            ShipmentCarrierDict.update({0:""})
            ShipmentStatusDict.update({0:""})
            self.tracking_results.delete(0, "end")
            self.carrier_results.delete(0, "end")
            self.status_results.delete(0, "end")

    #---Reseting Status Icons---#
        def forget():
            self.transitIcon.place_forget()
            self.noMovementIcon.place_forget()
            self.warningIcon.place_forget()
        
        #---Search Button---#
            #---Adds Entry into Dict---#
        def buttonpress():
            forget(),
            clearEntry(),
            ShipmentsDict.update({0:self.trackingNum.get()}),  
            CarrierService(), 
            self.search_entry.delete(0, "end"), 
            self.tracking_results.insert(tk.END, ShipmentsDict[0]),
            self.carrier_results.insert(tk.END, ShipmentCarrierDict[0]),
            self.status_results.insert(tk.END, ShipmentStatusDict[0]),
            iconStatus()


    
