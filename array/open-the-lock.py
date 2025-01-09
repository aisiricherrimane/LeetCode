class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        q = deque()
        q.append(['0000', 0])
        visit = set(deadends)

        def children(n):
            res = []
            for i in range(4):
                digit = str((int(n[i]) + 1) % 10)
                res.append(n[:i] + digit + n[i + 1:])
                digit = str((int(n[i]) - 1 + 10) % 10)
                res.append(n[:i] + digit + n[i + 1:])
            return res



        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns
            for number in children(lock):
                if number not in visit:
                    visit.add(number)
                    q.append([number, turns + 1])
        return -1
