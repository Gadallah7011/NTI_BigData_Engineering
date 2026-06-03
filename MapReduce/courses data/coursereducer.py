#!/usr/bin/env python3

import sys
import math

current_province = None
total_score = 0
total_count = 0
scores = []

for line in sys.stdin:
    line = line.strip()

    province, score, count = line.split("\t")

    score = float(score)
    count = int(count)

    if current_province == province:
        total_score += score
        total_count += count
        scores.append(score)

    else:
        if current_province is not None:

            avg = total_score / total_count

            variance = sum((x - avg) ** 2 for x in scores) / total_count

            std = math.sqrt(variance)

            print(f"{current_province}\t{total_count}\t{avg:.2f}\t{std:.2f}")

        current_province = province
        total_score = score
        total_count = count
        scores = [score]

if current_province is not None:

    avg = total_score / total_count

    variance = sum((x - avg) ** 2 for x in scores) / total_count

    std = math.sqrt(variance)

    print(f"{current_province}\t{total_count}\t{avg:.2f}\t{std:.2f}")
