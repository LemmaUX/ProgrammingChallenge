"""
Binary Search Template

Comprehensive implementations of binary search patterns for competitive programming.
Handles various edge cases and problem variants.

Time Complexity: O(log n)
Space Complexity: O(1) [iterative] or O(log n) [recursive with call stack]
"""


# ============================================================================
# TEMPLATE 1: Basic Binary Search (Find exact target)
# ============================================================================

def binary_search_basic(arr: list[int], target: int) -> int:
    """
    Find exact index of target in sorted array.
    Returns index if found, -1 otherwise.
    
    Usage: When searching for exact value in sorted array.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# ============================================================================
# TEMPLATE 2: Binary Search on Answer
# ============================================================================

def binary_search_leftmost(arr: list[int], target: int) -> int:
    """
    Find leftmost (first) occurrence of target in sorted array.
    Returns index of first occurrence, or -1 if not found.
    
    Key insight: When we find target, continue searching left side.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_rightmost(arr: list[int], target: int) -> int:
    """
    Find rightmost (last) occurrence of target in sorted array.
    Returns index of last occurrence, or -1 if not found.
    
    Key insight: When we find target, continue searching right side.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# ============================================================================
# TEMPLATE 3: Binary Search for Smallest Value >= Target
# ============================================================================

def binary_search_lower_bound(arr: list[int], target: int) -> int:
    """
    Find smallest value >= target (lower bound).
    Returns index, or len(arr) if no such element exists.
    
    Usage: Finding insertion position, range queries.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_upper_bound(arr: list[int], target: int) -> int:
    """
    Find smallest value > target (upper bound).
    Returns index, or len(arr) if no such element exists.
    
    Usage: Finding insertion position, range queries.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left


# ============================================================================
# TEMPLATE 4: Binary Search on Monotonic Function
# ============================================================================

def binary_search_on_function(high: int, check_func) -> int:
    """
    Binary search where we're looking for minimum value where check_func returns True.
    Works with any monotonic function.
    
    Args:
        high: Upper bound of search range (search is [0, high])
        check_func: Function that takes value and returns True/False
    
    Returns:
        Minimum value where check_func returns True
    
    Example:
        def can_fit_items(capacity):
            return sum_of_items <= capacity
        
        min_capacity = binary_search_on_function(10000, can_fit_items)
    """
    left, right = 0, high
    result = high
    
    while left <= right:
        mid = left + (right - left) // 2
        if check_func(mid):
            result = mid
            right = mid - 1  # Try smaller value
        else:
            left = mid + 1
    
    return result


# ============================================================================
# TEMPLATE 5: Binary Search Variant - Maximum Value Condition
# ============================================================================

def binary_search_max_condition(low: int, high: int, check_func) -> int:
    """
    Find maximum value where check_func returns True.
    
    Args:
        low, high: Search range [low, high]
        check_func: Function that takes value and returns True/False
        
    Returns:
        Maximum value where check_func returns True
    """
    result = low - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if check_func(mid):
            result = mid
            low = mid + 1  # Try larger value
        else:
            high = mid - 1
    
    return result


# ============================================================================
# EDGE CASES AND PITFALLS
# ============================================================================

"""
COMMON PITFALLS:

1. Off-by-one errors
   - Use "left < right" vs "left <= right" carefully
   - mid calculation: mid = left + (right - left) // 2 prevents overflow

2. Infinite loops
   - Always advance pointers: left = mid + 1, right = mid - 1
   - Never do: left = mid, right = mid (causes infinite loop)

3. Wrong update condition
   - Leftmost: when found, search LEFT (right = mid - 1)
   - Rightmost: when found, search RIGHT (left = mid + 1)
   - Lower bound: arr[mid] < target? search RIGHT
   - Upper bound: arr[mid] <= target? search RIGHT

4. Array bounds
   - Check if array is empty before calling
   - Verify target is in reasonable range

EDGE CASES TO TEST:
- Empty array
- Single element
- Target smaller than all elements
- Target larger than all elements
- Multiple occurrences of target
- Duplicates in array
"""


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    # Test cases
    arr = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8]
    
    # Basic search
    print(f"Find 2: {binary_search_basic(arr, 2)}")  # 1
    print(f"Find 5: {binary_search_basic(arr, 5)}")  # 6
    print(f"Find 10: {binary_search_basic(arr, 10)}")  # -1
    
    # Leftmost/Rightmost
    print(f"Leftmost 2: {binary_search_leftmost(arr, 2)}")  # 1
    print(f"Rightmost 2: {binary_search_rightmost(arr, 2)}")  # 3
    
    # Bounds
    print(f"Lower bound 2: {binary_search_lower_bound(arr, 2)}")  # 1
    print(f"Upper bound 2: {binary_search_upper_bound(arr, 2)}")  # 4
    
    # Binary search on function
    def can_contain_sum(capacity):
        return capacity >= 10
    
    result = binary_search_on_function(100, can_contain_sum)
    print(f"Min capacity to contain sum 10: {result}")
