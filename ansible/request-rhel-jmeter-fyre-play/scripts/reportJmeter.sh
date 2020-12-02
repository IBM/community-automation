# presume 1 report jmeter.jtl input file
jreportCount=$(ls -1 *.jmeter.jtl|wc -l)
[ "$jreportCount" != "1" ] && echo "ERROR: multiple input .jmeter.jtl files" && exit 2||true
IFS='.' read inputjreport jreportext <<< $(ls -1 *.jmeter.jtl) 
[ -z $inputjreport ] && exit 1
### run as a sep process on a large host
### jmeter -g $inputjmx.jmeter.file -o $inputjmx.jmeter.report
jmeter -g $inputjreport.$jreportext -o $inputjreport.jmeter.report
