class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.child = [1] * n

    def find(self,n):
        n = self.par[n]
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self,n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.child[p1] > self.child[p2]:
            self.child[p1] += 1
            self.par[p2] = p1
        else:
            self.child[p2] += 1
            self.par[p1] = p2
        return True
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailtoacc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoacc:
                    uf.union(emailtoacc[e], i)
                else:
                    emailtoacc[e] = i
        
        emailgroup = defaultdict(list)
        print(emailgroup)

        for e, i in emailtoacc.items():
            leader = uf.find(i)
            emailgroup[leader].append(e)
        
        res = []
        for leader_i, emails in emailgroup.items():
            name = accounts[leader_i][0]
            res.append([name] + sorted(emails))
        return res


        