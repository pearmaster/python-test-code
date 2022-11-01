from abc import ABC, abstractmethod

class TheBase(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def foo(self) -> str:
        pass

    @abstractmethod
    def bar(self) -> str:
        pass

class TheMiddle(TheBase):

    def bar(self) -> str:
        return "World"

    @abstractmethod
    def yaz(self) -> str:
        pass

class TheChild(TheMiddle):

    def foo(self) -> str:
        return "Hello"

    def yaz(self) -> str:
        return "Great"

if __name__ == '__main__':

    tc = TheChild()
    print(f"{tc.foo()} {tc.yaz()} {tc.bar()}")
    print(f"Is TheChild a subclass {issubclass(TheChild, TheBase)} {issubclass(TheChild, TheBase)}")
    print(f"Is tc instance an instance of {isinstance(tc, TheBase)} {isinstance(tc, TheBase)}")