class Solution(object):
    def removeDuplicates(self, nums):
        k=len(nums)
        out=[]
        for i in range(k):
            if nums[i] not in out:
                out.append(nums[i])
        k=len(out)
        for i in range(k):
            nums[i]=out[i]

        return k
sol=Solution()
a=[1,1,2]
k=sol.removeDuplicates(a)
print(k,a)
        