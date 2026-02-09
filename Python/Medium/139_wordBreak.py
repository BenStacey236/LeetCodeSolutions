# Medium Problem
# Problem 139

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:

    def match(target: str) -> bool:
        print(f"T: {target}")

        if target == "":
            return True

        for word in wordDict:
            if target.startswith(word):
                if match(target[len(word):]):
                    return True
            
        return False

    return match(s)


if __name__ == "__main__":

    wordDict = [
        "leet",
        "code"
    ]

    print(wordBreak("leetcode", wordDict))