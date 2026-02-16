# Problem: Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

## Examples

### Example 1
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

### Example 2
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6
```

### Example 3
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: nums[0] + nums[1] = 3 + 3 = 6
```

## Key Observations

1. **Complementary pair**: If we pick element x, we need target - x
2. **Hash table enables O(1) lookup**: Check if complement exists as we iterate
3. **Indices matter**: Must return indices, not values
4. **Order doesn't matter**: [0, 1] or [1, 0] both valid
5. **Exactly one solution exists**: No ambiguity in answer

## Approaching the Solution

### Brute Force
**Approach**: Check every pair
**Complexity**: O(n²) time, O(1) space
**Verdict**: Too slow for n = 10⁴

### Optimal Approach
**Approach**: Hash map to track seen numbers
**Complexity**: O(n) time, O(n) space
**Verdict**: Passes constraints

## Related Topics

- Hash Table
- Array
- Two Pointers (alternative approach)

## Difficulty Assessment

**Difficulty**: Easy
**Acceptance Rate**: ~47%
**Key Skill**: Hash table usage

