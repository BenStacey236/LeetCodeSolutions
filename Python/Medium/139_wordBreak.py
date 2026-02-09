# Medium Problem
# Problem 139

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:

    memo: dict[str, bool] = {}

    def match(target: str) -> bool:

        if target in memo:
            return memo[target]

        if target == "":
            return True

        for word in wordDict:
            if target.startswith(word):
                newSearch = target[len(word):]
                res = match(newSearch)
                memo[newSearch] = res 
                if res:
                    return True
            
        return False

    return match(s)


if __name__ == "__main__":

    wordDict = [
        "leet",
        "code"
    ]

    print(wordBreak("leetcode", wordDict))