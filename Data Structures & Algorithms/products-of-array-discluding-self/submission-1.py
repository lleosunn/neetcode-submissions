class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n
        
        return [product/int(m) for m in nums]