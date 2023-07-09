import sys
import re

for line in sys.stdin:
    try:
        a = int(str(line), 2)
        if a % 3 == 0:
            print(f"{line}".strip())
    except:
        None
