class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        return True if a==a[::-1] else False 