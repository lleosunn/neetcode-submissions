class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        # basin: false
        # new > prev --> basin = ture
        # new < prev --> in basin, basin height 2
        # new > prev --> out of basin
        return 9
