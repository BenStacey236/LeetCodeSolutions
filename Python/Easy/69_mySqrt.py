# Easy Problem
# Problem 69

def mySqrt(x: int) -> int:

    l, r = 0, x

    if x < 2:
        return x

    while l < r:

        mid = (l + r) // 2
        if l + 1 == r:
            return l

        midSquared = mid ** 2
        if midSquared > x:
            r = mid

        else:
            l = mid