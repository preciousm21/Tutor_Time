from Tkinter import *
import Tkinter as tk 
import csv
import sys
from collections import defaultdict
import re
from array import *
from Sample_python import *




class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        
        find_course_name()

        msg = tk.Message(root, text=list_need2)
        msg.config(bg='lightgreen', font=('times', 12, 'italic'))
        msg.pack()

        find_course_times()
        #<create the rest of your GUI here>




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tutor Time")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()