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
        #tframe=tk.Frame(self)
        #yscrollcommand=tk.Scrollbar(tframe, orient=VERTICAL)
        #tree.tk.Treeview(tframe)
        #yScrollbar.config(command=tree.yview)
        #tree.config(yscrollcommand=yscrollbar.set)

        #buildtree(tree, colHeadings, itemList)

        #tree.pack(side="left", fill="y")
        #yscrollbar.pack(side="right", fill="y")
        #tframe.pack(side="top", fill="y", expand=1, padx=10, pady=10)
        

  
    
    #widgets for top toolbar 
#def createWidgets(self):
    #top = self.winfo_toplevel()
    #self.menuBar = Menu(top)
    #top["menu"] = self.menuBar
    #self.subMenu = Menu(self.menuBar)
    #self.menuBar.add_cascade(label = "File", menu = self.subMenu)   

    #scrollbar = Scrollbar(root)
    #scrollbar.pack(side=RIGHT, fill=Y)

    #listbox = Listbox(root)
    #listbox.pack()

    #for i in range(100):
    #    listbox.insert(END, i)

# bind listbox to scrollbar
#listbox.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=listbox.yview)

    


    
 
        
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
    #scrollbar = Scrollbar(root)
    #scrollbar.pack( side = RIGHT, fill = Y )
    #root2 = tk.Tk()
    #root2.title("Tutor Time 2")
    find_csv_number1()
    find_csv_number2()
    #find_course_name()
    #find_course_times()
    for item in big_array:

        msg = tk.Button(root, text=big_array, command = lambda x=big_array:printtext(x))
        msg.config(bg='white', font=('times', 12, 'italic'))
        msg.pack()
    #msg2 = tk.Message(root2, text=dict_time)
    #msg2.config(bg='lightgreen', font=('times', 12, 'italic'))
    #msg2.pack()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.geometry("800x500")
    root.mainloop()
    #root2.mainloop