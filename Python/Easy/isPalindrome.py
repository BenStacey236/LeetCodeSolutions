# Easy Problem

def isPalindrome(s: str) -> bool:
    s = [letter.lower() for letter in s if letter.isalnum()]

    return s == list(reversed(s))


input = "A man, a plan, a canal: Panama"

if __name__ == "__main__":
    print(isPalindrome(input))