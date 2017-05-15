from xml.dom import minidom
import os
doc2 = minidom.parse("task.xml")

# Make to give loop here for taking various at a time.

task=doc.getElementsByTagName("task")[0]
id_task=task.getElementsByTagName("id")[0]
id_task_data=id.firstChild.data
start=task.getElementsByTagName("startTime")[0]
startTime=start.firstChild.data
finish=task.getElementsByTagName("finishTime")[0]
finishTime=finish.firstChild.data
t=task.getElementsByTagName("type")[0]
type=t.firstChild.data
attempt=task.getElementsByTagName("successfulAttempt")[0]
attempt_data=attempt.firstChild.data


url='http://localhost:19888/ws/v1/history/mapreduce/jobs/{id_data}/tasks/{task}/attempts/{attempt}'.format(id_data=id_data,task=id_task_data,attempt=attempt_data)

cmd='curl --compressed -H "Accept: application/xml" -X GET "{url}" >> /home/ankit/rrd-xml/attempt.xml'.format(url=url)

os.system(cmd)




