
import csv 
import sys

file = open('data.csv','r')
file2 = csv.writer(open('data_labelled.csv',"a"))

reader=csv.reader(file)
reader = list(reader)

for row in reader:
	if (row[30] == sys.argv[1]):		
		row[33]=sys.argv[2]
		file2.writerow(row)
	




