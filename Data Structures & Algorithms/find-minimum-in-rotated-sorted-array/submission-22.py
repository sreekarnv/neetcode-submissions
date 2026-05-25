class Solution:
    def findMin(self, nums: List[int]) -> int:
        minvalue = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            minvalue = min(minvalue, nums[mid])

            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return minvalue