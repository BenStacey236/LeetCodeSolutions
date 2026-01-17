# Easy Problem
# Problem 1768

def mergeAlternately(word1: str, word2: str) -> str:
    if len(word1) > len(word2):
        return ''.join([f'{a}{b}' for a, b in zip(word1, word2)])+word1[len(word2):]
    
    else:
        return ''.join([f'{a}{b}' for a, b in zip(word1, word2)])+word2[len(word1):]