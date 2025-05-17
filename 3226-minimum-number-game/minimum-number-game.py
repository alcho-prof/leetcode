class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        while len(nums)>0:
            i=min(nums)
            nums.remove(i)
            j=min(nums)
            nums.remove(j)
            arr.extend([j,i])
        return arr    