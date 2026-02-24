# Medium Problem
# Problem 567

from collections import defaultdict

def checkInclusion(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    targetLetters: defaultdict[int] = defaultdict(int)
    running: defaultdict[int] = defaultdict(int)
    for letter in s1:
        targetLetters[letter] += 1

    l, r = 0, len(s1)-1
    for letter in s2[l:r+1]:
        running[letter] += 1

    while r < len(s2):
        match = True
        for key in targetLetters.keys():
            if key not in running or running[key] != targetLetters[key]:
                match = False 
        
        if match:
            return True

        running[s2[l]] -= 1
        l += 1
        r += 1
        if r >= len(s2):
            break
        running[s2[r]] += 1

    return False