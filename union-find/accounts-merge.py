class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, e1, e2):
        p1 = self.find(e1)
        p2 = self.find(e2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_ind = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_ind:
                    uf.union(i, email_to_ind[e])
                else:
                    email_to_ind[e] = i
        
        emailGroup = collections.defaultdict(list)
        for e, i in email_to_ind.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i])) # array concat
        return res



        