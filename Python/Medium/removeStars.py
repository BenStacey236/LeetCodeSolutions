# Medium Problem
# Problem 2390

def removeStars(s: str) -> str:
    i = 0

    while 0 <= i < len(s):
        if s[i] == "*":
            s = s[:i-1] + s[i+1:]
            i = i - 1
        else:
            i += 1

    return s


input = "u*ensso****x*q"
if __name__ == "__main__":
    print(removeStars(input))