from salesforce import SalesforceConnection
import requests
import json

from s3 import push_to_s3

sf = SalesforceConnection()

path = '/services/data/v45.0/analytics/reports/00O0f000007mKFFEA2'
url = '{}{}'.format(sf.instance_url, path)
resp = requests.get(url, headers=sf.headers)
content = json.loads(resp.text)
the_good_stuff = content['factMap']['T!T']['aggregates'][0]
the_good_stuff = json.dumps(the_good_stuff)
push_to_s3(filename='smd19.json', contents=the_good_stuff)
