from google.cloud import storage
import requests
from bs4 import BeautifulSoup as bs


# NOTE:
# Set export GOOGLE_APPLICATION_CREDENTIALS="xx.json" if needed

url = 'https://xxxx' # 'https://portal.nersc.gov/project/lsst/cosmoDC2/'
bucket_name = 'bucket_name'
prefix = 'file_prefx' # 'z_'

# get list of files in bucket
client = storage.Client()
bucket = client.get_bucket(bucket_name)

blobset = set()

blobs = bucket.list_blobs()
for blob in blobs:
    if blob.name.startswith(prefix):
        blobset.add(blob.name)


response = requests.get(url)
soup = bs(response.content, 'html.parser')
url_files = set()

table = soup.body.table
for element in table.find_all("tr"):
    try:
        td = element.find_all('td')[1]
        content = td.get_text()
        if content.startswith(prefix):
            url_files.add(content)
    except IndexError:
        pass

print(url_files-blobset)
