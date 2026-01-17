# Easy Problem
# Problem 933


class RecentCounter:

    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        target = t - 3000
        
        while self.queue[0] < target:
            self.queue.pop(0)

        return len(self.queue)