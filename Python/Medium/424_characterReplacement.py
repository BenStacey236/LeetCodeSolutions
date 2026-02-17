# Medium Problem
# Problem 424

from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    
    l, r = 0, 0
    counts: defaultdict[int] = defaultdict(int)

    counts[s[0]] = 1
    maxLen = 1
    while r < len(s)-1:

        if max(counts.values()) + k >= (r-l+1) or r == l:
            r += 1
            counts[s[r]] += 1
        
        else:
            counts[s[l]] -= 1
            l += 1

        if max(counts.values()) + k >= (r-l+1):
            maxLen = max(maxLen, r - l + 1)

    return maxLen