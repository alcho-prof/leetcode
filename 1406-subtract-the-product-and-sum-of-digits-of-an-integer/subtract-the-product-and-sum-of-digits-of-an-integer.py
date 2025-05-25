class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        add=0
        while n>0:
            product*=n%10
            add+=n%10
            n//=10
        return product-add

