class Solution:
    def addDigits(self, num: int) -> int:
        n=num
        while n>=10:
            res=0
            while n>0:
                res+=n%10
                n=n//10
            n=res
        return n
