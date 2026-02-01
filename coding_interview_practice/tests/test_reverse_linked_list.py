"""
Test suite for Reverse Linked List problem
Run with: python -m pytest coding_interview_practice/tests/test_reverse_linked_list.py -v
"""
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "solutions"))

try:
    from reverse_linked_list import ListNode, reverse_list, create_linked_list, linked_list_to_list
except ImportError:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def reverse_list(head):
        """Placeholder function if solution not implemented yet."""
        raise NotImplementedError("Please implement reverse_list function in solutions/reverse_linked_list.py")


def test_multiple_nodes():
    """Test reversing list with multiple nodes."""
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    result = linked_list_to_list(reversed_head)
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"


def test_two_nodes():
    """Test reversing list with two nodes."""
    head = create_linked_list([1, 2])
    reversed_head = reverse_list(head)
    result = linked_list_to_list(reversed_head)
    assert result == [2, 1], f"Expected [2, 1], got {result}"


def test_empty_list():
    """Test reversing empty list."""
    head = create_linked_list([])
    reversed_head = reverse_list(head)
    result = linked_list_to_list(reversed_head)
    assert result == [], f"Expected [], got {result}"


def test_single_node():
    """Test reversing list with single node."""
    head = create_linked_list([1])
    reversed_head = reverse_list(head)
    result = linked_list_to_list(reversed_head)
    assert result == [1], f"Expected [1], got {result}"


def test_negative_values():
    """Test reversing list with negative values."""
    head = create_linked_list([-1, -2, -3])
    reversed_head = reverse_list(head)
    result = linked_list_to_list(reversed_head)
    assert result == [-3, -2, -1], f"Expected [-3, -2, -1], got {result}"


if __name__ == "__main__":
    print("Running Reverse Linked List tests...\n")
    tests = [
        ("Multiple nodes", test_multiple_nodes),
        ("Two nodes", test_two_nodes),
        ("Empty list", test_empty_list),
        ("Single node", test_single_node),
        ("Negative values", test_negative_values),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✅ {test_name}: PASSED")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name}: FAILED - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'='*50}")
