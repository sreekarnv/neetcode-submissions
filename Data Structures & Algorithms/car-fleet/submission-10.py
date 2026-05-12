class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        count = 0
        max_time = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > max_time:
                max_time = time
                count += 1
        
        return count