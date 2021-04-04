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
    print(d['foo'].lc.line)
    print(d['foo']['bar'].lc.item(3))
