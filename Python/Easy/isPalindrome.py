# Easy Problem
# Problem 125

def isPalindrome(s: str) -> bool:
    s = [letter.lower() for letter in s if letter.isalnum()]

    frontP = 0
    backP = len(s) - 1

    while frontP < backP:
        if s[frontP] != s[backP]:
            return False
        else:
            frontP += 1
            backP -=1

    return True


input = "A man, a plan, a canal: Panama"

if __name__ == "__main__":
    print(isPalindrome(input))