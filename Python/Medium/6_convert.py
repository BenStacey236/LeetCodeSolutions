# Medium Problem
# Problem 6

def convert(s: str, numRows: int) -> str:

    if numRows == 1:
        return s

    res = []

    for row in range(numRows):
        step = numRows+(numRows-2)
        offset = step - 2*row
        for i in range(row, len(s), step):
            res.append(s[i])

            if row != 0 and offset != 0:
                if i + offset < len(s):
                    res.append(s[i+offset])

    return ''.join(res)