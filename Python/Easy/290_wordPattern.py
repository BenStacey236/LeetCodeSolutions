# Easy Problem
# Problem 290

def wordPattern(pattern: str, s: str) -> bool:
    
    splits: list[str] = s.split()

    if len(pattern) != len(splits):
        return False

    forwards: dict[str, str] = {}
    backwards: dict[str, str] = {}

    for letter, word in zip(pattern, splits):

        if letter in forwards and forwards[letter] != word:
            return False

        if word in backwards and backwards[word] != letter:
            return False

        forwards[letter] = word
        backwards[word] = letter

    return True