import tkinter as tk
import tkinter
from tkinter.ttk import *
from tkinter import *
from assetPath import relative_to_assets
from styles import *

'''The Frame2 Class is the GUI set up for the To Do Task
   section of the software.'''


class Frame2(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
    #---Switch Between Frames---#
        self.controller = controller

#---Assets------------------------------------------------------------------------------#
    #---Background Image---#
        self.frame_bg=PhotoImage(
            file=relative_to_assets("frame_todo.png"))
    #---Single Track Icon---#
        self.single_track_icon = PhotoImage(
            file=relative_to_assets("single_track_icon.png"))
    #---Multi Track Icon---#
        self.multi_track_icon = PhotoImage(
            file=relative_to_assets("multi_track_icon.png"))
    #---To Do Task Icon---#
        self.todo_task_icon = PhotoImage(
            file=relative_to_assets("todo_task_icon.png"))
    #---ToDo Task Photo---#        
        self.todo_Task_Bg = PhotoImage(
            file=relative_to_assets("todo_task_bg.png"))   
    #---Complete Task Photo---#        
        self.complete_task = PhotoImage(
            file=relative_to_assets("complete_icon_test_blue.png"))
    #---Search Button Background---#
        self.icon_btn_add_task= PhotoImage(
            file=relative_to_assets("btn_add_task.png"))   

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

    
#---Buttons------------------------------------------------------------------------------#
    #---Single Track Button---#
        sTrackBtn = Button(
            self, 
            text="Go to Frame 2",
            image=self.single_track_icon, 
            borderwidth=0, 
            background="#26294b", 
            activebackground="#26294b",
            command= self.show_frame_1)
        sTrackBtn.pack(pady=(60,0), padx=(5,0), anchor="w")

    #---ToDo List Button---#
        toDoBtn = Button(
            self, 
            text="Go to Frame 2",
            image=self.todo_task_icon, 
            borderwidth=0, 
            background="#26294b", 
            activebackground="#26294b",
            command=None)
        toDoBtn.pack(pady=(60,0), padx=(5,0), anchor="w")

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
        self.add_task.place(anchor="n", x=632, y=185)

#---Entry------------------------------------------------------------------------------#
    #---Single Track Entry---#
        self.task_entry=Entry(
            self, 
            width=38, 
            font=font1, 
            fg="white", 
            background="#181933", 
            borderwidth=0,)
        self.task_entry.place(anchor="n", x=635, y=133)

#---Scrollable Canvas for ToDo List------------------------------------------------------------------------------#
        self.canvas = tk.Canvas(
            self, 
            bg="#0d1525",
            width=300, 
            height=400,  
            highlightthickness=0, 
            background="#181933")
        self.canvas.place(x=473, y=235)

        #self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind_all('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

     #---Scrollbar---#
        self.scrollbar = tk.Scrollbar(
            self, 
            orient="vertical", 
            command=self.canvas.yview,
            troughcolor="#0d1525")
        self.scrollbar.place(x=775, y=235, height=400)

    #---Task Frames in Canvas---#
        task_container = tk.Frame(
            self.canvas, 
            bg="#181933", 
            width=350, 
            height=60)
        self.canvas.create_window((0, 0), window=task_container, anchor="nw")


#---Functions------------------------------------------------------------------------------#
    #---Add Task---#
        def add_task(task=None):
            if not task:
                task = self.task_entry.get()
            if task:
                task_frame = tk.Frame(
                    task_container, 
                    bg="#171833", 
                    pady=5, 
                    width=350, 
                    height=65)
                
        #---Task Frame Background---#    
                task_bg= tk.Label(
                    task_frame, 
                    image=self.todo_Task_Bg,  
                    bg="#171833")
                task_bg.place(x=0, y=0)

        #---Task Text---#
                task_label = tk.Label(
                    task_frame, 
                    text=task, 
                    fg="white", 
                    bg="#171833")
                task_label.place(x=75, y=18)

        #---Complete Button---#
                complete_button = tk.Button(
                    task_frame, 
                    image=self.complete_task, 
                    command=lambda: complete_task(task_frame), 
                    fg="#e0194b",
                    background="#212443", 
                    activebackground="#212443",
                    font=font1, 
                    relief=FLAT,
                    borderwidth=0)
                complete_button.place(x=19, y=17)

                task_frame.pack(fill=tk.X, pady=5)
                self.task_entry.delete(0, tk.END)
                self.canvas.update_idletasks()
                self.canvas.configure(scrollregion=self.canvas.bbox("all")) 

    #---Complete Task---#
        def complete_task(task_frame):
            task_frame.destroy()

#--Show Frame 1---#
    def show_frame_1(self):
        self.pack_forget()  
        self.controller.show_frame("Frame1") 
