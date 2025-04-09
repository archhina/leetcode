# 2. Add Two Numbers

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
    res = deque()

    num1 = ""
    num2 = ""

    while l1:
        num1 = str(l1.val) + num1
        l1 = l1.next

    while l2:
        num2 = str(l2.val) + num2
        l2 = l2.next    
    
    sol = int(num1) + int(num2)
    for x in str(sol):
        res.append(int(x))
    
    res_list = ListNode(res.pop())
    res_head = res_list

    for i in range(len(res)):
        res_list.next = ListNode(res.pop())
        res_list = res_list.next
    
    return res_head