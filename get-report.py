from salesforce import SalesforceConnection
import requests
import json

from s3 import push_to_s3

sf = SalesforceConnection()

path = "/services/data/v45.0/analytics/reports/00O0f0000089IddEAE"
url = "{}{}".format(sf.instance_url, path)
resp = requests.get(url, headers=sf.headers)
content = json.loads(resp.text)
the_good_stuff = content["factMap"]["T!T"]["aggregates"][0]
push_to_s3(filename="border2019.json", contents=the_good_stuff)
