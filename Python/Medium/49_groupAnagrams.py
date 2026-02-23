# Medium Problem
# Problem 49

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for word in strs:
        letters = [0] * 26
        
        for letter in word:
            letters[ord(letter)-97] += 1

        groups[tuple(letters)].append(word)

    return list(groups.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        