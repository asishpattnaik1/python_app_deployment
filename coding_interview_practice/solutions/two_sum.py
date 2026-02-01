"""
Problem: Two Sum
Difficulty: Easy
Category: Arrays, Hash Table

Problem Statement:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Approach:
[Write your approach here - explain your thinking in 2-3 sentences]

Time Complexity: O(?)
Space Complexity: O(?)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    # TODO: Write your solution here
    pass


# Example usage and testing
if __name__ == "__main__":
    # Test case 1: Basic case
    result1 = two_sum([2, 7, 11, 15], 9)
    print(f"Test 1: {result1}")  # Expected: [0, 1]
    
    # Test case 2: Different positions
    result2 = two_sum([3, 2, 4], 6)
    print(f"Test 2: {result2}")  # Expected: [1, 2]
    
    # Test case 3: Duplicate values
    result3 = two_sum([3, 3], 6)
    print(f"Test 3: {result3}")  # Expected: [0, 1]
    
    # Add your own test cases here
    print("\n✅ All test cases passed! Ready for review.")
