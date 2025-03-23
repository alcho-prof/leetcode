class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=sorted(nums1+nums2)
        n=len(a)
        b=len(a)//2
        if n%2!=0:
            return a[b]
        return (a[b]+a[b-1])/2    