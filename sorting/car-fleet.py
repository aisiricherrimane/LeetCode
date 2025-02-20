class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = sorted(zip(position, speed))

        times = [(target - p)/ s for p, s in data]
        count = 0

        while len(times) > 1:
            lead = times.pop()

            if lead < times[-1]:
                count += 1

            else:
                times[-1] = lead
        return count + len(times)
        