
from enum import Enum, EnumMeta
import inspect
import functools

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    BLACK = 3
    WHITE = 4

def convert_to_enums(func):
    param_sig = inspect.signature(func).parameters

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = []
        new_kwargs = {}
        for i, arg in enumerate(args):
            param_annotation = list(param_sig.values())[i].annotation
            if param_annotation != inspect.Parameter.empty and issubclass(type(param_annotation), EnumMeta):
                new_args.append(param_annotation(arg))
            else:
                new_args.append(arg)
        for kw, arg in kwargs.items():
            param_annotation = param_sig[kw].annotation
            if param_annotation != inspect.Parameter.empty and issubclass(type(param_annotation), EnumMeta):
                new_kwargs[kw] = param_annotation(arg)
            else:
                new_kwargs[kw] = arg
        return func(*new_args, **new_kwargs)
    return wrapper

@convert_to_enums
def rainbow(color: Color):
    print(color)

if __name__ == '__main__':
    rainbow(1)

