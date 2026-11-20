Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given array of daily temperatures
        # want to return another array
        # number of days before we get a warmer temperature
        out = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)): # go through all the temperatures
            while stack and temperatures[i] > temperatures[stack[-1]]: # while stack not empty and current > last temp
                stackind = stack.pop()
                out[stackind] = i - stackind
            stack.append(i)



        return out
