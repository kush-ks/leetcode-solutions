class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: 
            return None

        lower, higher = [], []
        ptr = head

        while ptr:
            if ptr.val < x: lower.append(ptr.val)
            else:           higher.append(ptr.val)
            ptr = ptr.next
        
        ptr = head
        m,n = len(lower), len(higher)

        for i in range(m):
            ptr.val = lower[i]
            ptr = ptr.next
        for i in range(n):
            ptr.val = higher[i]
            ptr = ptr.next

        return head