# Medium Problem
# Problem 49

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    
    for string in strs:
        sortedStr = ''.join(sorted(string))
        if sortedStr in anagrams:
            anagrams[sortedStr].append(string)
        else:
            anagrams[sortedStr] = [string]

    return [value for value in anagrams.values()]


if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        