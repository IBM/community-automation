rm -f nohup.out
rm -f *.error
rm -f *.jmeter.jtl
# presume 1 jmx input file
jmxCount=$(ls -1 *.jmx|wc -l)
[ "$jmxCount" != "1" ] && echo "ERROR: multiple input .jmx files" && exit 2||true
IFS='.' read inputjmx jmxext <<< $(ls -1 *.jmx) 
[ -z $inputjmx ] && exit 1
[ -d $inputjmx.jmeter.report ] && zip -rq9 $inputjmx.jmeter.report.`date +%F-%T`.zip $inputjmx.jmeter.report && rm -rf $inputjmx.jmeter.report
[ "$NEST_JMETER_REPORT" == "true"  ] && jReport=" -l $inputjmx.jmeter.jtl" 
### ^^ do not generate the report when the run is done since it requires TONS memory
### -e -o $inputjmx.jmeter.report
### run as a sep process on a large host
### jmeter -g $inputjmx.jmeter.jtl -o $inputjmx.jmeter.report
nohup jmeter -n -t $inputjmx.$jmxext -q $inputjmx.user.properties -j $inputjmx.jmeter.$$.log -JRESULTSREPORT=$inputjmx.jmeter.$$.error $jReport 1>/dev/null 2>/dev/null &
./isRunning.sh
