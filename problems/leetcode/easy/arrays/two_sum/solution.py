"""
Two Sum - Solution

Approach: Hash Map
- Iterate through array once
- For each element, check if complement (target - element) was seen
- If not, store current element in hash map
- Return indices when complement found

Time Complexity: O(n)
Space Complexity: O(n) for hash map
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        Indices [i, j] where nums[i] + nums[j] == target
    """
    # Map value to its index
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement already seen
        if complement in seen:
            return [seen[complement], i]
        
        # Store current number
        seen[num] = i
    
    # Should not reach here given problem guarantees
    return []


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    # Test case 1
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    print("✓ Test 1 passed")
    
    # Test case 2
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("✓ Test 2 passed")
    
    # Test case 3
    assert two_sum([3, 3], 6) == [0, 1]
    print("✓ Test 3 passed")
    
    # Edge case: negative numbers
    assert two_sum([-1, -2, -3, 5, 10], 9) == [1, 4]
    print("✓ Test 4 passed (negative numbers)")
    
    # Edge case: minimum array size
    assert two_sum([1, 2], 3) == [0, 1]
    print("✓ Test 5 passed (minimum size)")
    
    print("\n✓ All tests passed!")
