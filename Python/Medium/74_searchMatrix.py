# Medium Problem
# Problem 74

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    i = None
    for index, row in enumerate(matrix):
        if target >= row[0] and target <= row[-1]:
            i = index

    if i == None:
        return False
    
    searchRow = matrix[i]
    
    frontP, backP = 0, len(searchRow) - 1

    while frontP <= backP:
        mid = (frontP + backP) // 2
        if searchRow[mid] == target:
            return True
        elif searchRow[mid] < target:
            frontP = mid + 1
        else:
            backP = mid - 1

    return False


input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

if __name__ == "__main__":
    print(searchMatrix(input, target))