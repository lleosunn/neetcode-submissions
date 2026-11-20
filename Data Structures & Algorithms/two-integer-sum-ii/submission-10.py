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
            if s > target:
                j -= 1
            else:
                i += 1



            
        