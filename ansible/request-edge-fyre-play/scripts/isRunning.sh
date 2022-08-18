pids=$(ps -fe|grep jmeter|grep -v grep|awk '{print $2}')
if [ "$1" == "gui" ] ; then
	if [ -z "$pids" ] ; then
		printf "<b><font color=red>Jmeter is not running</font></b>\n"
	else
		printf "<b><font color=green>Jmeter is running. Process(s)</font></b>\n$pids\n"
	fi
else
	printf "$pids\n"
fi
