import json
import os
import re
from webrecon import reporting

SPACES_IN_TAB = os.getenv("SPACES_IN_TAB", 4)

@reporting.self_report
def tokanize_row(*columns):
    return map(_safe_strip(), columns)

@reporting.self_report
def format_gse_query():
    """
    Receive a gcse search result and apply formatting rules

    Params:
    -------
    raw : dict
        This is the result set form your gcse result or any other dictionary
    formatters : List[Function]
        Function objects that can accept a dict or tupple or anything else that
        behaves like an iterable, run arbitrary rules on it and
        return the formatted string as a result.  Rules will be applied from
        first to last and may overwrite each other.

    Returns:
    --------
    dict

    """
    pass

@reporting.self_report
def build_query(row):
    return json.dumps({
        'id': row[0], 'brand': row[8], 'description': row[6],
        'measurement': ' '.join(map(str, row[14:]))})

def doctodict(docstring):
    """
    Receive a docstring and format it into a json object that represents the
    elements in the docstring.

    Params:
    -------
    docstring : string

    Returns:
    --------
    dictionary : dict
        The string this method receives will be taken apart and reconstructed
        as a dictionary where the first level keys are 'description',
        'keyword_arguments', 'params' and 'returns'.

    Examples:
    ---------
    TODO : str
        create example and and code that can handle it that also ties in with
        the indicies.  This is how to run the method, though.
        webrecon.conversions.doc_to_dict(your_func.__doc__)
    """
    def _pattern(word, num=1):
        return f"{'    ' * num}{word}"

    lines   = [l for l in docstring.splitlines() if l]
    docdict = {"description": None, "keyword_arguments": [], "params": [], "returns": []}
    pat_indx_tups = []
    ppatt   = _pattern("Params:")
    kwpatt  = _pattern("Keyword Arguments:")
    rpatt   = _pattern("Returns:")

    # create tuple of (Params pattern, index of the location of said pattern)
    if ppatt in lines:
        pindx = lines.index(ppatt)
        pat_indx_tups.append((ppatt, pindx))

    # create tuple of (KW Args pattern, index of the location of said pattern)
    if kwpatt in lines:
        kwindx = lines.index(kwpatt)
        pat_indx_tups.append((kwpatt, kwindx))

    # create tuple of (Returns pattern, index of the location of said pattern)
    if rpatt in lines:
        rindx = lines.index(rpatt)
        pat_indx_tups.append((rpatt, rindx))

    sorted_map = sorted(pat_indx_tups, key=lambda tup: tup[1])

    # pull out the description
    if sorted_map[0][1] > 0:
        original_size = len(lines)
        docdict["description"] = ' '.join(
            [l.strip() for l in lines[0:sorted_map[0][1]]]).lower()

        # pop off the description and adjust the sorted map indicies for the diff
        lines.reverse()
        [lines.pop() for i in range(sorted_map[0][1])]
        lines.reverse()
        size_diff = original_size - len(lines)

        sorted_map = [(a[0], a[1] - size_diff) for a in sorted_map]

    # pull out Params, Keyword Arguments and Returns keys and values for them
    for i, attr in enumerate(sorted_map):
        outter_attr = attr[0].strip().lower().replace(':', '').replace(' ', '_')

        start_i = attr[1]+2 # add 2 because outter_attr and --- lines are skipped
        end_i = sorted_map[i+1][1] if len(sorted_map) > i+1 else len(lines)-1

        inner_attrs = lines[start_i:end_i]
        inner_keys = [(ii, a) for ii, a in enumerate(inner_attrs)
                        if re.compile(_pattern(r"\w+")).match(a)]

        for ii, ik in enumerate(inner_keys):
            iv_start = ik[0]+1
            iv_end = inner_keys[ii+1][0] if len(inner_keys) > ii+1 else len(inner_attrs)
            v = inner_attrs[iv_start:] if iv_start == iv_end else inner_attrs[iv_start:iv_end]
            value = ' '.join([d.strip() for d in v]).lower()
            docdict[outter_attr].append({ik[1].strip():value})

    return docdict
