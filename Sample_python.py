X=[]

with open('StudentsandCourses.FA18.09.06.18.csv', 'r') as infile:    
   for line in infile:
      # Split on comma first
      cols = [x.strip() for x in line.split(',')]

      # Grab 2nd "column"
      col2 = cols[0]

      # Split on spaces
      words = [x.strip() for x in col2.split(' ')]
      for word in words:     
         if word not in X:
            X.append(word)

for w in X:
   print w