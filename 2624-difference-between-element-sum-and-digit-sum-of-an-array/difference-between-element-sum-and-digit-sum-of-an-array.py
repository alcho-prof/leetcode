class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=sum(nums)
        digit_sum=sum(int(digit) for i in nums for digit in str(i))
        return abs(element_sum - digit_sum)

