
class MyObj:

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"My name is {self.name}"


class WrappedObj:

    def __init__(self, inst: MyObj):
        self.inst = inst
        self.foo = "Barbie"

    def speak_foo(self):
        return f"My name is {self.foo}"

    def __getattr__(self, name):
        if name == "speak":
            return self.speak_foo
        return getattr(self.inst, name)



if __name__ == "__main__":

    a = MyObj("Joe")
    b = WrappedObj(a)
    print(b.speak())