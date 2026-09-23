class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for a in range(0,len(nums)):
            for b in range(0,len(nums)): 
                if a!=b :
                    if (nums[a] + nums[b] == target):
                        return [a,b]