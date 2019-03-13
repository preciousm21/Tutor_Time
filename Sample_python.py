from Tkinter import *
import Tkinter as tkinter 
import csv
import sys
from collections import defaultdict



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

columns = defaultdict(list) # each value in each column is appended to a list

with open('CourseList.FA18.09.06.18.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
subjects = []
course_number = []
meeting_times = []
for i in columns['Subject']:
   subjects.append(i)
for i in columns['Course Number']:
   course_number.append(i)
for i in columns['Meeting Times']:
   meeting_times.append(i)

for i in list_need2:
   for j in range(0,len(subjects)):
      if subjects[j] in i and course_number[j] in i:
         print (meeting_times[j])

#msg = tkinter.Message(root, text=list_need2)
#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
#msg.pack()
tkinter.mainloop()
