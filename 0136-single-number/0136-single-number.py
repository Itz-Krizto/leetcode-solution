class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range(0,len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]