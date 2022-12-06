
from abc import ABC, abstractmethod, ABCMeta

class BaseClass(metaclass=ABCMeta):

    @property
    @abstractmethod
    def foo(self) -> int:
        return 1

    @abstractmethod
    def bar(self) -> int:
        ...

def dec(v):
    def inner(cls):

        def new_foo(self):
            return 4

        cls.foo = property(new_foo)
        abstmeths = list(cls.__abstractmethods__)
        abstmeths.remove('foo')
        cls.__abstractmethods__ = frozenset(abstmeths)
        return cls
    
    return inner