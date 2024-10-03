import tkinter
from tkinter import *
from tkinter import ttk 
from assetPath import relative_to_assets
import tkinter as tk
from styles import *

#TODO -- Design TaskFrames - Better Working Scrolls - Connect to Database

class todo_Task(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width=1125, height=700)
        self.place(width=1125, height=700, x=75)

        self.todo_task()

#---------------------------------------------------------------------------------#
    def todo_task(self):

#---Images------------------------------------------------------------------------------#
    #---Search Button Background---#
        self.icon_btn_add_task= PhotoImage(
            file=relative_to_assets("btn_add_task.png"))

        self.place(width=1125, height=700, x=75)
    #---Background Photo---#
        self.frame_bg=PhotoImage(
            file=relative_to_assets("frame_todo.png"))
    #---Complete Icon Photo---#        
        complete_icon = PhotoImage(
            file=relative_to_assets("delete_icon_small.png"))

#---Image Placements------------------------------------------------------------------------------#
    #---Background Image Placement---#
        bg_image=tkinter.Label(
            self,
            image=self.frame_bg, 
            background="#26294b")
        bg_image.place(relheight=1,relwidth=1)

#---Entry------------------------------------------------------------------------------#
    #---Task Entry---#
        self.task_entry=Entry(
            self, 
            width=399, 
            font=font1, 
            fg="white", 
            background="#181933", 
            borderwidth=0,)
        self.task_entry.pack(pady=(132,0), padx=(380,395))

#---Buttons------------------------------------------------------------------------------#
    #---Search Button---#  
        self.add_task=Button(
            self, 
            image=self.icon_btn_add_task, 
            borderwidth=0,
            background="#26294b", 
            activebackground="#26294b", 
            text="Add Task", 
            fg="white", 
            font=font1, 
            command=lambda: add_task())
        self.add_task.pack(pady=(30,0))

#---Tasks Canvas------------------------------------------------------------------------------#
    #---Scrollable Canvas---#
        self.canvas = tk.Canvas(self, bg="#0d1525", height=400, width=300, highlightthickness=0, background="#181933")
        self.canvas.place(x=405, y=235)
        #self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind_all('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

     #---Scrollbar---#
        #self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.scrollbar.place(x=705, y=235, height=400)

    #---Task Frames in Canvas---#
        task_container = tk.Frame(self.canvas, bg="#181933")
        self.canvas.create_window((0, 0), window=task_container, anchor="nw")

#---Functions------------------------------------------------------------------------------#
     #---Add Task---#
        def add_task(task=None):
            if not task:
                task = self.task_entry.get()
            if task:
                task_frame = tk.Frame(task_container, bg="#1d2332", pady=5)
                #task_number = len(task_container.winfo_children()) + 1
                task_label = tk.Label(task_frame, text=task, bg="#1d2332", fg="#ffffff")
                task_label.pack(side=tk.LEFT, padx=10)

                delete_button = tk.Button(task_frame, image=complete_icon, command=lambda: delete_task(task_frame), bg="#ff6347", fg="#e0194b", font=("Helvetica", 12))
                delete_button.pack(side=tk.RIGHT, padx=5)

                task_frame.pack(fill=tk.X, pady=5)
                self.task_entry.delete(0, tk.END)
                self.canvas.update_idletasks()
                self.canvas.configure(scrollregion=self.canvas.bbox("all")) 

    #---Delete Task---#
        def delete_task(task_frame):
            task_frame.destroy()



