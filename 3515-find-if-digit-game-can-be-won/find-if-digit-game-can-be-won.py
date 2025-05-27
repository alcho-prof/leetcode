class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=0
        double=0
        for i in nums:
            if len(str(i))==1:
                single+=i
            if len(str(i))==2:
                double+=i
        return single!=double            