import boto3
from googleapiclient.discovery import build
import os
import sys
import pdb

def _ff(doc, *keys):
    """
    Filter and Flatten based on keys
    TODO:
    This is closer to what we're shooting for...so do that:
        items(formattedUrl,image/thumbnailLink,snippet,title)
        promotions(bodyLines/link,link,title)
    """
    d = {}
    [d.update({k:doc[k]}) for k in keys if k in doc.keys()]
    return d

def _lookfor(key):
    """
    Search in the shell environment then parameter stores for the CSE API ID and
    key
    TODO:
    Create an actual docstring...
    """
    if os.getenv(key):
        val = os.getenv(key)
    else:
        ssm = boto3.client('ssm')
        param = ssm.get_parameter(Name=key)['Parameter']
        val = param['Value'] if 'Value' in param else ''

    return val

def search(q,
           *filters,
           key=_lookfor('CSE_KEY'),
           cx=_lookfor('CSE_ID'),
           **kwargs):
    """
    Run a search and filter the response.
    TODO:
    Create an actual docstring...
    """
    intel = []
    filters = ['title', 'link'] if not filters else filters
    api = build("customsearch", "v1", developerKey=key)
    response = api.cse().list(q=q, cx=cx, **kwargs).execute()['items']
    [intel.append(_ff(res, *filters)) for res in response]

    return intel