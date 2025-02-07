# Easy Problem
# Problem 392

def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t) or not set(s).issubset(set(t)):
        return False
    
    l, r = 0, len(t)-1
    flip = 0
    
    while l < r:
        if len(s) > 0 and t[l] == s[0]:
            s = s[1:]
            l += 1
        else:
            l += flip

        if len(s) > 0 and t[r] == s[-1]:
            s = s[:-1]
            r -= 1
        else:
            r -= not flip

        flip = not flip

    return s == ""


s = "aaaaaa"
t = "bbaaaa"

if __name__ == "__main__":
    print(isSubsequence(s, t))