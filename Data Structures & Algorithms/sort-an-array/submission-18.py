class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        results = []

        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                results.append(left[i])
                i += 1
            else:
                results.append(right[j])
                j += 1
        
        results.extend(left[i:])
        results.extend(right[j:])

        return results

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)