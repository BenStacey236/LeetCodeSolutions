# Easy Problem
# Problem 1002

from collections import defaultdict
from typing import List

def commonChars(words: List[str]) -> List[str]:

    letters: defaultdict[int] = defaultdict(int)
    for letter in words[0]:
        letters[letter] += 1

    for word in words[1:]:
        counter: defaultdict[int] = defaultdict(int)
        for letter in word:
            counter[letter] += 1

        for key in letters.keys():
            letters[key] = min(letters[key], counter[key])
        
    res = []
    for key, value in letters.items():
        for i in range(value):
            res.append(key)

    return res