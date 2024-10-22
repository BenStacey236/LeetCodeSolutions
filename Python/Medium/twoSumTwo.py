# Medium Problem
# Problem 167

def twoSumTwo(numbers: list[int], target: int) -> list[int]:
    frontP, backP = 0, len(numbers) - 1

    while frontP < backP:
        if numbers[frontP] + numbers[backP] == target:
            return [frontP+1, backP+1]
        
        elif numbers[frontP] + numbers[backP] < target:
            frontP += 1

        else:
            backP -= 1


input = [2,7,11,15]
target = 9

if __name__ == "__main__":
    print(twoSumTwo(input, target))