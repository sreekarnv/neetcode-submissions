class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_mapper = {0: 1}
        prefix_sum = 0

        for n in nums:
            prefix_sum += n
            delta_sum = prefix_sum - k
            if delta_sum in prefix_mapper:
                result += prefix_mapper[delta_sum]

            prefix_mapper[prefix_sum] = 1 + prefix_mapper.get(prefix_sum, 0)

        return result