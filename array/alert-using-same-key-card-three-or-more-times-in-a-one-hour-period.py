from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def time_to_hour(time):
            hr, m = time.split(':')
            hr = int(hr)
            m = int(m)
            return hr * 60 + m
        
        check_in = defaultdict(list)
        for i in range(len(keyName)):
            check_in[keyName[i]].append(time_to_hour(keyTime[i]))
        res = []
        for person, times in check_in.items():
            times = sorted(times)
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    res.append(person)
                    break
        return res

            
        