#!/bin/bash

sleep_count=30
while [[ $sleep_count -gt 0 ]]; do
  po_status=$(oc  get po -n rook-ceph | grep  -e  rook-ceph-mds-myfs | tr -s ' ')
  if [[ -z $po_status ]] ; then
    echo "Waiting for rook-ceph-mds-myfs pods to start"
    sleep 1m
    ((sleep_count--))
  else
    echo "rook-ceph-mds-myfs pods started"
    break
  fi
done
while [[ $sleep_count -gt 0 ]]; do
  po_status=$(oc  get po -n rook-ceph | grep  -e  rook-ceph-mds-myfs | grep -e Running | tr -s ' ')
  if [[ -z $po_status ]] ; then
    echo "Waiting for rook-ceph-mds-myfs pods to go to Running"
    sleep 1m
    ((sleep_count--))
  else
    echo "rook-ceph-mds-myfs pods Running"
    break
  fi
done
