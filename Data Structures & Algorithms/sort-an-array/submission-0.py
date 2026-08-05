class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        
        result.extend(nums1[i:])
        result.extend(nums2[j:])

        return result


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        right_sorted = self.sortArray(right)
        left_sorted = self.sortArray(left)

        return self.merge(left_sorted, right_sorted)