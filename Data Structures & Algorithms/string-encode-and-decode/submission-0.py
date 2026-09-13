class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += f"{len(s)}#{s}"
        
        return word

    def decode(self, s: str) -> List[str]:
        words = []

        i = 0
        j = 0
        while j < len(s):
            if s[j] == "#":
                word_len = int(s[i:j])
                k = j + 1 + word_len
                word = s[j + 1:k]
                words.append(word)
                i = j + 1 + word_len
                j = i
            else:
                j += 1
        
        return words