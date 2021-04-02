import functools


def decorate(func):

    def say_goodbye():
        print(f"Goodbye {func.__name__}")

    setattr(func, "greeting", "hello")
    setattr(func, "bye", say_goodbye)

    return func

@decorate
def do_nothing():
    print(do_nothing.greeting)
    do_nothing.bye()

if __name__ == '__main__':
    print(do_nothing.__name__)
    print(do_nothing)
    print(do_nothing.greeting)
    do_nothing()