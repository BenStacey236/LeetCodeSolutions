# Medium Problem
# Problem 1456

def maxVowels(s: str, k: int) -> int:
    vowels = "aeiou"
    maxVowelNum = currentNumVowels = sum(1 for i in s[0:k] if i in vowels)

    for i in range(1, len(s)-k+1):
        if s[i-1] in vowels:
            currentNumVowels -= 1
        if s[i+k-1] in "aeiou":
            currentNumVowels += 1
        maxVowelNum = max(maxVowelNum, currentNumVowels)

    return maxVowelNum


input = "abciiidef"
k = 3

if __name__ == "__main__":
    print(maxVowels(input, k))