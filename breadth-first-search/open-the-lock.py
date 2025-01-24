class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(number):
            res = []
            for i in range(4):
                digit = str((int(number[i]) + 1) % 10)
                res.append(number[:i] + digit + number[i + 1:])
                digit = str((int(number[i]) - 1 + 10) % 10)
                res.append(number[:i] + digit + number[i + 1:])
            return res


        q = deque([('0000', 0)])
        visit = set(deadends)

        while q:
            number, turns = q.popleft()

            if number == target:
                return turns
            
            for n in children(number):
                if n not in visit:
                    q.append([n, turns + 1])
                    visit.add(n)
        return -1
            
        