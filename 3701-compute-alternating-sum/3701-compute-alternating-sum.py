class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        b = 0
        for i in range(0,len(nums)):
            b = b + (((-1)**i)*(nums[i]))
        return b