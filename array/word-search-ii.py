class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTree(words):
            def TrieNode():
                return defaultdict(TrieNode)
            
            root = TrieNode()
            for word in words:
                node = root
                for letter in word:
                    node = node[letter]
                node['#'] = word
            return root
        
        Trie = buildTree(words)
        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c, node):
            letter = board[r][c]
            
            if letter not in node:
                return 
            next_node = node[letter]

            if '#' in next_node:
                res.append(next_node['#'])
                del next_node['#']
            
            board[r][c] = ''
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                R, C = dr + r, dc + c
                if 0 <= R < rows and 0 <= C < cols and board[R][C] in next_node:
                    dfs(R, C, next_node)
            board[r][c] = letter

            if not next_node:
                node.pop(letter)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in Trie:
                    dfs(r, c, Trie)
        return res

         