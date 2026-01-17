# Medium Problem
# Problem 649

from collections import deque
from collections import Counter

def predictPartyVictory(senate: str) -> str:
    rBanned = 0
    dBanned = 0
    counts = Counter(senate)
    queue = deque()

    for senator in senate:
        queue.append(senator)

    while counts.get('R') and counts.get('D'):
        senator = queue.popleft()

        if senator == 'R':
            if rBanned:
                counts['R'] -= 1
                rBanned -= 1
            else:
                queue.append(senator)
                dBanned += 1

        else:
            if dBanned:
                counts['D'] -= 1
                dBanned -= 1
            else:
                queue.append(senator)
                rBanned += 1

    return "Radiant" if queue[0] == 'R' else "Dire"



if __name__ == "__main__":
    print(predictPartyVictory("RDD"))
    print(predictPartyVictory("DRRDRDRDRDDRDRDR"))
    print(predictPartyVictory("D"))