from Tkinter import *
import Tkinter as tk 
import csv
import sys
from collections import defaultdict
import re
from array import *
from main import *





big_array = [["", "7:45AM", "8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", \
   "9:45AM", "10:00AM", "10:15AM", "10:30AM", "10:45AM", "11:00AM", "11:15AM", "11:30AM", "11:45AM", \
   "12:00PM", "12:15PM", "12:30PM", "12:45PM", "1:00PM", "1:15PM", "1:30PM", "1:45PM", "2:00PM", \
   "2:15PM", "2:30PM", "2:45PM", "3:00PM", "3:15PM", "3:30PM", "3:45PM", "4:00PM", "4:15PM", "4:30PM", \
   "4:45PM", "5:00PM", "5:15PM", "5:30PM", "5:45PM", "6:00PM", "6:15PM", "6:30PM", "6:45PM", "7:00PM",\
   "7:15PM", "7:30PM", "7:45PM", "8:00PM", "8:15PM", "8:30PM", "8:45PM", "9:00PM", "9:15PM", "9:30PM"], \
   ["Mon", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ["Tues", 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ["Wed", 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ["Thurs", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ["Fri", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
   0, 0, 0, 0, 0, 0, ]]





#root = Tk()
#root.title("Tutor Time")




X=[]
word_list = []
list_need = []
list_need2 = []
keyword = "MATH 340"
temp_list = []
temp_string = ""
marker = 0
dict_time = []




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

   
   # msg = tk.Message(root, text=list_need2)
   #msg.config(bg='lightgreen', font=('times', 12, 'italic'))
   #msg.pack()
          
      
      

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



   #print (days_array)
   #print (start_array)
   #print (end_array)

   start_conversion = []
   end_conversion = []
   temp_conversion = 0

   for i in start_array:
      if "12:" in i:
         temp_conversion += 720
      elif "11:" in i:
         temp_conversion += 660
      elif "10:" in i:
         temp_conversion += 600
      elif "9:" in i:
         temp_conversion += 540
      elif "8:" in i:
         temp_conversion += 480
      elif "7:" in i:
         temp_conversion += 420
      elif "6:" in i:
         temp_conversion += 360
      elif "5:" in i:
         temp_conversion += 300
      elif "4:" in i:
         temp_conversion += 240
      elif "3:" in i:
         temp_conversion += 180
      elif "2:" in i:
         temp_conversion += 120
      elif "1:" in i:
         temp_conversion += 60
      if ":05" in i:
         temp_conversion += 5
      if ":10" in i:
         temp_conversion += 10
      if ":15" in i:
         temp_conversion += 15
      if ":20" in i:
         temp_conversion += 20
      if ":25" in i:
         temp_conversion += 25
      if ":30" in i:
         temp_conversion += 30
      if ":35" in i:
         temp_conversion += 35
      if ":40" in i:
         temp_conversion += 40
      if ":45" in i:
         temp_conversion += 45
      if ":50" in i:
         temp_conversion += 50
      if ":55" in i:
         temp_conversion += 55
      if "PM" in i and "12:" not in i:
         temp_conversion += 720
      start_conversion.append(temp_conversion)
      temp_conversion = 0

   for i in end_array:
      if "12:" in i:
         temp_conversion += 720
      elif "11:" in i:
         temp_conversion += 660
      elif "10:" in i:
         temp_conversion += 600
      elif "9:" in i:
         temp_conversion += 540
      elif "8:" in i:
         temp_conversion += 480
      elif "7:" in i:
         temp_conversion += 420
      elif "6:" in i:
         temp_conversion += 360
      elif "5:" in i:
         temp_conversion += 300
      elif "4:" in i:
         temp_conversion += 240
      elif "3:" in i:
         temp_conversion += 180
      elif "2:" in i:
         temp_conversion += 120
      elif "1:" in i:
         temp_conversion += 60
      if ":05" in i:
         temp_conversion += 5
      if ":10" in i:
         temp_conversion += 10
      if ":15" in i:
         temp_conversion += 15
      if ":20" in i:
         temp_conversion += 20
      if ":25" in i:
         temp_conversion += 25
      if ":30" in i:
         temp_conversion += 30
      if ":35" in i:
         temp_conversion += 35
      if ":40" in i:
         temp_conversion += 40
      if ":45" in i:
         temp_conversion += 45
      if ":50" in i:
         temp_conversion += 50
      if ":55" in i:
         temp_conversion += 55
      if "PM" in i and "12:" not in i:
         temp_conversion += 720
      end_conversion.append(temp_conversion)
      temp_conversion = 0

      



   #print (dict_time)
#find_course_name()
#find_course_times()

#class Application(Frame):
#  def __init__(self, master= None):
#     self.master=master
#       frame = Frame(master)
#frame.pack()
# msg = tkinter.Message(root, text=list_need2)
# msg.config(bg='lightgreen', font=('times', 12, 'italic'))
# msg.pack()
   #def open_file():
   #  result = filedialog.askopenfile(intialdir="/", title="select file", filetypes=("test files", ".csv")
      #print (result) 
      #for c in result:
      #print(c) 
   #button = Button(root, text= "open file", command=open_file)
   #root.geometry ("300x300")
   #root.title("Tutor Time")
   #app = Application()
   #app.mainloop
   
   #tkinter.mainloop()
#root = Tk()
#root.title("Tutor Time")
#find_course_name()
#find_course_times()
#tk.mainloop()




#def main(): 
#app = Application()
#root.title("Tutor Time")
#find_course_name()
#find_course_times()
#app.mainloop()
#if __name__ == '__main__':
#   main()


#BUGS:
#only takes the first class without caring about sections
#Doesn't work for MAT* 330 cuz it doesnt appear for the spreadsheet
