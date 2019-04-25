from Tkinter import *
import Tkinter as tk 
import tkFileDialog
import csv
import sys
from collections import defaultdict
import re
from array import *
from Sample_python import *

filename = ''
filename2 = ''
keyword2 = 'MATH 340'
#int num = 1

#keyword = "MATH 340"

global keyword
keyword = "MATH 340"

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


def find_csv_number1():
    global filename
    global keyword2
    keyword2 = text_entry.get()
    if keyword2 != '':
        
        print(keyword2)
        filename = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
        #keyword2 = text_entry.get()
        print(type(filename))
    #print(filename)
        if filename != None:
            print (filename)#"I got %d bytes from this file." % len(filename)
            find_course_name(filename, keyword2)
            find_csv_number2()




def find_csv_number2():
    global filename2
    filename2 = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
    #print(filename2)
    if filename2 != None:
        print (filename2)#"I got %d bytes from this file." % len(filename)
        find_course_times(filename2)
        create_table()



def create_table():
    for j in range(columns):
        for i in range(rows):
            var = total_array[i][j]
            #sprint(var)
            this_label = Label(frame, text=var)
            this_label.grid(row=j,column=i)

    button2 = Button(frame, text="Clear", command=callback2)
    button2.grid(row=3, column = 9)
    

    

def callback2():
    for widget in frame.winfo_children():
        widget.destroy()
    
    
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tutor Time")
 
    canvas = Canvas(root, height=200) # a canvas in the parent object
    frame = Frame(canvas) # a frame in the canvas
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    
    
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    
    
    canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    
    
    frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    root.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    root.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    root.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))

    rows = 6

    columns = 57


    def callback():
        find_csv_number1()
    #note 2: Move to find_csv_number1
    
    global text_entry
    text_entry = Entry(frame)
    text_entry.grid(row = 1, column = 8)

    text_entry.focus_set()

    button = Button(frame, text="Enter", command=callback)
    button.grid(row=3, column = 8)

    


    root.mainloop()
    #note 1: Create canvas with textbar and button. On click, move to callback.