import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from styles import *
from frame_single_track import Frame1
from frame_todo_list import Frame2

'''This is the main class of the app. The main class host the frames in the GUI. 
   This class also sets the intial frame for viewing when opened and diplays the frames'''

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Track_It! Shipment Tracking Services")
        self.geometry("1200x700")
        self.resizable(False, False)
        
#---Container for Frames---#
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        
#---Initialize Frames---#
        self.frames = {}
        self.frames["Frame1"] = Frame1(container, self)
        self.frames["Frame2"] = Frame2(container, self)
        
#---Initial Frame---#
        self.show_frame("Frame1")
    
#---Determine Frame---#
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.pack(fill="both", expand=True)
        for name, fr in self.frames.items():
            if name != frame_name:
                fr.pack_forget()

#---Start aApplication
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
