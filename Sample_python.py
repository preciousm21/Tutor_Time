from Tkinter import *
import Tkinter as tk 
import csv
import sys
from collections import defaultdict
import re
from array import *
from Tkinter import *
import Tkinter as tk 
import tkFileDialog
import csv
import sys
import os
from collections import defaultdict
import re
from array import *


filename = ''
filename2 = ''
keyword2 = 'MATH 340'
#int num = 1

#keyword = "MATH 340"

global keyword
keyword = "MATH 340"





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


X=[]
word_list = []
list_need = []
list_need2 = []
#argumentList = sys.argv 
#keyword = sys.argv[1] + " " + sys.argv[2]
temp_list = []
temp_string = ""
marker = 0
dict_time = []
num_students = 0
total_array = [["", "7:45AM", "8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", \
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


def find_course_name(f_n1, ky22):
   
   global X
   global word_list 
   global list_need 
   global list_need2 
   #global keyword
   global temp_list 
   global temp_string 
   global marker  
   global num_students
   global total_array

   



   with open(f_n1, 'r') as infile:    
      for line in infile:
         if marker == 1:
            if "Total For" not in line:
               list_need.append(line)
            else:
               marker = 0
         if ky22 in line:
            for i in range (len(temp_list)):
               list_need.append(temp_list[i])
            list_need.append(line)
            marker = 1
            num_students += 1
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

   for i in list_need:
      for j in i:
         if j == ",":
               list_need2.append(temp_string)
               temp_string = ""
               break
         else:
            temp_string += j
   #note 4: Open the first file and use it and the keyword to create list_need2, then go back into find_csv_number1
   #Variables: keyword2, list_need2
   

def find_course_times(f_n2):
   global marker
   columns = defaultdict(list) # each value in each column is appended to a list

   with open(f_n2) as f:
      reader = csv.DictReader(f) # read rows into a dictionary format
      for row in reader: # read a row as {column1: value1, column2: value2,...}
         for (k,v) in row.items(): # go over each column name and value 
               columns[k].append(v) # append the value into the appropriate list
                                    # based on column name k
   global subjects
   global course_number
   global section_number
   global meeting_times
   
   subjects = []
   course_number = []
   section_number = []
   meeting_times = []
   for i in columns['Subject']:
      subjects.append(i)
   for i in columns['Course Number']:
      course_number.append(i)
   for i in columns['Section Number']:
      section_number.append(i)
   for i in columns['Meeting Times']:
      meeting_times.append(i)

   for i in list_need2:
      for j in range(0,len(subjects)):
         if (subjects[j] + " " + course_number[j] + " - " + section_number[j]) in i:
            dict_time.append(meeting_times[j])
            break
   
   convert_times()
#note 7: Open file 2, harvest subject, course number, section number, and meeting times.
#Compare that stuff to list_need2 to get dict_time.
#Variables: list_need2, dict_time

def convert_times():

   marker = 0
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
      #Break the stuff from dict_time into days, start time, and end time

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
   #Convert both start and end times to actual numbers.
   
   for i in range(0,len(start_array)):
      if "M" in days_array[i]:
         for j in range((start_conversion[i] - 450) / 15, ((end_conversion[i] - 450) / 15) +1):
            big_array[1][j] += 1
      if "T" in days_array[i]:
         for j in range((start_conversion[i] - 450) / 15, ((end_conversion[i] - 450) / 15) + 1):
            big_array[2][j] += 1
      if "W" in days_array[i]:
         for j in range((start_conversion[i] - 450) / 15, ((end_conversion[i] - 450) / 15) + 1):
            big_array[3][j] += 1
      if "R" in days_array[i]:
         for j in range((start_conversion[i] - 450) / 15, ((end_conversion[i] - 450) / 15) + 1):
            big_array[4][j] += 1
      if "F" in days_array[i]:
         for j in range((start_conversion[i] - 450) / 15, ((end_conversion[i] - 450) / 15) + 1):
            big_array[5][j] += 1
   #Increment big_array based on the start and end times.
         
   

   for i in range(0,6):
      for j in range(0, len(big_array[i])):
         if isinstance(big_array[i][j], int):
            total_array[i][j] = (str(big_array[i][j]) + " (" + str(big_array[i][j] * 100 / num_students) + "%) ")
         else:
            total_array[i][j] = (big_array[i][j])
   #Create total_array, which is basically big_array except with percentages.

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
print (big_array)
#note 8: Use the information in dict_time to create big_array and total array, then go back into find_csv_number2.
#Variable: big_array, total_array

def reset_data():
   X = []
   word_list = []
   list_need = []
   list_need2 = []
   temp_list = []
   temp_string = ""
   marker = 0
   dict_time = []
   num_students = 0
   subjects = []
   course_number = []
   section_number = []
   meeting_times = []
   days_string = ""
   start_string = ""
   end_string = ""
   days_array = []
   start_array = []
   end_array = []
   start_conversion = []
   end_conversion = []
   temp_conversion = 0
   



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

   total_array = [["", "7:45AM", "8:00AM", "8:15AM", "8:30AM", "8:45AM", "9:00AM", "9:15AM", "9:30AM", \
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

   print ("Data Reset")

   print (X)
   print (word_list)
   print (list_need)
   print (list_need2)
   print (temp_list)
   print (temp_string)
   print (marker)
   print (dict_time)
   print (num_students)
   print (subjects)
   print (course_number)
   print (section_number)
   print (meeting_times)
   print (days_string)
   print (start_string)
   print (end_string)
   print (days_array)
   print (start_array)
   print (end_array)
   print (start_conversion)
   print (end_conversion)
   print (temp_conversion)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


def find_csv_number1():
    global filename
    global keyword2
    keyword2 = text_entry.get()
    if keyword2 != '':
        
        print(keyword2)
        filename = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
        #keyword2 = text_entry.get()
        print(type(filename))
    #print(filename)
        if filename != None:
            print (filename)#"I got %d bytes from this file." % len(filename)
            find_course_name(filename, keyword2)
            find_csv_number2()
#note 3: Text input becomes keyword2. Make user open file 1, move to find_course_name
#Variables: keyword2, filename.
#note5: After finishing find_course_name, go to find_csv_number2
#Variables: list_need2




def find_csv_number2():
    global filename2
    filename2 = tkFileDialog.askopenfilename(filetypes=[("csv files","*.csv")])
    #print(filename2)
    if filename2 != None:
        print (filename2)#"I got %d bytes from this file." % len(filename)
        find_course_times(filename2)
        create_table()
#note6: Make the user open file 2, jump to find_course_times
#Variables: list_need2, filename2
#note 9: After finishing find_course_times, go to create_table.
#Variables: big_array, total_array



def create_table():
    for j in range(columns):
        for i in range(rows):
            var = total_array[i][j]
            #sprint(var)
            this_label = Label(frame, text=var)
            this_label.grid(row=j,column=i)

    reset_data()

    button2 = Button(frame, text="Clear", command=callback2)
    button2.grid(row=3, column = 9)
    

#note 10: Use big_array to create a grid. Make a new button, Clear. On click, go to callback2.
#Variables: None


def callback2():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tutor Time")
 
    canvas = Canvas(root, height=200) # a canvas in the parent object
    frame = Frame(canvas) # a frame in the canvas
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    
    
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    
    
    canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    
    
    frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    root.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    root.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    root.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))

    rows = 6

    columns = 57


def callback():
    X = []
    word_list = []
    list_need = []
    list_need2 = []
    temp_list = []
    temp_string = ""
    marker = 0
    dict_time = []
    num_students = 0
    subjects = []
    course_number = []
    section_number = []
    meeting_times = []
    days_string = ""
    start_string = ""
    end_string = ""
    days_array = []
    start_array = []
    end_array = []
    start_conversion = []
    end_conversion = []
    temp_conversion = 0
    find_csv_number1()
#note 2: Move to find_csv_number1
#Variables: text input
    
global text_entry
text_entry = Entry(frame)
text_entry.grid(row = 1, column = 8)

text_entry.focus_set()

button = Button(frame, text="Enter", command=callback)
button.grid(row=3, column = 8)

    


root.mainloop()
#note 1: Create canvas with textbar and button. On click, move to callback.
#Variables: text input