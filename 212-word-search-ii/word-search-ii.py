class TrieNode:
    def __init__(self):
        

        self.children = {}
        self.isword = False
    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isword = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        root = TrieNode()
        for w in words:
            root.addword(w)
        r, c = len(board), len(board[0])
        res, visit = set(), set()
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def valid(i, j):
            return 0<= i < len(board) and 0<=j <len(board[i])
        ans = set()
        # print(root.children)
        def back(i, j, node, word, visit):
            # print(i, j , node.children , word)
            if node.isword:
                ans.add(word)
            for dr, dc, in dir:
                nr, nc, = i+ dr, j + dc
                # print("nr, nc", nr, nc, i, j, node.children)
                if valid(nr, nc) and board[nr][nc] in node.children and (nr, nc) not in visit:
                    # print("nr, nc", nr, nc, i, j)

                    letter = board[nr][nc]
                    visit.add(( nr, nc))
                    node2 = node
                    back(nr, nc, node2.children[letter], word+letter,visit)
                    visit.remove((nr, nc))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in root.children:
                    # print("call ", i, j)
                    visit = set()
                    visit.add((i , j))
                    back(i, j, root.children[board[i][j]], board[i][j], visit)
        return(list(ans))



        