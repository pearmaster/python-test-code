
import pytest
import random

from fixit import foo, UnitStuff

class TestThis(UnitStuff):

    def setup_method(self):
        super().setup_method()
        print(f"setup method {random.random()}")

    def test_true(self, foo):
        print(f"test true {foo} {random.random()}")
        assert not True

    def test_false(self, foo):
        print(f"test_false {foo} {random.random()}")
        assert False