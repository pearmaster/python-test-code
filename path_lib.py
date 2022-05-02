from pathlib import Path

p = Path(__file__)

print(p)
print(p.resolve())
print((p / "../").resolve())