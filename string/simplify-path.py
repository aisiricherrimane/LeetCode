class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif not p or p == '.':
                continue
            else:
                stack.append(p)
        final = '/' + '/'.join(stack)
        return final
            