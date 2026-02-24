# Hard Problem
# Problem 76

from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    
    tCount = Counter(t)

    minSize: int = float('inf')
    minPair: tuple[int, int] = None
    sCount: defaultdict[int] = defaultdict(int)

    l, r = 0, 0
    sCount[s[l]] += 1

    while r <= len(s):
        matches: bool = True
        for key in tCount.keys():
            if sCount[key] < tCount[key]:
                matches = False
                break

        if not matches:
            r += 1
            if r == len(s):
                break
            sCount[s[r]] += 1
            continue

        size = (r + 1) - l
        if size < minSize:
            minSize = size
            minPair = (l, r)

        if l + 1 > r:
            r += 1
            if r == len(s):
                break
            sCount[s[r]] += 1

        else:
            sCount[s[l]] -= 1
            l += 1

    if not minPair:
        return ""

    l, r = minPair
    return s[l:r+1]