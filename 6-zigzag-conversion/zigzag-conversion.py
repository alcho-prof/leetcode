class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]*numRows
        cur=0
        dir=1
        for ch in s:
            rows[cur]+=ch
            if cur==0:
                dir=1
            elif cur==numRows-1:
                dir=-1
            cur+=dir
        return "".join(rows)  