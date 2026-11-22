class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for m in range(n+1,len(nums)):
                 if nums[n]+nums[m]==target :
                        return [n,m]


"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        