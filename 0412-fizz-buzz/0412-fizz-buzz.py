class Solution(object):
    def fizzBuzz(self, n):
        li=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                li.append("FizzBuzz")
            elif i%5==0:
                li.append("Buzz")
            elif i%3==0  :
                li.append("Fizz")
            else:
                li.append(str(i))
        return li
        
sol=Solution()
print(sol.fizzBuzz(15))
        