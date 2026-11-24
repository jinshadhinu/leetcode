class Solution(object):
    def isPalindrome(self, x):
        X=str(x)
        y=""
        for i in range(len(X)-1,-1,-1):
            y+=X[i]
        if y==X:
            return True
        else:
            return False

sol=Solution()
print(sol.isPalindrome(121))


        