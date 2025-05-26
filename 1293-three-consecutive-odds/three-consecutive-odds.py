class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag=False 
        for i in range(len(arr)-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                flag=True
        return True if flag else False        