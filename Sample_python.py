from Tkinter import *
import Tkinter as tkinter 
import csv
import sys

root = Tk()



X=[]
word_list = []
list_need = []
keyword = "MATH 340"
marker = 0

with open('StudentsandCourses.FA18.09.06.18.csv', 'r') as infile:    
   for line in infile:
      if marker == 1:
         if "Total For" not in line:
            list_need.append(line)
         else:
            marker = 0
      if keyword in line:
          list_need.append(line)
          marker = 1
          
      
      # Split on comma first
      cols = [x.strip() for x in line.split(',')]

      # Grab 2nd "column"
      col2 = cols[0]

      # Split on spaces
      words = [x.strip() for x in col2.split(' ')]
      for word in words:     
        if word not in X:
            X.append(word)

#for w in X:
#  print w

print(list_need)
msg = tkinter.Message(root, text=list_need)
msg.config(bg='lightgreen', font=('times', 12, 'italic'))
msg.pack()
tkinter.mainloop()