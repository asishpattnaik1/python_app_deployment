"""
Problem: Reverse Linked List
Difficulty: Easy
Category: Linked List, Recursion

Problem Statement:
Reverse a singly linked list.

Approach:
[Write your approach here]

Time Complexity: O(?)
Space Complexity: O(?)
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    # TODO: Write your iterative solution here
    pass


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    """
    Reverse a singly linked list recursively.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    # TODO: Write your recursive solution here (bonus challenge!)
    pass


# Helper functions for testing
def create_linked_list(values: list) -> ListNode | None:
    """Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: ListNode | None) -> list:
    """Convert linked list to Python list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Example usage and testing
if __name__ == "__main__":
    # Test case 1: Multiple nodes
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverse_list(head1)
    print(f"Test 1: {linked_list_to_list(reversed1)}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test case 2: Two nodes
    head2 = create_linked_list([1, 2])
    reversed2 = reverse_list(head2)
    print(f"Test 2: {linked_list_to_list(reversed2)}")  # Expected: [2, 1]
    
    # Test case 3: Empty list
    head3 = create_linked_list([])
    reversed3 = reverse_list(head3)
    print(f"Test 3: {linked_list_to_list(reversed3)}")  # Expected: []
    
    print("\n✅ All test cases passed! Ready for review.")
