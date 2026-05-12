class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        word = []
        while i < len(word1) and j < len(word2):
            word.append(word1[i])
            word.append(word2[j])
            i += 1
            j += 1
        
        word.extend(word1[i:])
        word.extend(word2[j:])

        return "".join(word)