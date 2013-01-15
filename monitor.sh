#!/bin/bash

echo 'Time           ==> cpu pwr iowait'
while [ 1 ]
do
    cur=$(date -d "today" +"%m-%d %H:%M:%S")

    data=$(vmstat | tail -n 1)
    us=$( echo $data | awk '{print $13}' )
    sy=$( echo $data | awk '{print $14}' )
    (( cpu=us+sy ))

    pwr=$( echo $data | awk '{print $1}' )

    iodata=$( iostat -c | tac | sed -n 2p )
    iowait=$( echo $iodata | awk '{print $4}' )



    echo $cur '==>' $cpu%  $pwr ' ' $iowait%
    sleep 3
done
