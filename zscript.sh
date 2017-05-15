	#!/bin/bash

	echo "hello ak"
	starttime=$1
	finishtime=$2
	job_id=$3
	task_id=$4
	job_type=$5	
	node=$6
	data_file="data.csv"
	path=/var/lib/ganglia/rrds/cluster1/$node
	storage_path=/home/ankit/rrd-xml
	
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/boottime.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/boottime.xml	
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/bytes_in.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/bytes_in.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/bytes_out.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/bytes_out.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_aidle.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_aidle.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_idle.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_idle.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_nice.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_nice.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_num.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_num.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_speed.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_speed.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_system.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_system.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_user.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_user.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/cpu_wio.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/cpu_wio.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/disk_free.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/disk_free.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/disk_total.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/disk_total.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/load_fifteen.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/load_fifteen.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/load_five.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/load_five.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/load_one.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/load_one.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/mem_buffers.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/mem_buffers.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/mem_cached.rrd:sum:AVERAGE XPORT:xx:    >$storage_path/mem_cached.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/mem_free.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/mem_free.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/mem_shared.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/mem_shared.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/mem_total.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/mem_total.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/part_max_used.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/part_max_used.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/pkts_in.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/pkts_in.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/pkts_out.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/pkts_out.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/proc_run.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/proc_run.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/proc_total.rrd:sum:AVERAGE XPORT:xx:    >$storage_path/proc_total.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/swap_free.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/swap_free.xml
	rrdtool xport -s $starttime -e $finishtime DEF:xx=$path/swap_total.rrd:sum:AVERAGE XPORT:xx:    > $storage_path/swap_total.xml

	python $storage_path/zget.py $starttime $finishtime $job_id $task_id $job_type $node $data_file
