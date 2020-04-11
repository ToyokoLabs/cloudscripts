#!/bin/bash
# How to use:
# dup.sh list.txt bucketname
# Download files from list, ungzip and extract AR data only

file=$1
while IFS= read -r line
do
        # display $line or do somthing with $line
        printf '%s\n' "$line"
        fn=${line##*/}
        gsutil cp gs://$2/$fn .
        # wait 1 sec
        sleep 1
        gunzip $fn
        sleep 1
        awk -F'\t' '$9 == "AR"' ${fn::13} > ar_${fn::13}
        printf 'done awk %s\n' "$fn"
        rm ${fn::13}
done <"$file"
