class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # in: list of ints
        # out: list of list of 3 ints 
        # sort the input list
        # go through the sorted list, these are the starters for the triplets
        # to account for duplicates, skip a loop if the starter was the same as last round
        # for each starter: do a 2 pointer search through the sorted list for 0 - n

        # for the two pointer search: keep track of previous pointer values.
        # if the next pointer value = previous, skip that one
        prev_value = None
        out = []
        for i in range(len(nums) - 2):
            if nums[i] == prev_value: # duplicate
                prev_value == nums[i]
                continue
            out += self.twoPointer(nums[i:], nums[i], 0 - nums[i])
        return out


    def twoPointer(self, nums: List[int], starter: int, target: int) -> List[List[int]]:
        left_index = 0
        right_index = len(nums) - 1
        left_prev_value = None
        right_prev_value = None
        out = []

        for _ in range(1, len(nums) - 1): # loop length - 1 times
            # duplicates
            if nums[left_index] == left_prev_value:
                left_prev_value = nums[left_index]
                left_index += 1
                continue
            if nums[right_index] == right_prev_value:
                right_prev_value = nums[right_index]
                right_index -= 1
                continue

            total = nums[left_index] + nums[right_index]
            if total == target:
                out.append([starter, nums[left_index], nums[right_index]])
                left_index += 1 # advance any pointer
            elif total < target:
                left_prev_value = nums[left_index]
                left_index += 1
            else:
                right_prev_value = nums[right_index]
                right_index -= 1
        
        return out
            
            