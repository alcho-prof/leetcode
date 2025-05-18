class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=max(len((sentence).split())for sentence in sentences )
        return res