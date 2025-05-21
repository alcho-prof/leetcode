class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        for a in range(1,len(s)):
            i=s[a-1]
            j=s[a]
            if "A" <= i <="Z":
                i=chr(ord(i)+32)
            if "A"<=j<="Z":
                j=chr(ord(j)+32) 
            if i!=j:
                count+=1
        return count               