import sys
from typing import List

def is_safe(levels: List[int]) -> bool:

    """Determine whether a single report’s levels are safe.

    A report is safe if:
      1. All adjacent differences are between 1 and 3 inclusive.
      2. The sequence is strictly increasing or strictly decreasing.

    Args:
        levels (List[int]): A list of integer levels from one report.

    Returns:
        bool: True if the report meets the safety criteria, False otherwise.
    """

    if len(levels) <= 1:
        return True

    diffs = [b - a for a, b in zip(levels, levels[1:])]

    if any(abs(d) not in (1, 2, 3) for d in diffs):
        return False

    all_pos = all(d > 0 for d in diffs)
    all_neg = all(d < 0 for d in diffs)
    return all_pos or all_neg


def count_safe_reports(lines: List[str]) -> int:

    """Count how many reports in the input are safe.

    Processes each non-empty line, parses it into integers,
    and uses `is_safe` to check safety.

    Args:
        lines (List[str]): Lines of text, each containing space-separated levels.

    Returns:
        int: The number of reports that satisfy the safety criteria.
    """

    safe_count = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        levels = list(map(int, stripped.split()))
        if is_safe(levels):
            safe_count += 1
    return safe_count


def main() -> None:
  
    """Read report data from stdin and print the count of safe reports."""

    lines = sys.stdin.readlines()
    result = count_safe_reports(lines)
    print(result)


if __name__ == "__main__":
    main()
