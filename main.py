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
<<<<<<< HEAD
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
=======
>>>>>>> a52ded2be9870b1d7675d13e4fb3071ef1ce919b

        find_csv_number1()
        find_csv_number2()

        listbox = Listbox(root)
        listbox.pack(fill=BOTH, expand=TRUE)

        listbox.insert(END, "\n")

        for item in big_array:
            listbox.insert(END, item)
            listbox.insert(END, "\n")
    
  

    #widgets for top toolbar 
def createWidgets(self):
    top = self.winfo_toplevel()
    self.menuBar = Menu(top)
    top["menu"] = self.menuBar
    self.subMenu = Menu(self.menuBar)
    self.menuBar.add_cascade(label = "File", menu = self.subMenu)   
        
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
    root.geometry("800x500")
    root.mainloop()
    #root2.mainloop