# Easy Problem
# Problem 202

def isHappy(n: int) -> bool:
    
    seen: set[int] = set()

    while n != 1:
        
        n = sum([int(dig)**2 for dig in str(n)])
        if n in seen:
            return False
        
        seen.add(n)
        
    return True