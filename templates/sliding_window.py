"""
Sliding Window Template

Two-pointer technique for efficient substring/subarray problems.
Maintains a window of elements and expands/contracts based on condition.

Use Cases:
- Substring problems (longest, shortest, count)
- Subarray with constraint (sum, product, character count)
- Anagram detection
- Duplicate removal

Time Complexity: O(n) - each element visited at most twice
Space Complexity: O(1) to O(k) depending on problem
"""

from typing import List, Dict, Tuple
from collections import defaultdict


# ============================================================================
# TEMPLATE 1: Basic Sliding Window Pattern
# ============================================================================

def sliding_window_basic(arr: List[int], k: int) -> List[int]:
    """
    Find maximum element in every window of size k.
    
    Args:
        arr: Input array
        k: Window size
        
    Returns:
        List of maximum in each window
    """
    if not arr or k > len(arr):
        return []
    
    result = []
    left = 0
    
    for right in range(len(arr)):
        # Window: [left, right]
        
        # Shrink window if it exceeds size k
        if right - left + 1 > k:
            left += 1
        
        # When window is exactly size k, process it
        if right - left + 1 == k:
            window_max = max(arr[left:right+1])
            result.append(window_max)
    
    return result


# ============================================================================
# TEMPLATE 2: Substring with Constraint (Character Count)
# ============================================================================

def longest_substring_without_repeating(s: str) -> int:
    """
    Find longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character seen and in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move left pointer past previous occurrence
            left = char_index[s[right]] + 1
        
        # Update last seen index of character
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Find longest substring with at most k distinct characters.
    """
    char_count = defaultdict(int)
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Add character to window
        char_count[s[right]] += 1
        
        # Shrink window if too many distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ============================================================================
# TEMPLATE 3: Subarray Sum Constraint
# ============================================================================

def min_subarray_length(target: int, nums: List[int]) -> int:
    """
    Find minimum length subarray with sum >= target.
    Works only for non-negative integers.
    
    Args:
        target: Target sum
        nums: Input array
        
    Returns:
        Minimum subarray length, or 0 if impossible
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        # Add current element
        current_sum += nums[right]
        
        # Shrink from left while condition satisfied
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0


def max_subarray_with_constraint(nums: List[int], max_sum: int) -> int:
    """
    Find maximum length subarray with sum <= max_sum.
    """
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Shrink if sum exceeds limit
        while current_sum > max_sum:
            current_sum -= nums[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ============================================================================
# TEMPLATE 4: Finding Anagram/Permutation in String
# ============================================================================

def find_anagram_substrings(s: str, p: str) -> List[int]:
    """
    Find all indices where anagram of p appears in s.
    
    Args:
        s: Text string
        p: Pattern string
        
    Returns:
        List of starting indices where anagram of p found
    """
    if len(p) > len(s):
        return []
    
    p_count = defaultdict(int)
    window_count = defaultdict(int)
    
    # Build pattern count
    for char in p:
        p_count[char] += 1
    
    result = []
    left = 0
    
    for right in range(len(s)):
        # Add character to window
        window_count[s[right]] += 1
        
        # Remove character if window too large
        if right - left + 1 > len(p):
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            left += 1
        
        # Check if window is anagram of p
        if window_count == p_count:
            result.append(left)
    
    return result


# ============================================================================
# TEMPLATE 5: Generic Sliding Window with Validation
# ============================================================================

def sliding_window_generic(arr: List[int], condition_check_func, extend_func, shrink_func):
    """
    Generic sliding window pattern.
    
    Args:
        arr: Input array
        condition_check_func: Function returns True if condition satisfied
        extend_func: Called when window moves right
        shrink_func: Called when window moves left
        
    Returns:
        Answer based on the condition
    """
    left = 0
    result = None
    
    for right in range(len(arr)):
        extend_func(arr[right])
        
        while not condition_check_func():
            shrink_func(arr[left])
            left += 1
        
        # Process valid window at [left, right]
        if result is None or right - left + 1 < result:
            result = right - left + 1
    
    return result


# ============================================================================
# KEY PATTERNS & INSIGHTS
# ============================================================================

"""
SLIDING WINDOW PATTERNS:

1. Fixed Size Window
   - Window moves with fixed size k
   - Check window on each expansion
   
2. Variable Size - Minimize
   - Shrink from left while condition still satisfied
   - Track minimum length
   - Example: Minimum window substring
   
3. Variable Size - Maximize
   - Shrink when condition violated
   - Track maximum length
   - Example: Longest substring without repeating

WHEN APPLICABLE:

✓ Array/string manipulation problems
✓ Looking for contiguous subarrays/substrings
✓ Need efficiency (O(n) better than O(n^2))
✓ Involves "at most k" or "exactly k" constraints

✗ Problems requiring non-contiguous selection
✗ Trees or general graphs
✗ Multiple separate pass-throughs

COMMON MISTAKES:

1. Not expanding window enough
   - Must always move right pointer forward
   
2. Not shrinking properly
   - When shrinking, must update state correctly
   
3. Off-by-one in window bounds
   - Window is [left, right] inclusive
   - Length = right - left + 1
   
4. Not handling duplicates
   - Use frequency map/counter
   - Delete when count reaches 0
   
5. Forgetting to process final window
   - Last window might be valid
   - May need separate check after loop
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Longest substring without repeating
    print("=== Longest Substring Without Repeating ===")
    test_str = "abcabcbb"
    result = longest_substring_without_repeating(test_str)
    print(f"String: {test_str}")
    print(f"Longest substring length: {result}")  # "abc" = 3
    print()
    
    # Longest substring with k distinct
    print("=== Longest Substring with K Distinct ===")
    test_str2 = "eceba"
    k = 2
    result2 = longest_substring_with_k_distinct(test_str2, k)
    print(f"String: {test_str2}, k={k}")
    print(f"Longest substring: {result2}")  # "ece" = 3
    print()
    
    # Minimum subarray length
    print("=== Minimum Subarray with Sum ===")
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    result3 = min_subarray_length(target, nums)
    print(f"Array: {nums}, target sum: {target}")
    print(f"Minimum subarray length: {result3}")  # [4, 3] = 2
    print()
    
    # Find anagram indices
    print("=== Find Anagram Substrings ===")
    s = "cbaebabacd"
    p = "abc"
    indices = find_anagram_substrings(s, p)
    print(f"Text: {s}, pattern: {p}")
    print(f"Anagram indices: {indices}")  # [0, 6]
