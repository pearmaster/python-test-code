from dataclasses import dataclass

@dataclass
class Foo:
    a: int
    b: str

d = {"b":"hello", "a":1,}

f = Foo(**d)

print(f.a)

fd = dict(f.__dict__)

print(fd)
