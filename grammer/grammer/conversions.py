import json

def tokanize_row(*columns):
    return map(_safe_strip(), columns)

def format_gse_query():
    pass

def build_query(row):
    return json.dumps({
        'id': row[0], 'brand': row[8], 'description': row[6],
        'measurement': ' '.join(map(str, row[14:]))})
