from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        temp = {i:[] for i in keyName}
        def time_convert(time):
            hr, mn = time.split(':')
            return ((int(hr) * 60) + int(mn))
        
        for i in range(len(keyName)):
            temp[keyName[i]].append(time_convert(keyTime[i]))
        res = []
        for person, times in temp.items():
            times = sorted(times)
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    res.append(person)
                    break
        return sorted(res)



        