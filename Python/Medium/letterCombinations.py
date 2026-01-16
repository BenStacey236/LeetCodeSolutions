# Medium Problem
# Problem 17

from typing import List

def letterCombinations(digits: str) -> List[str]:

    letterMapping: dict[str, list[str]] = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def backtrack(index: int, path: List[str]) -> None:
        
        if index == len(digits):
            res.append(''.join(path))
            return

        for letter in letterMapping[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    res = []

    backtrack(0, [])

    return res


if __name__ == "__main__":
    digits = "24854"

    print(letterCombinations(digits))