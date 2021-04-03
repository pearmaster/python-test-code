
class Foo:

    def __init__(self, foo):
        self._foo = foo
        print(f"Foo {self._foo}")


class Bar:

    def __init__(self, bar):
        self._bar = bar
        print(f"Bar {self._bar}")


class Penguin(Bar, Foo):

    def __init__(self, something, otherthing):
        super().__init__(something)
        Foo.__init__(self, otherthing)

if __name__ == '__main__':
    Penguin("jacob", "brunson")