# Easy Problem
# Problem 1207

def uniqueOccurrences(arr: list[int]) -> bool:
    items = set(arr)
    occurrences = set()

    for item in items:
        count = arr.count(item)

        if count in occurrences:
            return False
        
        else:
            occurrences.add(count)

    return True