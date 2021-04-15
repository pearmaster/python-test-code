import sys

def foo():
    print(sys.modules['__main__'].__file__)
