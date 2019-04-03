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

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        

        #scrollbar = Scrollbar(root, orient=VERTICAL)
        #crollbar2 = Scrollbar(root, orient=HORIZONTAL)


        




        #listbox = Listbox(root, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)
        #scrollbar.config(command=listbox.yview)
        #scrollbar2.config(command=listbox.xview)

    
        #scrollbar.pack(side=RIGHT, fill=Y)
        #scrollbar2.pack(side=RIGHT, fill=Y)

        #listbox.pack(fill=BOTH, expand=1)

        #listbox.insert(END, "\n")

    
 
        
        #for item in big_array:
        #    listbox.insert(END, item)
         #   listbox.insert(END, "\n")

    

# bind listbox to scrollbar
#listbox.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=listbox.yview)
#     #find_course_name()
    #print("Test")
    #msg = tk.Message(root, text=list_need2)
    #msg.config(bg='lightgreen', font=('times', 12, 'italic'))
    #msg.pack()

    #find_course_times()
    #<create the rest of your GUI here>

def find_csv_number1():
    global filename
    filename = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
    print(type(filename))
    #print(filename)
    if filename != None:
        #data = file.read()
        #msg = tk.Message(root, text=data)
        #msg.config(bg='red', font=('times', 12, 'italic'))
        #msg.pack()
        #file.close()
        print (filename)#"I got %d bytes from this file." % len(filename)
        find_course_name(filename)




def find_csv_number2():
    global filename2
    filename2 = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
    #print(filename2)
    if filename2 != None:
        #data = file.read()
        #msg = tk.Message(root, text=data)
        #msg.config(bg='red', font=('times', 12, 'italic'))
        #msg.pack()
        #file.close()
        print (filename2)#"I got %d bytes from this file." % len(filename)
        find_course_times(filename2)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tutor Time")

    find_csv_number1()
    find_csv_number2()
 
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


    for j in range(columns):
        for i in range(rows):
            var = total_array[i][j]
            #sprint(var)
            Label(frame, text=var).grid(row=j,column=i)
        for i in range(rows):
            var = big_array[i][j]
            

    root.mainloop()
    #root2.mainloop