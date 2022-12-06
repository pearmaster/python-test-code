from dec import BaseClass, dec

class Concrete1(BaseClass):
    foo = 3
    def bar(self):
        return 13

@dec(100)
class Concrete2(BaseClass):
    def bar(self):
        return 14