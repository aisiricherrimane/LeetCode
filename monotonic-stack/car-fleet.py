class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]
        count = 0

        while len(times) > 1:
            lead = times.pop()

            if lead < times[-1]:
                count += 1
            else:
                times[-1] = lead
        return  count +len(times)
        
     
