from functools import wraps
import logging

def self_report(func, *args, **kwargs):
    """
    Report a method call, its parameters, arguments, return values and responses
     for each method decorated with the @self_report decorator.  Each time a
     method that is decorated with @self_report runs, it will gather the params
     it was invoked with and send that information up to the index.  The original
     method is run and the resulting behaviour is sent to the index.  Finally the
     original method's response is returned to the caller, as usual.

     Params:
        - func:Function
    """
    print(f"Following: {func.__name__}")
    @wraps(func)
    def _wrapper(*args, **kwargs):
        # print(f"stuff stuff: {func.__doc__}")
        # _wrapper.__doc__ = func.__doc__

        try:
            print(f"Running: {func.__name__}( {args} , {kwargs} )")
            v = func(*args, **kwargs)
        except Exception as e:
            logging.FATAL(f"Failed running {func.__name__}: {e}")
            report_failure(func.__name__,
                           *args,
                           failure=e,
                           **kwargs)

        rep_id = report_invocation(func.__name__,
                                   *args,
                                   scope='id',
                                   **kwargs)

        report_results(func.__name__,
                       *args,
                       invocation_report_id=rep_id,
                       **kwargs)
        print(f"Finished: {func.__name__}( {args} , {kwargs} )")
        return v

    return _wrapper

def report_invocation(*args, scope=None, **kwargs):
    logging.debug(f"Reporting invocation for {args}, scope={scope}, {kwargs}")
    pass

def report_results(*args, **kwargs):
    logging.debug(f"Reporting results for {args}, {kwargs}")
    pass
