class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []

        for j, m in enumerate(nums):
            if j > 0 and m == nums[j - 1]:
                continue
            
            for i in range(j + 1, len(nums)):
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue
                
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    curr = nums[j] + nums[i] + nums[l] + nums[r]
                    if curr > target: r -= 1
                    elif curr < target: l += 1
                    else:
                        results.append((nums[j], nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                
        return results
