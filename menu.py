from assetPath import relative_to_assets
import tkinter
from tkinter import *
from tkinter import ttk 
import singleTrack
import todo_Task


#TODO -- Get Frames to show and disappear with button presses---------------------------------------------------------------------------------#
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width=75, height=700)
        self.place(width=75, height=700, x=0)
        #self.pack_propagate(False)
        #self.pack(side="left")

        self.create_menu()

    def create_menu(self):

#---Assets------------------------------------------------------------------------------#
        #---Single Track Icon---#
        self.single_track_icon = PhotoImage(
            file=relative_to_assets("single_track_icon.png"))
        #---Multi Track Icon---#
        self.multi_track_icon = PhotoImage(
            file=relative_to_assets("multi_track_icon.png"))
        #---To Do Task Icon---#
        self.todo_task_icon = PhotoImage(
            file=relative_to_assets("todo_task_icon.png"))

#---Background------------------------------------------------------------------------------#
        bg_color=tkinter.Label(
            self,
            background="#26294b")
        bg_color.place(relheight=1,relwidth=1)

#---Buttons------------------------------------------------------------------------------#
        #---Single Track Button---#        
        btn_single_track= Button(
            self,
            image=self.single_track_icon, 
            borderwidth=0, 
            background="#26294b", 
            activebackground="#26294b", 
            command=lambda: print("Single Track Button") )
        btn_single_track.pack(pady=(94,0))

        #---Multi Track Button---#        
        btn_multi_track= Button(
            self,
            image=self.multi_track_icon, 
            borderwidth=0, 
            background="#26294b", 
            activebackground="#26294b",  
            command=lambda:print("multi button"))
        btn_multi_track.pack(pady=(60,0))

        #---To Do Task Button---#        
        self.btn_todo_task= Button(
            self,
            image=self.todo_task_icon, 
            borderwidth=0, background="#26294b", 
            activebackground="#26294b", 
            width=60, height=60, 
            command=lambda: print("ToDo Task Button"))
        self.btn_todo_task.pack(pady=(60,0))

