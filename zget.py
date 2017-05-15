from xml.dom.minidom import parse
import xml.dom.minidom
import csv
import sys

doc = xml.dom.minidom.parse("boottime.xml")
rows = doc.getElementsByTagName("row")
count=0
for row in rows:
	count+=1
elements= [ [ 'nan' for i in range(29+5) ] for j in range(count) ]

i=0
for row in rows:
	t = row.getElementsByTagName("t")[0]
	v = row.getElementsByTagName("v")[0]
	elements[i][0]=int (t.firstChild.data)
	# elements [i][1] = float (v.firstChild.data)
	i+=1


				

files=['boottime.xml','bytes_in.xml','bytes_out.xml','cpu_aidle.xml','cpu_idle.xml','cpu_nice.xml','cpu_num.xml','cpu_speed.xml','cpu_system.xml','cpu_user.xml','cpu_wio.xml','disk_free.xml','disk_total.xml','load_fifteen.xml','load_five.xml','load_one.xml','mem_buffers.xml','mem_cached.xml','mem_free.xml','mem_shared.xml','mem_total.xml','part_max_used.xml','pkts_in.xml','pkts_out.xml','proc_run.xml','proc_total.xml','swap_free.xml','swap_total.xml']
k=0

for f in files:
	k+=1
	doc = xml.dom.minidom.parse(f)
	rows = doc.getElementsByTagName("row")
	for row in rows:
		t = row.getElementsByTagName("t")[0]
		v = row.getElementsByTagName("v")[0]
		j=-1			
		for i in elements:	
			j+=1
			if (int (t.firstChild.data) == i[0]):
				elements[j][k]= float(v.firstChild.data)

for i in range(5):
	k+=1
	j=-1
	for n in elements:
		j+=1
		if(i==0):
			elements[j][k]=sys.argv[3]
		if(i==1):
			elements[j][k]=sys.argv[4]
		if(i==2):
			elements[j][k]=sys.argv[5]
		if(i==3):
			elements[j][k]=sys.argv[6]
		if(i==4):
			elements[j][k]=0

"""
k=0
titles= [ [ 'nan' for i in range(29) ] for j in range(1) ]
print titles
titles[0][0]="timestamp"
for f in files:
	k+=1
	f=f[:-4]
	titles[0][k]=f
	print f
"""

c = csv.writer(open(sys.argv[7], "a"))

"""
for i in titles:
	c.writerow(i)
"""
for i in elements:
	c.writerow(i)			
			


