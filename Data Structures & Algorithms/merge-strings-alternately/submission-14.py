class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = []

        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            words.append(word1[i])
            words.append(word2[j])

            i += 1
            j += 1
        
        words.extend(word1[i:])
        words.extend(word2[j:])

        return "".join(words)