# Medium Problem
# Problem 3

from collections import defaultdict

def lengthOfLongestSubstring(s: str) -> int:

    if not s:
        return 0
    
    letters: defaultdict[str, int] = defaultdict(int)
    strlen: int = len(s)

    l, r, maxLen = 0, 0, 1
    letters[s[0]] = 1

    while l < strlen:
        #print(l, r, letters, s[l:r+1])

        if r + 1 < strlen and letters[s[r+1]] == 0:
            r += 1
            letters[s[r]] += 1
            maxLen = max(maxLen, r+1-l)

        else:
            letters[s[l]] -= 1
            l += 1

    return maxLen

    


if __name__ == "__main__":

    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(lengthOfLongestSubstring(s))