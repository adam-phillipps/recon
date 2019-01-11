import os
import sys
from googleapiclient.discovery import build
from webrecon import helpers, reporting


@reporting.self_report
def _ff(doc, *keys):
    import pdb
    pdb.set_trace()
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


@reporting.self_report
def search(q, *filters, key=None, cx=None, **kwargs):
    """
    Run a scoped search and filter the response.

    Params:
    -------
    q : str
        Query used to search CSE
    filters : str
        Terms used to limit the scope of the response

    Keyword Arguments:
    ------------------
    key : str
        Google CSE key
    cx : str
        Google CSE ID
    kwargs : Keyword Arguments
        Key Value pairs used to limit the scope of the search

    Returns:
    --------
    List[dict]
    """
    key = key if key is None else helpers.lookfor('CSE_KEY')
    cx = cx if cx is None else helpers.lookfor('CSE_ID')

    intel = []
    filters = ['title', 'link'] if not filters else filters
    api = build("customsearch", "v1", developerKey=key)
    response = api.cse().list(q=q, cx=cx, **kwargs).execute()['items']
    [intel.append(_ff(res, *filters)) for res in response]

    return intel
