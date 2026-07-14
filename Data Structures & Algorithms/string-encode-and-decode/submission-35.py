class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += f"{len(s)}#{s}"
        
        return word

    def decode(self, s: str) -> List[str]:
        words = []
        
        startIdx = 0
        for i, ch in enumerate(s):
            if ch == "#":
                word_len = s[startIdx:i]
                if not word_len.isnumeric():
                    continue
                
                word = s[i + 1:i + 1 + int(word_len)]
                words.append(word)
                startIdx = i + 1 + int(word_len)
        
        return words