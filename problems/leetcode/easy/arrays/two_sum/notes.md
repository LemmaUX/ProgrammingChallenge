# Two Sum - Solution Notes

## Complexity Analysis

### Hash Map Solution
- **Time**: O(n) - single pass through array
- **Space**: O(n) - hash map in worst case stores all elements
- **Justification**: Each element visited once, hash operations O(1) on average

### Alternative: Two Pointer with Sorting
- **Time**: O(n log n) - dominated by sorting
- **Space**: O(1) or O(n) - depends on sorting algorithm and index tracking
- **Better for**: Finding all pairs, related problems

## Algorithm Walkthrough

### Example: [2, 7, 11, 15], target = 9

**Step 1**: i=0, num=2
- complement = 9 - 2 = 7
- 7 not in seen yet
- seen = {2: 0}

**Step 2**: i=1, num=7  
- complement = 9 - 7 = 2
- 2 IS in seen at index 0
- Return [0, 1] ✓

## Implementation Tricks

### 1. Hash Map vs. Set
- Use **dict** (hash map) to store indices
- Use **set** if only need existence check

### 2. Order of Checking
```python
# IMPORTANT: Check complement BEFORE adding current element
if complement in seen:
    return [seen[complement], i]
seen[num] = i
```

Why? Can't use same element twice.

### 3. Handle Duplicates
```
nums = [1, 1, 1, 1], target = 2
- First 1 at index 0: complement = 1, not yet seen, store {1: 0}
- Second 1 at index 1: complement = 1, found at index 0, return [0, 1] ✓
```

## Related Problems

### Easier
- **Contains Duplicate**: Check if array has duplicates (use set)

### Harder
- **3Sum**: Find all triplets that sum to target (multiple approaches)
- **4Sum**: Find all quadruplets that sum to target
- **Two Sum II**: Array is sorted, return indices [1, 2]
- **Two Sum Less Than K**: Find pair with sum < k

### Skills Transfer
- Hash table design
- Complementary value thinking
- Index tracking in transformations

## Common Mistakes

1. **Returning values instead of indices**: Problem asks for indices!
2. **Using same element twice**: Check complement before storing
3. **Assuming sorted**: Input might not be sorted
4. **Forgetting edge cases**: Duplicates, negative numbers, zeros

## Interview Angles

**Question**: "What if we want ALL pairs?"
- Use *nested loop* O(n²): simple but slow
- Use *two pointers* O(n log n): need sorting
- Use *hash set with careful tracking*: tricky but O(n)

**Question**: "What if there are multiple solutions?"
- Return any one
- Return all (slightly different approach)
- Return in specific order

**Question**: "Can you do better than O(n) space?"
- For single pair: No (need to track complements)
- If array sorted: Use two pointers O(1) space

## Key Takeaways

1. **Hash tables** are powerful for complement/match problems
2. **Two pointers** work well on sorted arrays
3. **Index tracking** matters when returning positions
4. **Order of operations** important (check before storing)

