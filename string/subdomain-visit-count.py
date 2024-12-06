class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        temp = defaultdict(int)

        for domain in cpdomains:
            count, dom = domain.split(' ')
            count = int(count)
            frags = dom.split('.')
            for i in range(len(frags)):
                temp['.'.join(frags[i:])] += count
        ans = []
        for dom, cnt in temp.items():
            ans.append('{} {}'.format(cnt, dom))
        return ans


