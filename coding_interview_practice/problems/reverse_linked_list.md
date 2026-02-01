# Problem 3: Reverse Linked List

**Difficulty:** Easy  
**Category:** Linked List, Recursion  
**Company Tags:** Amazon, Microsoft, Apple, Facebook, Google

---

## Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

---

## Examples

### Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

### Example 2:
```
Input: head = [1,2]
Output: [2,1]
```

### Example 3:
```
Input: head = []
Output: []
```

---

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Follow-up

A linked list can be reversed either iteratively or recursively. Could you implement both?

---

## Hints

1. **Iterative approach**: Use three pointers (prev, current, next)
2. **Recursive approach**: Think about reversing the rest and then fixing pointers
3. Make sure to handle the edge case of empty list
4. Draw it out on paper!

---

## Test Cases to Consider

1. **Empty list**: None or []
2. **Single node**: [1]
3. **Two nodes**: [1,2]
4. **Multiple nodes**: [1,2,3,4,5]

---

## Your Task

Create a file `solutions/reverse_linked_list.py` and implement:

```python
class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    Reverse a singly linked list.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    # Your code here
    pass


# Bonus: Implement recursive version
def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    """
    Reverse a singly linked list recursively.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    # Your code here
    pass
```

**Interview Tips:**
- Explain your approach before coding
- Draw diagrams to visualize pointer changes
- Consider edge cases (empty, single node)
- Discuss both iterative and recursive approaches
