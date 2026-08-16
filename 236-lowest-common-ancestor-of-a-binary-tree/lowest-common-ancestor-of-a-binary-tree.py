# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        parents list for both p and q
        find the first matching parent (parent that exists in both lists)
            1
        2       3
        p=2; q=3
        root node _  2 return that p true 
        root knows it has seen p , then it calls 3 
        three returns that it has seen q 
        the root know it has seen both

            2
        1       3
        p=2; q=3
        
        root node checks if it is p or q, p becomes true for the root 
        the it calls  1  one returns false for both  p and q 
        it calls 3  , 3 returnrs true for q and false for p 
        
        p=6; q=4
        root node -> 5 
        5 ->6
        6-> true , false
        5 -> 2
        7 ->false, false
        4> false , True
        
        5 > True, True,node
        """
        def dfs(node):
            seenP, seenQ, lca, = False, False , None
            if node == p:
                seenP = True
            if node == q:
                seenQ = True
            if node.left:
                rp, rq, rlca = dfs(node.left) # for 5 False, False, None
                seenP |= rp
                seenQ |= rq
                if lca is None:
                    lca = rlca
            if node.right:
                rp, rq, rlca = dfs(node.right)
                seenP |= rp
                seenQ |= rq
                if lca is None:
                    lca = rlca
            
            if seenP and seenQ and lca is None: 
                # print(node)
                lca = node
            return seenP , seenQ, lca
        if root is None:
            return None
        rp , rq, rlca  = dfs(root)
        return rlca
            
                
                