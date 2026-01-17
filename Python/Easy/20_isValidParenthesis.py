# Easy Problem
# Problem 20

def isValidParenthesis(s: str) -> bool:
    stack = []
    validBrackets = {'(':')', '[':']', '{':'}'}

    
    for bracket in s:
        if bracket in validBrackets:
            stack.append(bracket)
        elif bracket in validBrackets.values():
            if len(stack) == 0:
                return False
            elif validBrackets[stack.pop(-1)] != bracket:
                return False
        
    return len(stack) == 0


input = '({[]})'

if __name__ == "__main__":
    print(isValidParenthesis(input))