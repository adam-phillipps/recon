from webrecon import reporting

PRICE_PATTERN = "\d{1,3}(?:,\d{3})*(?:\.\d+)?"

@reporting.self_report
def lookfor(key):
    """
    Search in the shell environment then parameter stores for the given key

    Params:
        - key:str
    Returns:
        - None
        - Value:str
        - Value:dict
    """
    try:
        # check environment variables
        val = os.getenv(key)

        if not val:
            from boto3 import client as bc
            # search in AWS SSM Params Store
            ssm = bc('ssm')
            param = ssm.get_parameter(Name=key)['Parameter']
            val = param['Value'] if 'Value' in param else ''

    except NameError as e:
        # it's ok to ignore errors that we receive while looking for
        # hidden values because sometimes those values or even the keys
        # we're searching for don't exist.
        pass

    return val
