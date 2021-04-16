
class Foo(int):

    def __init__(self, v):
        int.__init__(v)

    def hello(self):
        print("Hello")

if __name__ == '__main__':
    a = Foo(1)
    b = Foo(2)
    print(a+b)
    a.hello()