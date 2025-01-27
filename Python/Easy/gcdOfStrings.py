# Easy Problem
# Problem 1071

def gcdOfStrings(str1: str, str2: str) -> str:
    long = str1 if len(str1) > len(str2) else str2
    short = str1 if long == str2 else str2

    for i in range(len(short), 0, -1):
        divisor = short[:i]
        if (divisor in long) and (divisor * (len(long) // len(divisor)) == long) and (divisor * (len(short) // len(divisor)) == short):
            return divisor

    return ""