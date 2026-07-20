class Solution:
    def isPalindrome(self, s: str, l = 0, r = None) -> bool:
        if r == None:
            r = len(s) - 1

        while l < r:
            if not s[l] == s[r]: return False

            l += 1
            r -= 1

        return True
        
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s): return True

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l] == s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            
            l += 1
            r -= 1
        
        return True