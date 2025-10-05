"""
Fixed average calculator for AI & Prompts Track

- Reads numbers from marks.csv and computes the average with two decimals.
- Ignores the header row and any blank lines.
- Handles bad values gracefully (skips them without crashing).
- Prints only the final average to stdout, rounded to two decimals.
"""

import sys

def average_from_csv(path: str) -> float:
    with open(path, 'r', encoding='utf-8') as f:
        rows = [line.strip() for line in f.readlines()]
    total = 0.0
    count = 0

    # Skip the header row
    for r in rows[1:]:
        if not r:  # skip blank lines
            continue
        try:
            val = float(r)
            total += val
            count += 1
        except Exception:
            # skip non-numeric, non-blank lines
            continue
    return total / count if count else 0.0

if __name__ == '__main__':
    avg = average_from_csv('marks.csv')
    print(f"{avg:.2f}")
