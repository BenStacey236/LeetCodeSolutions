# Medium Problem
# Problem 12

from typing import List

def intToRoman(num: int) -> str:

    numerals: List[str] = []
    symbols: List[tuple[int, str]] = [
        (1000, 'M', True),
        (500, 'D', False),
        (100, 'C', True),
        (50, 'L', False),
        (10, 'X', True),
        (5, 'V', False),
        (1, 'I', True)
    ]

    for i, (divisor, symbol, pow10) in enumerate(symbols):

        if not pow10:
            if num >= divisor:
                if num // symbols[i+1][0] == 9:
                    numerals.append(symbols[i+1][1])
                    numerals.append(symbols[i-1][1])
                    num -= 9 * symbols[i+1][0]
                else:
                    num -= divisor
                    numerals.append(symbol)
        
        else:
            divisions = 0

            if num // divisor == 4:
                num -= 4 * divisor
                numerals.append(symbol)
                numerals.append(symbols[i-1][1])

            else:
                while num >= divisor:
                    num -= divisor
                    divisions += 1
                    numerals.append(symbol)

    return ''.join(numerals)