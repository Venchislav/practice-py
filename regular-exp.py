import re
import sys
"""
for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)


for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\bcat\b", line):
        print(line)


pattern = r"human"

for line in sys.stdin:
    line = line.strip()
    print(re.sub(pattern, 'computer', line))
    

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\bA+\b", 'augh', line, 1, re.IGNORECASE))

"""

import re
line = input()
print(re.sub(r"\b.{2+}\b", r'\2\1', line))
