from Tkinter import *
import Tkinter as tkinter 
import csv
import sys
from collections import defaultdict
import re



root = Tk()
root.title("Tutor Time")



X=[]
word_list = []
list_need = []
list_need2 = []
keyword = "MATH 340"
temp_list = []
temp_string = ""
marker = 0
dict_time = []


class_time_dict = {
   "M 9:45AM": 0,
   "M 10:00AM": 0,
   "M 10:15AM": 0,
   "M 10:30AM": 0,
   "M 10:45AM": 0,
   "M 11:00AM": 0,
   "M 11:15AM": 0,
   "M 11:30AM": 0,
   "M 11:45AM": 0,
   "M 12:00PM": 0,
   "M 12:15PM": 0,
   "M 12:30PM": 0,
   "M 12:45PM": 0,
   "M 1:00PM": 0,
   "M 1:15PM": 0,
   "M 1:30PM": 0,
   "M 1:45PM": 0,
   "M 2:00PM": 0,
   "M 3:00PM": 0,
   "M 3:15PM": 0,
   "M 3:30PM": 0,
   "M 3:45PM": 0,
   "M 4:00PM": 0,
   "M 4:15PM": 0,
   "M 4:30PM": 0,
   "M 4:45PM": 0,
   "M 5:00PM": 0,
   "M 5:15PM": 0,
   "M 5:30PM": 0,
   "M 5:45PM": 0,
   "M 6:00PM": 0,
   "M 6:15PM": 0,
   "M 6:30PM": 0,
   "M 6:45PM": 0,
   "M 7:00PM": 0,
   "M 7:15PM": 0,
   "M 7:30PM": 0,
   "M 7:45PM": 0,
   "M 8:00PM": 0,
}


def find_course_name():
   global X
   global word_list 
   global list_need 
   global list_need2 
   global keyword 
   global temp_list 
   global temp_string 
   global marker  




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
          
      
      

#for w in X:
#  print w
def find_course_times():
   global marker
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
            dict_time.append(meeting_times[j])
            break


   days_string = ""
   start_string = ""
   end_string = ""
   days_array = []
   start_array = []
   end_array = []
   for i in dict_time:
      for j in i:
         if j.isdigit() == False and marker == 0:
            days_string += j
         elif j != "-" and marker <= 1:
            start_string += j
            marker = 1
         elif j == "-":
            marker = 2
         else:
            end_string += j   
      marker = 0
      days_array.append(days_string)
      start_array.append(start_string)
      end_array.append(end_string)
      days_string = ""
      start_string = ""
      end_string = ""



   print (days_array)
   print (start_array)
   print (end_array)


   #print (dict_time)


find_course_name()
find_course_times()
tkinter.mainloop()

#tkinter.mainloop()

#tkinter.mainloop()



#BUGS:
#only takes the first class without caring about sections
#Doesn't work for MAT* 330 cuz it doesnt appear for the spreadsheet
