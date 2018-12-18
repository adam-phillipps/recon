name = "webrecon"

try:
    print('here')
    from . import gcse as gcse
    from . import constants as constants
except ImportError as err:
    # If something strange happens during `import os` and setting the variables
    # in the try block, just move along but print out the error in the most
    # unbreakable way
    print("Attempted to import gcse and failed...")
    print(err)
    pass
