class Solution:
    def merge(self, left: List[int], right: List[int]):
        final = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                final.append(left[i])
                i += 1
            else:
                final.append(right[j])
                j += 1
        
        final.extend(left[i:])
        final.extend(right[j:])

        return final

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        left_sort = self.mergeSort(left)
        right_sort = self.mergeSort(right)

        return self.merge(left_sort, right_sort)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)