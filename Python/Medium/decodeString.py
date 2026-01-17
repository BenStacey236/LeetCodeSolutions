# Medium Problem
# Problem 394

def decodeString(s: str) -> str:
    
    stack = []

    num = ""
    for letter in s:

        if not letter.isnumeric() and letter != ']':
            stack.append(num)
            num = ""
            stack.append(letter)

        elif letter.isnumeric():
            num += letter

        else:
            toPush = ""
            while stack[-1] != '[':
                toPush = stack.pop() + toPush

            stack.pop()
            multiplier = int(stack.pop())
            stack.append(toPush * multiplier)

    return ''.join(stack)


if __name__ == "__main__":

    s = "3[a]2[bc]"
    print(decodeString(s))

    s = "3[a2[c]]"
    print(decodeString(s))