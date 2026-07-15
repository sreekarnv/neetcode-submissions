class Solution:
    def findMin(self, nums: List[int]) -> int:
        value = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            value = min(value, nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return value
