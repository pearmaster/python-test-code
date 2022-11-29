import pytest
import random

@pytest.fixture(scope='class')
def foo():
    print(f"running foo fixture {random.random()}")
    return {"hello": "world", "random": random.random()}

class UnitStuff:

    def setup_method(self):
        print(f"parent setup method")

    def test_from_parent(self, foo):
        print(f"from parent {foo}")
        assert False