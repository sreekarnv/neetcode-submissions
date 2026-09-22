class Solution:
    def findMin(self, nums: List[int]) -> int:
        val = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            val = min(nums[mid], val)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return val