class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], (target - position[i])/speed[i]] for i in range(len(position))] # position, time to target pairs
        pairs.sort()
        # now we have pos, time to target pairs sorted by position
        out = 1
        stack = [] # keep track of current time to target
        for car in pairs:
            if stack and stack[-1] <= car[1]: # car joins the current fleet
                stack.append(car[1])
            else:
                out += 2
                stack.append(car[1])
        return out

