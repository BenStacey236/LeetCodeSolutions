# Medium Problem
# Problem 150

from math import trunc

def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = ['+', '-', '*', '/']

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            match token:
                case '+':
                    stack.append(stack.pop(-1) + stack.pop(-1))
                case '-':
                    x1, x2 = stack.pop(-1), stack.pop(-1)
                    stack.append(x2 - x1)
                case '*':
                    stack.append(stack.pop(-1) * stack.pop(-1))
                case '/':
                    x1, x2 = stack.pop(-1), stack.pop(-1)
                    stack.append(trunc(x2 / x1))

    return stack[0]


input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

if __name__ == "__main__":
    print(evalRPN(input))