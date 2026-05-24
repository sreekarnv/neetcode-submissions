class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        min_val = nums[0]

        while l <= r:
            mid = (l + r) // 2
            min_val = min(min_val, nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return min_val