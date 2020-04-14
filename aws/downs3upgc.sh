#!/bin/bash
# Download a list of files from AWS S3 bucket and uploads to a
# Google bucket with the same name.
# How to use:
# downs3upgc.sh list.txt bucketname

file=$1
while IFS= read -r line
do
        printf '%s\n' "$line"
        aws s3 cp s3://$2/${line##*/} .
        # wait 1 sec
        sleep 1
        # upload to Google Cloud
        gsutil cp ${line##*/} gs://$2
        rm ${line##*/}
done <"$file"
