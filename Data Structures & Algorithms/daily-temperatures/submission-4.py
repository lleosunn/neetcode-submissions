class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # indicies
        out = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                lowerTempIndex = stack.pop(-1)
                out[lowerTempIndex] = i - lowerTempIndex
            stack.append(i)


        return out