# Easy problem
# Problem 242

def isAnagram(s: str, t: str) -> bool:
    sSet = set(s)

    if not sSet == set(t):
        return False

    for letter in sSet:
        if not s.count(letter) == t.count(letter):
            return False

    return True
    

if __name__ == '__main__':
    print(isAnagram('aacc', 'ccca'))