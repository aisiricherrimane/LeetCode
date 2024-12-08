class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(int)

        for temp in cpdomains:
            count, dom = temp.split(' ')
            count = int(count)
            frags = dom.split('.')
            for i in range(len(frags)):
                store['.'.join(frags[i:])] += count
        ans = []
        for dom, cnt in store.items():
            ans.append('{} {}'.format(cnt, dom))
        return ans
