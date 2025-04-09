# 21. Merge Two Sorted Lists

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    res = []

    curr = list1
    while curr:
        res.append(curr.val)
        curr = curr.next
    curr = list2
    while curr:
        res.append(curr.val)
        curr = curr.next

    res.sort()

    if len(res) == 0:
        return
    head = ListNode(res[0])
    curr = head
    for i in res[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head