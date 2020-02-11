#!/bin/bash
# How to use:
# downloadfromlist.sh list.txt bucketname
file=$1
while IFS= read -r line
do
        # display $line or do somthing with $line
        printf '%s\n' "$line"
        wget "$line"
        # wait 1 sec
        sleep 1
        # get filename
        gsutil cp ${line##*/} gs://$2
        rm ${line##*/}
done <"$file"
