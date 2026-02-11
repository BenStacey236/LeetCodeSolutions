# Easy Problem
# Problem 205

def isIsomorphic(s: str, t: str) -> bool:

    forwards: dict[str, str] = {}
    backwards: dict[str, str] = {}

    for l, r in zip(s, t):
        
        if l in forwards and forwards[l] != r:
            return False

        if r in backwards and backwards[r] != l:
            return False

        forwards[l] = r
        backwards[r] = l
        
    return True

if __name__ == "__main__":

    s = "egg"
    t = "see"

    print(isIsomorphic(s, t))