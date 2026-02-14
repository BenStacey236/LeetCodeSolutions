# Easy Problem
# Problem 70

def climbStairs(n: int) -> int:
    
    prev = 1
    curr = 1

    for i in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":

    print(climbStairs(4))