class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers in increasing order (with repeats)
        # walk up with the smallest increase
        i = 0
        j = 1
        while True:
            print(i, j)
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if j - i == 1:
                j += 1
            elif j == len(numbers) - 1:
                i += 1
            elif numbers[i + 1] < numbers[j+1]:
                i += 1
            else:
                j += 1