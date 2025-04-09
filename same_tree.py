# 100. Same Tree

from collections import deque
from typing import Optional


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
    if not p and not q:
        return True
    elif not p or not q:
        return False

    bfs_p = deque([p])
    bfs_q = deque([q])

    while bfs_p and bfs_q:
        if len(bfs_p) != len(bfs_q):
            return False
        for i in range(len(bfs_p)):
            visit_p = bfs_p.popleft()
            visit_q = bfs_q.popleft()
            if visit_p.val != visit_q.val:
                return False
            if visit_p.right:
                if visit_q.right:
                    bfs_q.append(visit_q.right)
                else:
                    return False
                bfs_p.append(visit_p.right)                
            if visit_p.left:
                if visit_q.left:
                    bfs_q.append(visit_q.left)
                else:
                    return False
                bfs_p.append(visit_p.left)
            
            if visit_q.right:
                if visit_p.right:
                    bfs_p.append(visit_p.right)
                else:
                    return False
                bfs_q.append(visit_q.right)                
            if visit_q.left:
                if visit_p.left:
                    bfs_p.append(visit_p.left)
                else:
                    return False
                bfs_q.append(visit_q.left)
    
    return True