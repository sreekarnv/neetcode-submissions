class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0

        mapper = {}

        l = 0
        r = 0

        while r < len(fruits):
            mapper[fruits[r]] = 1 + mapper.get(fruits[r], 0)

            if len(mapper) > 2:
                mapper[fruits[l]] -= 1
                if mapper[fruits[l]] == 0:
                    del mapper[fruits[l]]
                
                l += 1
            
            max_fruits = max(max_fruits, r - l + 1)
            r += 1
        
        return max_fruits