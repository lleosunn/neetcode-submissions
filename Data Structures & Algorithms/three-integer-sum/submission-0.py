class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # give array of nums, output all numbers s.t.
        # values sum up to 0
        # if we sort, we aren't removing duplicates
        nums = nums.sorted() # O(nlogn)
        out = []
        for i, n in enumerate(nums):
            if i == len(nums) - 2:
                break
            target = 0 - n # need to find numbers that add to target
            # 2 pointer problem here
            out += twoSum(nums[i + 1:])
        return out
            
def twoSum(sortedList, initialNumber, targetNumber):
    # output triplets with that initial number
    i = 0
    j = len(sortedList) - 1
    out = []
    for _ in range(j - 1):
        total = sortedList[i] + sortedList[j]
        if total == targetNumber:
            out.append([initalNumber, sortedList[i], sortedList[j]])
        elif total < targetNumber:
            i += 1
        else: j -= 1
    return out


        