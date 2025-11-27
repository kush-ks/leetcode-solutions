class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        queue = deque()
        curr, nextCurr = 0, 1
        st, ans = [], []
        ltr = False

        queue.append(root)

        while queue:
            arr = []
            curr = nextCurr
            nextCurr = 0
            ltr = not ltr
            
            for _ in range(curr):
                node = queue.popleft()
                arr.append(node.val)
                
                if ltr:
                    if node.left:   st.append(node.left);   nextCurr += 1
                    if node.right:  st.append(node.right);  nextCurr += 1
                else:
                    if node.right:  st.append(node.right);  nextCurr += 1
                    if node.left:   st.append(node.left);   nextCurr += 1
                
            while st:
                queue.append(st.pop())
            
            ans.append(arr)


        return ans                    