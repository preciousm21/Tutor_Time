from Tkinter import *
import Tkinter as tk 
import tkFileDialog
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

        
        #find_course_name()
        #print("Test")
        #msg = tk.Message(root, text=list_need2)
        #msg.config(bg='lightgreen', font=('times', 12, 'italic'))
        #msg.pack()

        #find_course_times()
        #<create the rest of your GUI here>

def find_csv_number1():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        data = file.read()
        #msg = tk.Message(root, text=data)
        #msg.config(bg='red', font=('times', 12, 'italic'))
        #msg.pack()
        #file.close()
        print "I got %d bytes from this file." % len(data)




def find_csv_number2():
    file = tkFileDialog.askopenfile(parent=root2,mode='rb',title='Choose a file')
    if file != None:
        data2 = file.read()
        #msg2 = tk.Message(root2, text=data2)
        #msg2.config(bg='lightgreen', font=('times', 12, 'italic'))
        #msg2.pack()
        #file.close()
        print "I got %d bytes from this file." % len(data2)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tutor Time")
    root2 = tk.Tk()
    root2.title("Tutor Time 2")
    find_csv_number1()
    find_csv_number2()
    find_course_name()
    find_course_times()
    msg = tk.Message(root, text=list_need2)
    msg.config(bg='red', font=('times', 12, 'italic'))
    msg.pack()
    msg2 = tk.Message(root2, text=dict_time)
    msg2.config(bg='lightgreen', font=('times', 12, 'italic'))
    msg2.pack()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    root2.mainloop