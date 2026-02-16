"""
Two Sum - Optimized Solution

Note: Hash map approach IS the optimal solution (O(n) time).
This file shows alternative approaches for learning.

ALTERNATIVE 1: Two Pointers (requires sorting)
- Sort array with index tracking
- Use two pointers from ends
- Adjust based on sum vs target

Time: O(n log n), Space: O(n) for index tracking
Advantage: Can find ALL pairs easily
Disadvantage: Doesn't match original indices directly
"""


def two_sum_two_pointers(nums: list[int], target: int) -> list[int]:
    """
    Two pointer approach (alternative).
    Note: This requires returning original indices after sorting.
    """
    # Create (value, original_index) pairs
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    
    # Sort by value
    indexed_nums.sort()
    
    # Two pointers
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


# ============================================================================
# COMPARISON
# ============================================================================

"""
HASH MAP vs TWO POINTER:

Hash Map:
+ O(n) time (optimal for single pair)
+ O(n) space
+ Single pass through array
- Can't easily find all pairs

Two Pointer:
+ Can find all pairs with slight modification
+ Sometimes clearer logic
- O(n log n) due to sorting
- Loses original indices (need careful tracking)
- Two passes through array

For this problem: Hash map is clearly superior.
For finding all pairs: Two pointer approach wins.
"""


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    # Test case 1
    assert two_sum_two_pointers([2, 7, 11, 15], 9) == [0, 1]
    print("✓ Test 1 passed")
    
    # Test case 2
    assert two_sum_two_pointers([3, 2, 4], 6) == [1, 2]
    print("✓ Test 2 passed")
    
    # Test case 3
    assert two_sum_two_pointers([3, 3], 6) == [0, 1]
    print("✓ Test 3 passed")
    
    print("\n✓ All two pointer tests passed!")
