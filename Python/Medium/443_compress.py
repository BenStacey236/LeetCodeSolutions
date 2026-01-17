# Medium Problem
# Problem 443

def compress(chars: list[str]) -> int:
    output = []
    currentChar = chars[0]
    count = 0

    for char in chars:
        if char != currentChar:
            output.append(currentChar)
            output.append(count)
            currentChar = char
            count = 1

        else:
            count += 1

    output.append(currentChar)
    output.append(count)

    for i in range(0, len(output)-1, 2):
        count = output[i+1]
        for n in range(count):
            char = chars.pop(0)
        
        chars.append(char)
        if count != 1: 
            countStr = str(count)
            for letter in countStr:
                chars.append(letter)

    return len(chars)
        


input = ["a","b","b","c","c","c"]

if __name__ == "__main__":
    compress(input)
    print(input)