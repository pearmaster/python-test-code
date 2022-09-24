from dataclasses import dataclass

@dataclass
class Foo:
    a: int
    b: str

f = Foo(1, 2)

print(f.a)

fd = dict(f.__dict__)

print(fd)
