#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("***")

    score = float(parts[0])

    province = parts[1].split("_")[1]

    print(f"{province}\t{score}\t1")
