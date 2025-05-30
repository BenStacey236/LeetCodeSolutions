# Medium Problem
# Problem 2390

def removeStars(s: str) -> str:
    output = []

    for char in s:
        if char == "*":
            output.pop()

        else:
            output.append(char)

    return ''.join(output)


input = "u*ensso****x*q"
if __name__ == "__main__":
    print(removeStars(input))