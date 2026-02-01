# Problem 5: Binary Tree Level Order Traversal

**Difficulty:** Medium  
**Category:** Tree, Breadth-First Search, Binary Tree  
**Company Tags:** Amazon, Microsoft, Facebook, Apple, Bloomberg

---

## Problem Statement

Given the `root` of a binary tree, return the **level order traversal** of its nodes' values. (i.e., from left to right, level by level).

---

## Examples

### Example 1:
```
Input: root = [3,9,20,null,null,15,7]
        3
       / \
      9  20
        /  \
       15   7
Output: [[3],[9,20],[15,7]]
```

### Example 2:
```
Input: root = [1]
Output: [[1]]
```

### Example 3:
```
Input: root = []
Output: []
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

## Hints

1. Use **Breadth-First Search (BFS)** with a queue
2. Use a queue to process nodes level by level
3. Track the size of each level to group nodes correctly
4. Can also use recursion with depth tracking

---

## Test Cases to Consider

1. **Empty tree**: None
2. **Single node**: Just root
3. **Complete binary tree**: All levels filled
4. **Unbalanced tree**: Only left or right children
5. **Perfect binary tree**: All leaves at same level

---

## Your Task

Create a file `solutions/binary_tree_level_order.py` and implement:

```python
class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    """
    Return level order traversal of binary tree.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of lists, where each inner list contains values at that level
    """
    # Your code here
    pass
```

**Interview Tips:**
- BFS uses a queue (FIFO)
- DFS uses a stack (LIFO) or recursion
- Explain why BFS is natural for level-order traversal
- Discuss time O(n) and space O(n) complexity
