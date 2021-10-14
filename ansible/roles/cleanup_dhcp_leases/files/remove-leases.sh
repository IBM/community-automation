#!/bin/bash
#
set -o errexit
set -o nounset
set -o pipefail

cluster_name=$1
lease_file=/var/lib/dhcp/dhcpd.leases
temp_lease_file=/tmp/dhcpd.leases
detail_file="$cluster_name"_details.log

rm -f $temp_lease_file

echo "Stop dhcp server..."
systemctl stop isc-dhcp-server.service

while IFS= read -r ip || [[ -n "$ip" ]]; do
   grep -q "9\." <<< $ip || continue
   echo $ip
   remove=false
   while IFS= read -r line || [[ -n "$line" ]]; do
     grep -q $ip <<< $line && remove=true || true
     [[ $remove == "true" ]] && { grep -q "}" <<< $line && { remove=false; continue; } || continue; } || printf '%s\n' "$line" >> "$temp_lease_file"
   done < "$lease_file"

   cp "$temp_lease_file" "$lease_file"
   rm -f "$temp_lease_file"
done < "$detail_file"

echo "Start dhcp server..."
 systemctl start isc-dhcp-server.service