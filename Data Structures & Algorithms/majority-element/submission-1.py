class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = None
        count = 0

        for n in nums:
            if count == 0:
                elem = n
                count += 1
            else:
                if elem == n:
                    count += 1
                else:
                    count -= 1
        
        return elem