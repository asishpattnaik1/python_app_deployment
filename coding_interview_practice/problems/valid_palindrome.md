# Problem 2: Valid Palindrome

**Difficulty:** Easy  
**Category:** Two Pointers, String  
**Company Tags:** Facebook, Microsoft, Amazon, Bloomberg

---

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Examples

### Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

---

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Hints

1. Two pointers approach: one from start, one from end
2. Skip non-alphanumeric characters
3. Compare characters case-insensitively
4. Can you do this with O(1) extra space?

---

## Test Cases to Consider

1. **Pure palindrome**: "racecar"
2. **With spaces and punctuation**: "A man, a plan, a canal: Panama"
3. **Empty or single character**: "", "a"
4. **No letters**: ",.;"
5. **Mixed case**: "RaceCar"
6. **With numbers**: "A1b2B1a"

---

## Your Task

Create a file `solutions/valid_palindrome.py` and implement:

```python
def is_palindrome(s: str) -> bool:
    """
    Check if string is a valid palindrome.
    
    Args:
        s: Input string
        
    Returns:
        True if palindrome, False otherwise
    """
    # Your code here
    pass
```

**Tips:**
- Think about the two-pointer technique
- Consider using Python's `.isalnum()` and `.lower()` methods
- Can you solve without creating a new cleaned string?
