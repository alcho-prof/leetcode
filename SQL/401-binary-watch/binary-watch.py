class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res=[]
        for i in range(12):
            for j in range(60):
                if bin(i).count('1')+bin(j).count('1')==turnedOn:
                    res.append("{}:{:02d}".format(i,j))
        return res