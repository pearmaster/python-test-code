class MyString(str):
    def __new__(cls, *args, **kwargs):
        obj = str.__new__(cls, *args, **kwargs)
        obj._evaluated = False
        return obj

    @property
    def evaluated(self):
        return self._evaluated

    @evaluated.setter
    def evaluated(self, value):
        self._evaluated = value


if __name__ == "__main__":
    a = MyString("foo")
    b = MyString("bar")
    assert a.evaluated is False
    assert b.evaluated is False
    a.evaluated = True
    assert a.evaluated is True
    assert b.evaluated is False
    b.evaluated = True
    assert a.evaluated is True
    assert b.evaluated is True
    a.evaluated = False
    assert a.evaluated is False
    assert b.evaluated is True
