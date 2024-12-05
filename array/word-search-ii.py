class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildtree(words):
            def trieNode():
                return defaultdict(trieNode)
            root = trieNode()
            for word in words:
                node = root
                for letter in word:
                    node = node[letter]
                node['#'] = word
            return root
        Trie = buildtree(words)
        rows, cols = len(board), len(board[0])
        res = [ ]

        def dfs(r, c, section):
            letter = board[r][c]

            if letter not in section:
                return 
            
            next_node = section[letter]

            if '#' in next_node:
                res.append(next_node['#'])
                del next_node["#"] 
            board[r][c] = ''

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                R, C = r + dr, c + dc
                if 0 <= R < rows and 0 <= C < cols and board[R][C] in next_node:
                    dfs(R, C, next_node)

            board[r][c] = letter

            if not next_node:
                section.pop(letter)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in Trie:
                    dfs(r, c, Trie)
        return res