"""
Test suite for Two Sum problem
Run with: python -m pytest coding_interview_practice/tests/test_two_sum.py -v
"""
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "solutions"))

try:
    from two_sum import two_sum
except ImportError:
    def two_sum(nums, target):
        """Placeholder function if solution not implemented yet."""
        raise NotImplementedError("Please implement two_sum function in solutions/two_sum.py")


def test_basic_case():
    """Test basic case with solution in middle."""
    result = two_sum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"


def test_different_positions():
    """Test with solution at different positions."""
    result = two_sum([3, 2, 4], 6)
    assert sorted(result) == [1, 2], f"Expected [1, 2], got {result}"


def test_duplicate_values():
    """Test with duplicate values in array."""
    result = two_sum([3, 3], 6)
    assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"


def test_negative_numbers():
    """Test with negative numbers."""
    result = two_sum([-1, -2, -3, -4, -5], -8)
    assert sorted(result) == [2, 4], f"Expected [2, 4], got {result}"


def test_with_zero():
    """Test with zero in array."""
    result = two_sum([0, 4, 3, 0], 0)
    assert sorted(result) == [0, 3], f"Expected [0, 3], got {result}"


def test_large_numbers():
    """Test with large numbers."""
    result = two_sum([1000000000, 2000000000, 3000000000], 5000000000)
    assert sorted(result) == [1, 2], f"Expected [1, 2], got {result}"


if __name__ == "__main__":
    print("Running Two Sum tests...\n")
    tests = [
        ("Basic case", test_basic_case),
        ("Different positions", test_different_positions),
        ("Duplicate values", test_duplicate_values),
        ("Negative numbers", test_negative_numbers),
        ("With zero", test_with_zero),
        ("Large numbers", test_large_numbers),
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
