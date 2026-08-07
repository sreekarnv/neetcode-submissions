class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)


        fleets = 0
        max_time = 0

        for p, s in cars:
            t = (target - p) / s

            if max_time < t:
                fleets += 1
                max_time = t
        
        return fleets