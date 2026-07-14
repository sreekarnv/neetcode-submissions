class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        value = nums[0]

        while l <= r:
            mid = (l + r) // 2
            value = min(nums[mid], value)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return value