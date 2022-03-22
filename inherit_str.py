class MyString(str):
    def __new__(cls, *args):
        if isinstance(args[0], cls):
            print(f"{args[0]} is already a {cls}")
            return args[0]
        obj = str.__new__(cls, *args)
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
    c = MyString(a)
    d = MyString(b)
    assert c.evaluated is False
    assert d.evaluated is True
    c.evaluated = True
    d.evaluated = False
    assert a.evaluated is True
    assert b.evaluated is False
    assert c.evaluated is True
    assert d.evaluated is False