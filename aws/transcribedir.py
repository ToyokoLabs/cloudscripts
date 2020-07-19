"""
Transcribe all audio files in current directory using 
AWS Transcribe

TO DO:
 * Use logging
 * Use input from command line

"""

import time
from glob import glob
import uuid
import json

import requests
import boto3

FILE_TYPE = 'mp4'
LANGUAGE_CODE='es-ES'
BASE_URI = "https://s3-us-west-1.amazonaws.com/ccnl.toyoko.io/newmp4/"


def save_text(cnt, file_name):
    """
    """
    tmp = json.loads(cnt.decode('utf-8'))
    trans = tmp['results']['transcripts'][0]['transcript']
    with open(file_name, 'w') as fh:
        fh.write(trans)


transcribe = boto3.client('transcribe')
allfiles = glob('*.{}'.format(FILE_TYPE))

for file_ in allfiles:
    job_uri = BASE_URI + file_
    job_name = '{}-{}'.format(file_, uuid.uuid1())
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat=FILE_TYPE,
        LanguageCode=LANGUAGE_CODE
)
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(15)
    print('ready')
    url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    response = requests.get(url)
    cnt = response.content
    fn = file_ + '.json'
    print("saving {}".format(fn))
    save_text(cnt, fn)

