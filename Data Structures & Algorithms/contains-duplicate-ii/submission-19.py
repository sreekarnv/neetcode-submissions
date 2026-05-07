class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0

        seen = set()

        while r < len(nums):
            while nums[r] in seen:
                if r - l <= k:
                    return True
                else:
                    seen.remove(nums[l])
                    l += 1
            
            seen.add(nums[r])
            r += 1
        
        return False