#104. Maximum Depth of Binary Tree

from collections import deque


def maxDepth(root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        depth = 0
        queue = deque([root])
        
        while queue:
            curr_level_nodes = len(queue)
            for i in range(curr_level_nodes):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            depth += 1
        return depth


if __name__ == "__main__":
    print(maxDepth([3,9,20,null,null,15,7]))