import csv

def read_csv():
    with open('CourseList.FA18.09.06.18.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print ' '.join(row)

