# Problem 1: Two Sum

**Difficulty:** Easy  
**Category:** Arrays, Hash Table  
**Company Tags:** Amazon, Google, Microsoft, Facebook, Apple

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

## Examples

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

## Follow-up

Can you come up with an algorithm that is less than O(n²) time complexity?

---

## Hints

1. Think about what you need to find: `target - current_number`
2. Can you store something to make lookups faster?
3. Hash tables provide O(1) lookup time
4. You can solve this in a single pass through the array

---

## Test Cases to Consider

1. **Basic case**: Standard array with solution
2. **Duplicate values**: Array with same number appearing twice
3. **Negative numbers**: Mix of positive and negative numbers
4. **Zero values**: Array containing zeros
5. **Large numbers**: Test with constraint limits

---

## Your Task

Create a file `solutions/two_sum.py` and implement:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers
    """
    # Your code here
    pass
```

**Good luck! Remember to:**
1. Think about edge cases
2. Consider time and space complexity
3. Test your solution
4. Ask for feedback when ready
