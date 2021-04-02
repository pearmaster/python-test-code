import inspect
from pprint import pprint


def foo():
    """
    This is the docstring.
    """
    pprint(foo.__doc__)

if __name__ == '__main__':
    foo()