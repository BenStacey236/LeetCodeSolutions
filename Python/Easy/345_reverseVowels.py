# Easy Problem
# Problem 345

def reverseVowels(s: str) -> str:
    vowels = [letter for letter in s if letter.lower() in {'a', 'e', 'i', 'o', 'u'}]
    newString: str = ""
    
    for letter in s:
        if letter.lower() in {'a', 'e', 'i', 'o', 'u'}:
            newString += vowels.pop(-1)
        else:
            newString += letter

    return newString


input = "IceCreAm"

if __name__ == "__main__":
    print(reverseVowels(input))
    