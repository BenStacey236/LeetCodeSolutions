# Medium Problem
# Problem 735

from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for ast in asteroids:
        if not stack:
            stack.append(ast)
        elif ast > 0:
            stack.append(ast)
        elif stack[-1] < 0:
            stack.append(ast)
        elif abs(ast) > abs(stack[-1]):
            while stack and stack[-1] > 0 and abs(ast) > abs(stack[-1]):
                stack.pop()
            if stack and ast == -stack[-1]:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(ast)
        elif abs(ast) == abs(stack[-1]):
            stack.pop()

    return stack


input = [-2,-2,-1,-2]
input2 = [-2,-1,1,2]

if __name__ == "__main__":
    print(asteroidCollision(input))
    print(asteroidCollision(input2))