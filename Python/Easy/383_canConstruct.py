# Easy Problem
# Problem 383

from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    letters = Counter(magazine)

    for letter in ransomNote:
        if letter not in letters:
            return False

        if letters[letter] <= 0:
            return False

        letters[letter] -= 1

    return True