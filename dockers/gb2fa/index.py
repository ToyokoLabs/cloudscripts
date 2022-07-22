"""
reads all gb files from a bucket and convert it to fasta files
"""

import os

from Bio import SeqIO
import boto3

bucket = os.getenv('INPUTBUCKET', '')

session = boto3.Session()
s3 = session.resource('s3')
my_bucket = s3.Bucket(bucket)
for bo in my_bucket.objects.all():
    k = bo.key
    # download
    if k.endswith('.gb'):
        s3.Bucket(bucket).download_file(k, k)
        nn = k[:-2] + 'fa'
        with open(k) as ifh, open(nn, "w") as ofh:
            sequences = SeqIO.parse(ifh, "genbank")
            SeqIO.write(sequences, ofh, "fasta")
            # upload
        s3.Bucket(bucket).upload_file(nn, nn)
        os.remove(k)
        os.remove(nn)