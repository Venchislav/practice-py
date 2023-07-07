import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    fixed = re.sub(r"(\w)(\1)+", r"\1", line)
    print(fixed)
    