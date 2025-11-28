class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        k = right - left + 1
        ptr = head

        for _ in range(left-2):
            ptr = ptr.next
        
        leftTail = None
        if left > 1: 
            leftTail = ptr
            ptr = ptr.next
        
        prev = None
        rev = ptr
        for i in range(k):
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
            if left == 1 and i == k-1:
                head = prev 
        
        rightTail = ptr
        if leftTail: 
            leftTail.next = prev
        if rightTail:
            rev.next = rightTail

        return head