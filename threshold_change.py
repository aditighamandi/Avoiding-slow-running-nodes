import sys
import csv 

dict={}
threshold=sys.argv[1]


file=open('threshold_change_data.csv','r')

reader=csv.reader(file)

for row in reader:
	dict[row[0]]=row[1]

list_value=sorted(dict.values())
if((len(list_value) % 2) == 0):
	median = list_value[len(list_value)/2]
else:
	median = list_value[(len(list_value)/2)+1]



def csv_label(task_id,label):
	import csv 
	import sys

	file = open('data.csv','r')
	name='data_with_threshold_{t}.csv'.format(t=threshold)
	file2 = csv.writer(open(name,"a"))

	reader=csv.reader(file)
	reader = list(reader)

	for row in reader:
		if (row[30] == task_id):		
			row[33]=label
			file2.writerow(row)
	return

for key_task_id,value in dict.items():
	if (value > (median*threshold)):
		csv_label(key_task_id,1)
	else:
		csv_label(key_task_id,0)
