class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTrie(words):
            root = {}
            for word in words:
                node = root
                for char in word:  # Iterate through characters of the word
                    node = node.setdefault(char, {})
                node['#'] = word  # Mark the end of a word
            return root

        Trie = buildTrie(words)
        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            letter = board[r][c]
           
            
            next_node = node[letter]
            if '#' in next_node:  # Word found
                res.append(next_node['#'])
                del next_node['#']  # Avoid duplicates
            
            board[r][c] = ''  # Mark as visited
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node:
                    dfs(nr, nc, next_node)
            board[r][c] = letter  # Restore original value
            
            if not next_node:  # Clean up Trie node
                node.pop(letter)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in Trie:
                    dfs(r, c, Trie)

        return res
