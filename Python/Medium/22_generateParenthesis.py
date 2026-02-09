# Medium Problem
# Problem 22

from typing import List

def generateParenthesis(n: int) -> List[str]:
    
    res = []

    def explore(parens: str, toOpen: int, openParen: int) -> None:
        
        if len(parens) == n*2:
            res.append(parens)
            return

        if openParen > 0:
            explore(parens + ")", toOpen, openParen-1)
        
        if toOpen > 0:
            explore(parens + "(", toOpen-1, openParen+1)
    
    explore("", n, 0)
    return res