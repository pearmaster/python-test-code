from ruamel.yaml import YAML
from pprint import pprint

example = """
foo:
    bar:
        - one
        - 2
        - true
        - three:
            feet
    food:
        pizza
"""

if __name__ == '__main__':
    y = YAML(typ='rt')
    d = y.load(example)
    pprint(d)
    print(d.lc)
    print(d['foo'].lc)
    print(d['foo']['bar'].lc)
    pprint(dir(d['foo']['bar'][3]))
    """
    Through experimentation, I found that only **collections** have the 'lc' property....
    individual values do not.
    """