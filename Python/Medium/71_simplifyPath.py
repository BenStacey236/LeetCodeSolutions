# Medium Problem
# Problem 71

def simplifyPath(path: str) -> str:

    stack = ['/']

    for sec in path.split('/'):

        if sec == "":
            continue

        if sec == '..':
            if len(stack) > 1:
                stack.pop()
                stack.pop()

        elif sec != '.':
            stack.append(sec)
            stack.append('/')

    if len(stack) > 1 and stack[-1] == '/':
        stack.pop()

    return ''.join(stack)