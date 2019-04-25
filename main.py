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
#note 3: Text input becomes keyword2. Make user open file 1, move to find_course_name
#Variables: keyword2, filename.
#note5: After finishing find_course_name, go to find_csv_number2
#Variables: list_need2




def find_csv_number2():
    global filename2
    filename2 = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
    #print(filename2)
    if filename2 != None:
        print (filename2)#"I got %d bytes from this file." % len(filename)
        find_course_times(filename2)
        create_table()
#note6: Make the user open file 2, jump to find_course_times
#Variables: list_need2, filename2
#note 9: After finishing find_course_times, go to create_table.
#Variables: big_array, total_array



def create_table():
    for j in range(columns):
        for i in range(rows):
            var = total_array[i][j]
            #sprint(var)
            this_label = Label(frame, text=var)
            this_label.grid(row=j,column=i)

    reset_data()

    button2 = Button(frame, text="Clear", command=callback2)
    button2.grid(row=3, column = 9)

#note 10: Use big_array to create a grid. Make a new button, Clear. On click, go to callback2.
#Variables: None


def callback2():
    for widget in frame.winfo_children():
        widget.destroy()
#note 11: Make the entire screen blank.
#Variables: None
    

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
        X = []
        word_list = []
        list_need = []
        list_need2 = []
        temp_list = []
        temp_string = ""
        marker = 0
        dict_time = []
        num_students = 0
        subjects = []
        course_number = []
        section_number = []
        meeting_times = []
        days_string = ""
        start_string = ""
        end_string = ""
        days_array = []
        start_array = []
        end_array = []
        start_conversion = []
        end_conversion = []
        temp_conversion = 0
        find_csv_number1()
    #note 2: Move to find_csv_number1
    #Variables: text input
    
    global text_entry
    text_entry = Entry(frame)
    text_entry.grid(row = 1, column = 8)

    text_entry.focus_set()

    button = Button(frame, text="Enter", command=callback)
    button.grid(row=3, column = 8)

    root.mainloop()
    #note 1: Create canvas with textbar and button. On click, move to callback.
    #Variables: text input