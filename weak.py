import gc
from weakref import ref

class MyObj:

    def __init__(self, i):
        self.i = i
        print(f"creating {self.i}")
    
    def __del__(self):
        print(f"del {self.i}")

    def speak(self):
        print(f"I am {self.i}")

    def __call__(self):
        return self

    def __repr__(self):
        return f"<MyObj {self.i}>"

class A:

    def __init__(self):
        self.stuff: dict[i, MyObj] = dict()

    def add(self, i):
        print(f"Adding {i}")
        self.stuff[i] = MyObj(i)

    def remove(self, i):
        if i in self.stuff:
            print(f"Removing {i}")
            del self.stuff[i]

    def reference_to(self, i, ref_i):
        print(f"{i} is a reference to {self.stuff[ref_i]}")
        self.stuff[i] = ref(self.stuff[ref_i], lambda _: self.remove(i))

    def print(self):
        print(self.stuff)

    def speak_all(self):
        for o in self.stuff.values():
            o().speak()

if __name__ == '__main__':
    a = A()
    a.add(1)
    a.reference_to(2, 1)
    a.reference_to(3, 1)
    a.print()
    a.speak_all()
    a.remove(1)
    a.print()
