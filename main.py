from tkinter import *
import tkinter as tk
from singleTrack import singleTrack
from todo_Task import todo_Task
from menu import Menu

class TrackIt(tk.Tk):
    
    def __init__ (self):
        super().__init__()
        self.title("Track_It! Shipment Tracking Services")
        self.geometry("1200x700")
        self.resizable(False, False)

        self.menu = Menu(self)
        self.singletrack = singleTrack(self)
        #self.todo = todo_Task(self)

        self.mainloop()

TrackIt()