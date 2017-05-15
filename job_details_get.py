from xml.dom import minidom
import os
import csv

os.system('sudo rm -r jobs.xml')
url='http://ankit21:19888/ws/v1/history/mapreduce/jobs'
cmd='curl --compressed -H "Accept: application/xml" -X GET "{url}" >> /home/ankit/rrd-xml/jobs.xml'.format(url=url)
os.system(cmd)

doc = minidom.parse("jobs.xml")
dict ={}
node_list=[]
jobs=doc.getElementsByTagName("job")
for job in jobs:
	id=job.getElementsByTagName("id")[0]
	name=job.getElementsByTagName("name")[0]

	id_data=id.firstChild.data
	name_data=name.firstChild.data
	""" 
	Make sure to get task.xml before this.

	"""

	os.system('sudo rm -r task.xml')
	url='http://ankit21:19888/ws/v1/history/mapreduce/jobs/{id_data}/tasks'.format(id_data=id_data)
	cmd='curl --compressed -H "Accept: application/xml" -X GET "{url}" >> /home/ankit/rrd-xml/task.xml'.format(url=url)
	os.system(cmd)

	doc2 = minidom.parse("task.xml")

	# Make to give loop here for taking various at a time.

	tasks=doc2.getElementsByTagName("task")
	for task in tasks:
		id_task=task.getElementsByTagName("id")[0]
		id_task_data=id_task.firstChild.data
		start=task.getElementsByTagName("startTime")[0]
		startTime=start.firstChild.data
		finish=task.getElementsByTagName("finishTime")[0]
		finishTime=finish.firstChild.data
		t=task.getElementsByTagName("type")[0]
		type=t.firstChild.data

		attempt=task.getElementsByTagName("successfulAttempt")[0]
		attempt_data=attempt.firstChild.data

		os.system('sudo rm -r attempt.xml')
		url='http://ankit21:19888/ws/v1/history/mapreduce/jobs/{id_data_url}/tasks/{task_url}/attempts/{attempt_url} '.format(id_data_url=id_data,task_url=id_task_data,attempt_url=attempt_data)

		cmd='curl --compressed -H "Accept: application/xml" -X GET "{url}" >> /home/ankit/rrd-xml/attempt.xml'.format(url=url)
		os.system(cmd)

		# Here we got attempt.xml which we needed for the extraction of the data of a task.


		doc3 = minidom.parse ("attempt.xml")

		attempt=doc3.getElementsByTagName("taskAttempt")[0]
		elaspedTime=doc3.getElementsByTagName("elapsedTime")[0]
		elasped = elaspedTime.firstChild.data
		"""
		start=attempt.getElementsByTagName("startTime")[0]
		startTime=start.firstChild.data
		finish=attempt.getElementsByTagName("finishTime")[0]
		finishTime=finish.firstChild.data
		t=attempt.getElementsByTagName("type")[0]
		type=t.firstChild.data
		"""

		n=attempt.getElementsByTagName("nodeHttpAddress")[0]
		node=n.firstChild.data
		node=node[:-5]
		if (node not in node_list):
			node_list.append(node)
		startTime=int(startTime)
		finishTime=int (finishTime)
		startTime=startTime/1000
		finishTime=finishTime/1000
		
#---------------------------------------------------------------------------------------------------------------------------------
		os.system('sudo rm -r attempt_counters.xml')
		url='http://ankit21:19888/ws/v1/history/mapreduce/jobs/{id_data_url}/tasks/{task_url}/attempts/{attempt_url}/counters'.format(id_data_url=id_data,task_url=id_task_data,attempt_url=attempt_data)

		cmd='curl --compressed -H "Accept: application/xml" -X GET "{url}" >> /home/ankit/rrd-xml/attempt_counters.xml'.format(url=url)
		os.system(cmd)
		print cmd
		doc4 = minidom.parse ("attempt_counters.xml")
		read = doc4.getElementsByTagName("value")[-1]
		read_data = read.firstChild.data
		write = doc4.getElementsByTagName("value")[1]
		write_data = write.firstChild.data
		elasped=float(elasped)
		read_data=float(read_data)
		print read_data
		write_data=float(write_data)	
		print write_data
		x = (elasped / (read_data))
		dict[id_task_data]=x
# --------------------------------------------------------------------------------------------------------------------------------
		cmd='./zscript.sh {} {} {} {} {} {}'.format(startTime,finishTime,id_data,id_task_data,type,node)  # improvements needed
		os.system(cmd)


#-----------Starting labelling logic here -------------------------------

list_value=sorted(dict.values())
if((len(list_value) % 2) == 0):
	median = list_value[len(list_value)/2]
else:
	median = list_value[(len(list_value)/2)+1]		

threshold=1.3     # ---------Set threshold value here for labeling

os.system('sudo rm -r data_labelled.csv')
for key_task_id,value in dict.items():
	if (value > (median*threshold)):
		cmd='python csv_label.py {t_id} {label}'.format(t_id=key_task_id,label=1)	
		os.system(cmd)
	else:
		cmd='python csv_label.py {t_id} {label}'.format(t_id=key_task_id,label=0)	
		os.system(cmd)

#----------------Printing node_list in node_list.csv for further use ----------------------

file = open('node_list.csv','w')
writer= csv.writer(file)

writer.writerow(node_list)

#--------------- creating the csv s' for separate node's data ------------------------------

file = csv.reader(open('data_labelled.csv','r'))
entries=list(file)
print node_list
for node in node_list:
	filename = 'nodes/{}.csv'.format(node)
	file2_obj=open(filename,'w')	
	file2 = csv.writer(file2_obj)
	print node
	for entry in entries:
		if(entry[32] == node):
			file2.writerow((entry[2],entry[3],entry[5],entry[6],entry[7],entry[8],entry[9],entry[10],entry[11],entry[12],entry[13],entry[14],entry[15],entry[16],entry[17],entry[18],entry[19],entry[20],entry[21],entry[22],entry[23],entry[24],entry[25],entry[26],entry[27],entry[28],entry[33]))
	file2_obj.close()

		

