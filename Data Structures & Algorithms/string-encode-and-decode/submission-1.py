class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        words = []

        i = 0

        while i < len(s):
            j = i

            while not s[j] == "#":
                j += 1
            
            word_len = int(s[i:j])
            start = j + 1
            end = start + word_len

            word = s[start:end]
            words.append(word)
            i = end
        
        return words