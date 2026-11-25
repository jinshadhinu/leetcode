class Solution(object):
    def runningSum(self, nums):
        Sum=[]
        for i in range(len(nums)):
            if i==0:
                Sum.append(nums[i])
            else:
                Sum.append(Sum[i-1]+nums[i])
        return Sum
sol=Solution()
num=[1,2,3,4]
print(sol.runningSum(num))