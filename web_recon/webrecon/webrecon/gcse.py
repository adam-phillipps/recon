import boto3
from googleapiclient.discovery import build as gcse_api_factory
from typing import Any, Dict, List, Mapping, Optional
import os
import sys
import pdb

#

# TypeHints to help with introspection and docstrings
SimpleMapping = Dict[str, str]
Filters = List[SimpleMapping]


def _ff(doc: SimpleMapping, *keys: Optional[List[Any]]) -> Mapping[str, Any]:
    """Filter and Flatten based on keys
    TODO:
    This is closer to what we're shooting for...so do that:
        items(formattedUrl,image/thumbnailLink,snippet,title)
        promotions(bodyLines/link,link,title)
    """
    dkeys = doc.keys()
    return { k: doc[k] for k in dkeys }

def _lookfor(key: str) -> str:
    """Search in the shell environment then parameter stores for the CSE API ID
    and key
    TODO:
    Create an actual docstring...
    """
    if os.getenv(key):
        val = os.getenv(key)
    else:
        ssm = boto3.client('ssm')
        try:
            param = ssm.get_parameter(Name=key)['Parameter']
            val = param['Value'] if 'Value' in param else ''
        except ssm.exceptions.ParameterNotFound as e:
            val = None

    return val


# @wrecord(mode=WEBRECON_RECORD_MODE, url=WEBRECON_INDEX_URL, index_name="")


    # Keyword Arguments:
    # q -- <String> This parameter is the actual search term.
    # filters -- [<String>] Filter the result of a search based on keys that might
    #      be included in the results
    # key -- <String> Set the Google CSE API key
    # cs -- <String> Set the Google CSE key ID
    # kwargs -- [<Keyword Arguments>] Send additional search customizations to the
    #      Google search API methos.


    # Returns:
    # [dict] with `filters` as keys of length `num`, from the params list.
def search(query: str,
           *filters: Optional[SimpleMapping],
           key: Optional[str] = None,
           cx: Optional[str] = None,
           **kwargs):
    """Run a search and filter the response.
    """
    import pdb
    if key is None:
        key = _lookfor('WEBRECON_GCSE_KEY')
    if cx is None:
        cx = _lookfor('WEBRECON_GCSE_ID')

    intel = []
    pdb.set_trace()
    filters = ['title', 'link'] if len(filters) == 0 else filters
    api = gcse_api_factory("customsearch", "v1", developerKey=key)
    response = api.cse().list(q=query, cx=cx, **kwargs).execute()['items']
    [intel.append(_ff(res, *filters)) for res in response]

    return intel
