class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i, n in enumerate(nums):

            if i > 0 and n == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = n + nums[l] + nums[r]

                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    results.append((n, nums[l], nums[r]))
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return results