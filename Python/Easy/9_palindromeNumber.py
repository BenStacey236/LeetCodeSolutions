# Easy Problem
# Problem 9

def isPalindrome(x: int) -> bool:
    s = str(x)

    frontP = 0
    backP = len(s) - 1

    while frontP < backP:
        if s[frontP] != s[backP]:
            return False
        else:
            frontP += 1
            backP -=1

    return True