class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += f"{len(s)}#{s}"
        
        return word

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        for j, ch in enumerate(s):
            if ch == "#":
                word_len = s[i:j]
                if not word_len.isnumeric():
                    continue
                
                word_len = int(word_len)
                word = s[j + 1:j + 1 + word_len]
                i = j + 1 + word_len

                words.append(word)
        
        return words