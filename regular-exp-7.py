import sys
import re

pattern = r"human"

for line in sys.stdin:
    line = line.strip()
    fixed = re.sub(pattern, 'computer', line)
    print(fixed)