from __future__ import print_function

import json
import os
import requests

print('Loading function')

def lambda_handler(event, context):

    status_opts = {
        0: 'Operational', 
        1: 'Under Maintenance',
        2: 'Degraded Performance',
        3: 'Partial Outage',
        4: 'Major Outage'
    }

    kwargs = {
        'api_endpoint': os.environ['API_ENDPOINT'],
        'component_id': '6cQeZAT8Yeo3',
        'api_key': os.environ['API_KEY']
    }

    r = requests.get("https://visualize-change.hotosm.org/api/health-check", headers={'Accept':'application/json'})

    if not r.ok:
    	r = requests.patch("https://{api_endpoint}/api/v0/components/{component_id}".format(**kwargs), json={'status': status_opts[4]}, headers={'x-api-key': kwargs['api_key']})
    	return r.text
    else:
        r = requests.patch("https://{api_endpoint}/api/v0/components/{component_id}".format(**kwargs), json={'status': status_opts[0]}, headers={'x-api-key': kwargs['api_key']})
        return r.text