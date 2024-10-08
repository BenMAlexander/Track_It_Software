import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter import *
from CarrierService import CarrierService
from assetPath import relative_to_assets
from styles import *
from variables import *

'''Frame1 Class is the GUI section for the Shipment Tracking
   Section of this sofware.'''

class Frame1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
    #---Switch Between Frames---#
        self.controller = controller

#---Assets------------------------------------------------------------------------------#
    #---Background Image---#
        self.frame_bg=PhotoImage(
            file=relative_to_assets("frame_single_bg.png"))
    #---Single Track Icon---#
        self.single_track_icon = PhotoImage(
            file=relative_to_assets("single_track_icon.png"))
    #---Multi Track Icon---#
        self.multi_track_icon = PhotoImage(
            file=relative_to_assets("multi_track_icon.png"))
    #---To Do Task Icon---#
        self.todo_task_icon = PhotoImage(
            file=relative_to_assets("todo_task_icon.png"))
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
        
#---Background------------------------------------------------------------------------------#
    #---Background Color Placement---#
        bg_color=tkinter.Label(
            self,
            background="#26294b")
        bg_color.place(width=1200, height=700)

    #---Background Image Placement---#
        bg_image=tkinter.Label(
            self,
            image=self.frame_bg, 
            background="#26294b")
        bg_image.place(width=1125, height=700, x=75)

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

    
#---Buttons------------------------------------------------------------------------------#
    #---Single Track Button---#
        sTrackBtn = Button(
            self, 
            text="Go to Frame 2",
            image=self.single_track_icon, 
            borderwidth=0, 
            background="#26294b", 
            activebackground="#26294b",
            command=None)
        sTrackBtn.pack(pady=(60,0), padx=(5,0), anchor="w")

    #---Multi Track Button---#
        toDoBtn = Button(
            self, 
            text="Go to Frame 2",
            image=self.todo_task_icon, 
            borderwidth=0, 
            background="#26294b", 
            activebackground="#26294b", 
            command=self.show_frame_2)
        toDoBtn.pack(pady=(60,0), padx=(5,0), anchor="w")

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
        self.btn_search.place(anchor="n", x=632, y=195)

#---Entry------------------------------------------------------------------------------#
    #---Tracking Number Variable---#
        self.trackingNum = tk.StringVar()
    #---Single Track Entry---#
        self.search_entry=Entry(
            self, 
            textvariable=self.trackingNum,
            width=38, 
            font=font1, 
            fg="white", 
            background="#181933", 
            borderwidth=0,)
        self.search_entry.place(anchor="n", x=635, y=133)

#---Labels & Results------------------------------------------------------------------------------#
    #---Tracking Label---#        
        tracking_label=tkinter.Label(
            self, 
            text="Tracking", 
            fg="white", 
            font=font3, 
            background="#222543")
        tracking_label.place(anchor="n", x=635, y=407)

    #---Tracking Result---#        
        self.tracking_results=Entry(
            self, 
            justify=CENTER, 
            width=17, 
            fg="white", 
            font=font2, 
            borderwidth=0,
            background="#15162d")
        self.tracking_results.place(anchor="n", x=635, y=431) 

        #---Carrier Label---#
        carrier_label=tkinter.Label(
            self, 
            text="Carrier", 
            fg="white", 
            font=font3, 
            background="#222543")
        carrier_label.place(anchor="n", x=635, y=451)

    #---Carrier Result---#
        self.carrier_results=Entry(
            self,
            justify=CENTER, 
            width=17, 
            fg="white", 
            font=font2, 
            borderwidth=0,
            background="#15162d")
        self.carrier_results.place(anchor="n", x=635, y=475)  

    #---Status Label---#
        status_label=tkinter.Label(
            self, 
            text="Status", 
            fg="white", 
            font=font3, 
            background="#222543")
        status_label.place(anchor="n", x=635, y=495)
        
    #---Status Result---#
        self.status_results=Entry(
            self, 
            justify=CENTER, 
            width=17, 
            fg="white", 
            font=font2, 
            borderwidth=0,
            background="#15162d")
        self.status_results.place(anchor="n", x=635, y=519)

#---Functions------------------------------------------------------------------------------#
    #---Icon Associated with Tracking Status---#
        def iconStatus():
            status = str(ShipmentStatusDict[0])
        #---In Transit (Check)---#
            transit = any(status in sublist for sublist in InTransitList)
            if transit == True:
                self.transitIcon.place(x=599, y=305)
        #---No Movement (X)---#
            noMove = any(status in sublist for sublist in NoMovementList)
            if noMove == True:
                self.noMovementIcon.place(x=599,y=305)
        #---Warning (Hazard)---#
            warning = any(status in sublist for sublist in WarningList)
            if warning == True:
                self.warningIcon.place(x=599,y=305)
    
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
    
    #---Show Frame 2---#
    def show_frame_2(self):
        self.pack_forget()  # Hide this frame
        self.controller.show_frame("Frame2")  # Show Frame 2