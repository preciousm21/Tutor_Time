from Tkinter import *
import Tkinter as tkinter 
import csv
import ttk

from ttk import *

#class App(Tk.frame):
 #  def __init__(self, master):
  #    self.master=master
   #   frame = Frame(master)
    #  frame.pack()

      # open file
      with open('CourseList2.FA18.09.06.18.csv', "rb") as file:
         reader = csv.reader(file)

         # r and c tell us where to grid the labels
         r = 0
         for col in reader:
            c = 0
         for row in col:
               # i've added some styling
            label = tkinter.Label(root, width = 10, height = 2, \
                                    text = row, relief = tkinter.RIDGE,)
            label.grid(row = r, column = c)
            if c == 2:
               ClassLabel = ""
            if c == 3:
               ClassLabel += row
            if c == 4:
               ClassLabel += row
      #           print (ClassLabel)
            c += 1
            r += 1


with open('StudentsandCourses2.FA18.09.06.18.csv', "rb") as file:
    reader = csv.reader(file)
    ClassLabel = "MUS 326"
    ImportantClasses = []
    class_dict = {}

   # r and c tell us where to grid the labels
    r = 0
    for col in reader:
      c = 0
      for row in col:
         if c == 0:
            # i've added some styling
           label = tkinter.Label(root, width = 10, height = 2, \
                                  text = row, relief = tkinter.RIDGE,)
           #label.grid(row = r, column = c)
           if c == 0:
              if ClassLabel in row:
                 ImportantClasses.append(row)
           c += 1
      r += 1
print (ImportantClasses)

#run main loop
#def main(): 
 #   root = Tk()
  #  App = Demo1(root)
   # root.title("Tutor Time")
    #root.mainloop()

#if __name__ == '__main__':
  #  main()


