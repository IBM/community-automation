#!/bin/bash

# bash best practices
set -o errexit
set -o nounset
set -o pipefail

function getdescription () {
  local readme="../../ansible/roles/$1/readme.md"
  local rline=""
  local descLine=""
  local firstline="true"

  [[ ! -f $readme ]] && { echo "readme template added to role"; cp ../../docs/role.readme.template.md "$readme"; return; } || true

  while IFS= read -r rline || [[ -n "$rline" ]]; do

    # stop at first set of dashes
    grep -q '\-\-' <<< "$rline" && break 
    # skip over first set of equals
    grep -q '==' <<< "$rline" && continue
    [[ $firstline == "true" ]] && firstline="false" || descLine="$descLine<br> $rline"

  done < "$readme"
  echo -e "$descLine"

}

roletable="/tmp/roletable.html"
rolenamesfile="/tmp/rolenamefile"
ls ../../ansible/roles | xargs -I {}  basename {} > $rolenamesfile

echo -e "<html><table border=1>" > $roletable
echo -e "<th>Role</th><th>Example Plays</th><th>Description</th>" >> $roletable
while IFS= read -r line || [[ -n "$line" ]]; do
  echo -e  "<tr><td>$line</td>" >> $roletable

  echo -e "<td>" >> $roletable
  grep -E -rl "$line" ../../ansible | grep -vi -E "jenkins|roles|readme|inventory|example" | awk '{printf " "$1 "<br>"}' >> $roletable || true
  echo -e "</td><td>" >> $roletable

  getdescription "$line" >> $roletable || true

  echo -e "</td></tr>" >> $roletable

done < $rolenamesfile

echo -e "</table></html>" >> $roletable
