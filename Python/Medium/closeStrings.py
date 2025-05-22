# Medium Problem
# Problem 1657

from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    if sorted(list(Counter(word1).keys())) != sorted(list(Counter(word2).keys())):
        return False
    
    return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values()))
    

input1 = "abc"
input2 = "bca"

if __name__ == "__main__":
    print(closeStrings(input1, input2))