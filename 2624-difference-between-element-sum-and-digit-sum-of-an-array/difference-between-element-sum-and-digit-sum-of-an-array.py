class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            a+=i
            while i!=0:
                b+=i%10
                i//=10
        return abs(a-b)        

