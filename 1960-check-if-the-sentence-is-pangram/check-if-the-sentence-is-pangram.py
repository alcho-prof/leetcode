class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) >= 26:
            for i in range(97, 123):
                if chr(i) not in sentence:
                    return False
            return True
        return False
