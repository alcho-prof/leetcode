class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort(reverse=True)
        while nums:
            a=nums.pop()
            b=nums.pop()
            arr.extend([b,a])
        return arr  