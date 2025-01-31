# Easy Problem
# Problem 605

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    validFlowerLocations = 0
    
    for i, flower in enumerate(flowerbed):
        if i != 0 and i != len(flowerbed)-1:
            if not flower and not flowerbed[i-1] and not flowerbed[i+1]:
                validFlowerLocations += 1
                flowerbed[i] = 1

        elif i == 0 and len(flowerbed) > 1:
            if not flower and not flowerbed[1]:
                validFlowerLocations += 1
                flowerbed[i] = 1

        elif i == len(flowerbed)-1 and len(flowerbed) > 1:
            if not flower and not flowerbed[i-1]:
                validFlowerLocations += 1
                flowerbed[i] = 1

        elif len(flowerbed) == 1:
            if flowerbed[0] == 0:
                validFlowerLocations += 1

    return validFlowerLocations >= n




flowerbed = [0]
n = 1

if __name__ == "__main__":
    print(canPlaceFlowers(flowerbed, n))