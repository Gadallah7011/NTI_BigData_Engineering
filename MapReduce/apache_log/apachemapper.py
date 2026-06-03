#!/usr/bin/env python3
import sys
import re

pattern = r'^(\d+\.\d+\.\d+\.\d+)'

for line in sys.stdin:
    match = re.search(pattern, line)

    if match:
        ip = match.group(1)
        print(f"{ip}\t1")
