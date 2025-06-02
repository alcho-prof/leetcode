class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        res=sorted(nums1)
        n=len(res)
        mid=n//2
        if n%2!=0:
            return res[mid]
        else:
            return (res[mid]+res[mid-1])/2    


        