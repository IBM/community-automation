# https://code-ready.github.io/crc/#starting-monitoring-alerting-telemetry_gsg
# using the grep 1 line should be returned , and cut only the index
oc get clusterversion version -ojsonpath='{range .spec.overrides[*]}{.name}{"\n"}{end}' | nl -v 0|grep cluster-monitoring-operator|tr -d '[[:space:]]'|cut -c1
