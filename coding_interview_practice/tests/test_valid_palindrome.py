"""
Test suite for Valid Palindrome problem
Run with: python -m pytest coding_interview_practice/tests/test_valid_palindrome.py -v
"""
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "solutions"))

try:
    from valid_palindrome import is_palindrome
except ImportError:
    def is_palindrome(s):
        """Placeholder function if solution not implemented yet."""
        raise NotImplementedError("Please implement is_palindrome function in solutions/valid_palindrome.py")


def test_classic_palindrome():
    """Test classic palindrome with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True


def test_not_palindrome():
    """Test string that is not a palindrome."""
    assert is_palindrome("race a car") == False


def test_empty_string():
    """Test empty string after removing non-alphanumeric."""
    assert is_palindrome(" ") == True


def test_simple_word():
    """Test simple palindrome word."""
    assert is_palindrome("racecar") == True


def test_mixed_case():
    """Test with mixed case letters."""
    assert is_palindrome("RaceCar") == True


def test_with_numbers():
    """Test palindrome with numbers."""
    assert is_palindrome("A1b2B1a") == True


def test_single_character():
    """Test single character."""
    assert is_palindrome("a") == True


def test_only_punctuation():
    """Test string with only punctuation."""
    assert is_palindrome(".,;") == True


def test_complex_palindrome():
    """Test more complex palindrome."""
    assert is_palindrome("Was it a car or a cat I saw?") == True


def test_not_palindrome_with_numbers():
    """Test non-palindrome with numbers."""
    assert is_palindrome("0P") == False


if __name__ == "__main__":
    print("Running Valid Palindrome tests...\n")
    tests = [
        ("Classic palindrome", test_classic_palindrome),
        ("Not palindrome", test_not_palindrome),
        ("Empty string", test_empty_string),
        ("Simple word", test_simple_word),
        ("Mixed case", test_mixed_case),
        ("With numbers", test_with_numbers),
        ("Single character", test_single_character),
        ("Only punctuation", test_only_punctuation),
        ("Complex palindrome", test_complex_palindrome),
        ("Not palindrome with numbers", test_not_palindrome_with_numbers),
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
