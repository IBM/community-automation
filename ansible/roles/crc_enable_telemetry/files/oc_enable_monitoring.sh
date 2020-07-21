# https://code-ready.github.io/crc/#starting-monitoring-alerting-telemetry_gsg
#$1 is the numeric index
if [ ! -z $1 ] ; then
 s1="oc patch clusterversion/version --type='json' -p '[{\"op\":\"remove\", \"path\":\"/spec/overrides/monidx\"}]' -oyaml"
 eval ${s1/monidx/$1}
else
 echo "Require's 1 argument"
fi
