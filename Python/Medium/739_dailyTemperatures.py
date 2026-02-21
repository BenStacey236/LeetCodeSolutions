# Medium Problem
# Problem 739

from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:

    stack: List[tuple[int, int]] = []
    length: int = len(temperatures)
    res: List[int] = [0] * length

    for day in range(length-1, -1, -1):
        if not stack:
            stack.append((temperatures[day], day))
            continue

        while stack and stack[-1][0] <= temperatures[day]:
            stack.pop()

        if not stack:
            stack.append((temperatures[day], day))
            continue

        res[day] = stack[-1][1]-day
        stack.append((temperatures[day], day))

    return res