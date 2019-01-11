import re
from webrecon import helpers, reporting


PRICE_PATTERN = helpers.PRICE_PATTERN

@reporting.self_report
def get_price(tokanized_page, price_pattern=PRICE_PATTERN):
    """
    Find a price-like string from a document

    Params:
    -------
    page : List[str]
        Tokanized page
    price_pattern : Regex
        Pattern of price

    Returns:
    --------
    str
    """
    # TODO: This seems less than good because it creates another copy of the
    #       doc, in memory then goes over the whole page.
    #       It sure is readable, though, eh?
    #       Anyways, the TODO is to test and refactor if needed
    return re.findall(price_pattern, ' '.join(tokanized_page))
