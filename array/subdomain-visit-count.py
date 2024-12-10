class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        temp = defaultdict(int)
        for domain in cpdomains:
            count, dom = domain.split(' ')
            frags = dom.split('.')
            for i in range(len(frags)):
                temp['.'.join(frags[i:])] += int(count)
        res = []
        for domain, count in temp.items():
            res.append('{} {}'.format(count, domain))
        return res

        
