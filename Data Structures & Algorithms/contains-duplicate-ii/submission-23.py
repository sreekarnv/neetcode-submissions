class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0

        seen = set()

        while r < len(nums):
            if r - l > k:
                if nums[l] in seen:
                    seen.remove(nums[l])
                    l += 1
                continue
            
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            r += 1
        
        return False