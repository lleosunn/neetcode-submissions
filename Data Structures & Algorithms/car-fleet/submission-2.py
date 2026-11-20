class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], (target - position[i])/speed[i]] for i in range(len(position))] # position, time to target pairs
        pairs.sort()
        pairs.reverse()
        # now we have pos, time to target pairs reverse sorted by position
        out = 1
        stack = [pairs[0][1]] # keep track of current time to target
        for car in pairs:
            if car[1] <= stack[-1]: # if car is blocked, it gets added to the fleet
                pass
            else:
                stack.append(car[1])
                out += 1

        
            
        return out

