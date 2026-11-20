class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list of numbers
        # output a list of numbers where every out[i] = product of everything but in[i]
        # build prefix and suffix list

        pre = [0]
        suf = [0]
        prod = 1
        for i in range(len(nums) - 1):
            prod *= nums[i]
            pre.append(prod)
        prod = 1
        nums = nums[::-1]
        for i in range(len(nums) - 1):
            prod *= nums[i]
            suf.append(prod)

        return[pre[i] * suf[i] for i in range(len(nums))]