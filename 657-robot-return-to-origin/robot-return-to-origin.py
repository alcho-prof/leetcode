class Solution:
    def judgeCircle(self, moves: str) -> bool:
        freq={} 
        for i in range(len(moves)):
            if moves[i] in freq:
                freq[moves[i]]+=1
            else:
                freq[moves[i]]=1    
        return freq.get("U",0)==freq.get("D",0)  and freq.get("L",0) ==freq.get("R",0)   