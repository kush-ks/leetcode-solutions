class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(ptr):
            nonlocal isFound, wanted
            if not ptr or isFound: return
            if ptr.val in wanted:
                isFound = True
                return
            
            wanted.add(k-ptr.val)

            if not isFound: inorder(ptr.left)
            if not isFound: inorder(ptr.right)

        
        wanted = set()
        isFound = False
        inorder(root)

        return isFound