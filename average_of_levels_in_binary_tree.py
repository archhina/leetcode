# 637. Average of Levels in Binary Tree

def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
    queue = deque([root])
    res = []

    while queue:
        total = 0
        nodes = len(queue)
        for i in range(nodes):
            visit = queue.popleft()
            total += visit.val
            if visit.left:
                queue.append(visit.left)
            if visit.right:
                queue.append(visit.right)
        res.append(total/nodes)

    return res