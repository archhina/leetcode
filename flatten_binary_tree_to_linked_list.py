# 114. Flatten Binary Tree to Linked List

def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return

    queue = deque([root])
    new = deque()

    while queue:
        for i in range(len(queue)):
            visit = queue.pop()
            new.append(visit.val)

            if visit.right:
                queue.append(visit.right)
            if visit.left:
                queue.append(visit.left)
    
    tmp = root
    new.popleft()
    for i in range(len(new)):
        tmp.right = TreeNode(new.popleft())
        tmp.left = None
        tmp = tmp.right