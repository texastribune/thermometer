from salesforce import SalesforceConnection
import requests
import json

from s3 import push_to_s3

sf = SalesforceConnection()

path = "/services/data/v46.0/analytics/reports/00O0f000007K5uiEAC"
url = "{}{}".format(sf.instance_url, path)
resp = requests.get(url, headers=sf.headers)
content = json.loads(resp.text)
print(content)
the_good_stuff = content["factMap"]["T!T"]["aggregates"][3]
print(the_good_stuff)
push_to_s3(filename="fmd2019.json", contents=the_good_stuff)
