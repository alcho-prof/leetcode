class Solution:
    def triangleType(self, nums: List[int]) -> str:
        i=0
        nums.sort()
        if nums[i]+nums[i+1]<=nums[i+2]:
            return "none"
        if nums[i]==nums[i+1] and nums[i+1]==nums[i+2] and nums[i+2]==nums[i]:
            return "equilateral"
        elif nums[i]==nums[i+1] or nums[i+1]==nums[i+2] or nums[i+2]==nums[i]:
            return "isosceles"
        else:
            return "scalene"    

        
