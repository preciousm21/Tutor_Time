from Tkinter import *
import Tkinter as tkinter 
import csv

root = Tk()

X=[]
list_need = []
keyword = "MUS 326"

with open('StudentsandCourses.FA18.09.06.18.csv', 'r') as infile:    
   for line in infile:
      if keyword in line:
          list_need.append(line)
      
      # Split on comma first
      cols = [x.strip() for x in line.split(',')]

      # Grab 2nd "column"
      col2 = cols[0]

      # Split on spaces
      words = [x.strip() for x in col2.split(' ')]
      for word in words:     
         if word not in X:
            X.append(word)

<<<<<<< HEAD
for w in X:
   print (w)
=======
#for w in X:
#  print w

print(list_need)
msg = tkinter.Message(root, text=list_need)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
tkinter.mainloop()
>>>>>>> e39172b17bb38932486777508c7741292c3ebb9f
