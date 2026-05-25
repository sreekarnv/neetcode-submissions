class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        
        for s in strs:
            word += f"{len(s)}#{s}"
        
        return word   

    def decode(self, s: str) -> List[str]:
        start_idx = 0
        words = []
        
        for i, st in enumerate(s):
            if st == "#":
                word_len = s[start_idx:i]
                if not word_len.isnumeric():
                    continue
                word_len = int(word_len)
                word = s[i + 1:i + 1 + word_len]
                words.append(word)
                start_idx = i + 1 + word_len

        return words