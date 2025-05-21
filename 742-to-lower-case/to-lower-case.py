class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.casefold()
        res=''
        for char in s:
            if "A"<=char<="Z":
                lower=chr(ord(char)+32)
                res+=lower
            else:
                res+=char
        return res            
        