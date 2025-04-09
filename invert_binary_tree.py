# 226. Invert Binary Tree

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root:
        return None

    queue = deque([root])

    while queue:

        for i in range(len(queue)):
            curr = queue.popleft()

            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return root