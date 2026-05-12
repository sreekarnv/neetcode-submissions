class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        word = ""
        while i < len(word1) and j < len(word2):
            word += word1[i]
            word += word2[j]
            i += 1
            j += 1
        
        word += word1[i:]
        word += word2[j:]

        return word