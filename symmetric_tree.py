# 101. Symmetric Tree

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
    if not root.right and not root.left:
        return True
    elif not root.right or not root.left:
        return False
    left = deque([root.left])
    right = deque([root.right])

    while right and left:
        
        visit_left = left.popleft()
        visit_right = right.popleft()
        if visit_left.val != visit_right.val:
            return False

        if visit_left.left and visit_right.right:
            left.append(visit_left.left)
            right.append(visit_right.right)
        elif visit_left.left or visit_right.right:
            return False

        if visit_left.right and visit_right.left:
            left.append(visit_left.right)
            right.append(visit_right.left)
        elif visit_left.right or visit_right.left:
            return False
        
    return True