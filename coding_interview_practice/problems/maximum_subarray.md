# Problem 4: Maximum Subarray

**Difficulty:** Medium  
**Category:** Array, Dynamic Programming, Divide and Conquer  
**Company Tags:** Amazon, Microsoft, Google, Apple, LinkedIn

---

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

A **subarray** is a contiguous part of an array.

---

## Examples

### Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

### Example 2:
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

### Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Follow-up

If you have figured out the O(n) solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

---

## Hints

1. **Kadane's Algorithm**: Keep track of current sum and maximum sum
2. At each position, decide: continue current subarray or start new one?
3. If current sum becomes negative, reset it to 0
4. This is a classic dynamic programming problem

---

## Test Cases to Consider

1. **All positive**: [1,2,3,4,5]
2. **All negative**: [-5,-4,-3,-2,-1]
3. **Mixed**: [-2,1,-3,4,-1,2,1,-5,4]
4. **Single element**: [42]
5. **Zero included**: [0,1,2,0,-1]

---

## Your Task

Create a file `solutions/maximum_subarray.py` and implement:

```python
def max_subarray(nums: list[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of contiguous subarray
    """
    # Your code here
    pass


# Bonus: Return the actual subarray, not just the sum
def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """
    Find the maximum sum and the subarray indices.
    
    Args:
        nums: List of integers
        
    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    # Your code here
    pass
```

**Key Concepts:**
- **Kadane's Algorithm**: O(n) time, O(1) space
- Dynamic Programming: Build solution from subproblems
- Greedy approach: Make locally optimal choices
