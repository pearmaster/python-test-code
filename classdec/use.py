from inst import Concrete1, Concrete2

c1 = Concrete1()
print(Concrete2.foo)
c2 = Concrete2()

print(f"c1.foo {c1.foo}")
print(f"c2.foo {c2.foo}")

print(Concrete2.foo)