class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for n in nums:
            if not n == val:
                nums[l] = n
                l += 1
        
        return l