# Easy Problem
# Problem 1732

def largestAltitude(gain: list[int]) -> int:
    maxAlt = currentAlt = 0

    for alt in gain:
        currentAlt += alt
        maxAlt = max(maxAlt, currentAlt)

    return maxAlt