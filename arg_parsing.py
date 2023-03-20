import argparse

parser = argparse.ArgumentParser()

class TrueUnlessSpecifiedFalseAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        kwargs['default'] = True
        kwargs['const'] = True
        super().__init__(option_strings, dest, nargs='?', **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if str(values).lower() in ['false', 'no', '0', 'n']:
            bool_value = False
        else:
            bool_value = bool(values)
        setattr(namespace, self.dest, bool_value)

parser.add_argument('--do', action=TrueUnlessSpecifiedFalseAction, help='do something')
parser.add_argument('--no-utils', action='store_true', help="Don't use util interfaces")

args = parser.parse_args()

print("----")
print(args)
