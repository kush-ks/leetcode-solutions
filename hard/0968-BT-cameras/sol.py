UNMONITORED, CAMERA, MONITORED = -1,0,1

class Solution:
    def __init__(self):
        self.cams = 0


    def postorder(self, ptr):
        if not ptr:
            return None
        
        l = self.postorder(ptr.left)
        r = self.postorder(ptr.right)
        
        if l==UNMONITORED or r==UNMONITORED:
            self.cams += 1
            return CAMERA
        
        if l==CAMERA or r==CAMERA:
            return MONITORED
        
        return UNMONITORED


    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        x = self.postorder(root)
        if x==UNMONITORED:
            self.cams += 1
        
        return self.cams