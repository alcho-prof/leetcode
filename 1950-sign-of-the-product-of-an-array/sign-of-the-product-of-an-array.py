class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFun(x):
            if x >0:
                return 1
            elif x<0:
                return -1
            else:
                return 0
        x=1        
        for i in range(len(nums)):
            x*=nums[i]
        return signFun(x)                   