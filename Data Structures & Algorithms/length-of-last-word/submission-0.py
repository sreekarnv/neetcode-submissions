class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        prev = None
        count = 0

        for ch in s:
            if ch == " ":
                if count > 0:
                    prev = count
                count = 0
            else:
                count += 1
        
        return prev if count == 0 else count