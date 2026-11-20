class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers in increasing order (with repeats)
        # walk up with the smallest increase
        i = 0
        j = len(numbers) - 1
        while True:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            inc_left = numbers[i + 1] + numbers[j]
            inc_right = numbers[i] + numbers[j-1]
            if abs(inc_left - s) < abs(inc_right - s):
                i += 1
            else:
                j -= 1



            
        