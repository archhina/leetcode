# 61. Rotate List

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if  head == None or k == 0:
        return head

    curr = head
    stack = deque()

    while curr:
        stack.append(curr.val)
        curr = curr.next
    
    k = k%len(stack)
    stack.rotate(k)

    head = ListNode(stack.popleft())
    pointer = head
    for i in range(len(stack)):
        pointer.next = ListNode(stack.popleft())
        pointer = pointer.next
    
    return head