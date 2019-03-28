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

        find_csv_number1()
        find_csv_number2()

        listbox = Listbox(root)
        listbox.pack(fill=BOTH, expand=TRUE)

        listbox.insert(END, "\n")
        
        for item in big_array:
            listbox.insert(END, item)
            listbox.insert(END, "\n")

    #scrollbar = Scrollbar(root)
    #scrollbar.pack(side=RIGHT, fill=Y)

    #listbox = Listbox(root)
    #listbox.pack()

    #for i in range(100):
    #    listbox.insert(END, i)

# bind listbox to scrollbar
#listbox.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=listbox.yview)

    
<<<<<<< HEAD
  

    #widgets for top toolbar 
#def createWidgets(self):
 #   top = self.winfo_toplevel()
 #   self.menuBar = Menu(top)
  #  top["menu"] = self.menuBar
   # self.subMenu = Menu(self.menuBar)
    #self.menuBar.add_cascade(label = "File", menu = self.subMenu)   
=======


    
 
>>>>>>> 152b267922bf3309f179ef5ac9b3aa1317631aed
        
    #find_course_name()
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
   


    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    #root2.mainloop