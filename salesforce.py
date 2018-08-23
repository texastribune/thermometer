import json
import os

import requests

class SalesforceConnection(object):
    """
    Represents a connection to Salesforce.

    Creating an instance will authenticate and allow queries
    to be processed.
    """

    def __init__(self):

        payload = {
                'grant_type': 'password',
                'client_id': os.environ['SALESFORCE_CLIENT_ID'],
                'client_secret': os.environ['SALESFORCE_CLIENT_SECRET'],
                'username': os.environ['SALESFORCE_USERNAME'],
                'password': '{0}{1}'.format(os.environ['SALESFORCE_PASSWORD'],
                    os.environ['SALESFORCE_TOKEN']),
                }
        token_path = '/services/oauth2/token'
        url = '{0}://{1}{2}'.format('https', os.environ['SALESFORCE_HOST'],
                token_path)
        # TODO: some error handling here:
        r = requests.post(url, data=payload)
        response = json.loads(r.text)
        self.instance_url = response['instance_url']
        access_token = response['access_token']

        self.headers = {
                'Authorization': 'Bearer {}'.format(access_token),
                'X-PrettyPrint': '1',
                }

    def query(self, query, path='/services/data/v33.0/query'):
        """
        Run a SOQL query against this Salesforce instance.
        """
        url = '{0}{1}'.format(self.instance_url, path)
        if query is None:
            payload = {}
        else:
            payload = {'q': query}
        # TODO: error handling:
        r = requests.get(url, headers=self.headers, params=payload)
        response = json.loads(r.text)
        # recursively get the rest of the records:
        if response['done'] is False:
            return response['records'] + self.query(query=None,
                    path=response['nextRecordsUrl'])
        return response['records']
