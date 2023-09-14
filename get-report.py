from salesforce import SalesforceConnection
import requests
import json

from s3 import push_to_s3

sf = SalesforceConnection()

# set array_index to 0 for Giving Tuesday report and 3 for SMD/FMD report
array_index = 3
path = "/services/data/v46.0/analytics/reports/00OPe00000126S9MAI"
filename = "fmd2023.json"

url = "{}{}".format(sf.instance_url, path)
resp = requests.get(url, headers=sf.headers)
content = json.loads(resp.text)
print('Content loaded')
the_good_stuff = content["factMap"]["T!T"]["aggregates"][array_index]

push_to_s3(filename=filename, contents=the_good_stuff)
print('File pushed to S3')