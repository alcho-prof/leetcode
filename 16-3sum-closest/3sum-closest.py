class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        a=float('inf')
        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            while j<k:
                res=nums[i]+nums[j]+nums[k]
                if abs(res-target)<abs(a-target):
                    a=res
                if res<target:
                    j+=1
                elif res>target:
                    k-=1
                else:
                    return res
        return a
                                
