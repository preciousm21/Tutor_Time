from Tkinter import *
import Tkinter as tkinter 
import csv
import sys

root = Tk()



X=[]
word_list = []
list_need = []
list_need2 = []
keyword = "MATH 340"
temp_list = []
temp_string = ""
marker = 0

with open('StudentsandCourses.FA18.09.06.18.csv', 'r') as infile:    
   for line in infile:
      if marker == 1:
         if "Total For" not in line:
            list_need.append(line)
         else:
            marker = 0
      if keyword in line:
         for i in range (len(temp_list)):
            list_need.append(temp_list[i])
         list_need.append(line)
         marker = 1
      if "Course Subj/Number" in line:
         temp_list[:] = []
      if "Course Subj/Number" not in line:
         temp_list.append(line)
          
      
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

for i in list_need:
   for j in i:
      if j != "-":
         temp_string += j
      else:
         list_need2.append(temp_string)
         temp_string = ""
         break


msg = tkinter.Message(root, text=list_need2)
msg.config(bg='lightgreen', font=('times', 12, 'italic'))
msg.pack()
tkinter.mainloop()