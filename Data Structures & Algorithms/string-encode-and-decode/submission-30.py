class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        
        for s in strs:
            word += f"{len(s)}#{s}"
        
        return word

    def decode(self, s: str) -> List[str]:
        words = []
        start_idx = 0

        for i, ch in enumerate(s):
            if ch == "#":
                word_len = s[start_idx:i]
                if not word_len.isnumeric():
                    continue
                word_len = int(word_len)
                words.append(s[i + 1: i + 1 + word_len])
                start_idx = i + 1 + word_len
        
        return words