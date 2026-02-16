# Optimization Techniques

Practical methods to improve algorithm performance.

## Algorithmic Optimizations

### 1. Problem Size Reduction

**Identify if problem has special structure**

- **Symmetry**: Solve half, mirror results
- **Monotonicity**: Binary search feasibility
- **Sorted assumption**: Presort if beneficial
- **Blocking**: Process in batches

**Example**: Find median in sorted matrices
- Doesn't require exploring all n elements
- Binary search on answer instead

### 2. Early Termination

**Stop when answer found, not when exhausted**

```python
def find_first_match(arr, target):
    for x in arr:
        if x == target:
            return x  # Stop immediately
    return None
```

**Applications**:
- Two-pointer: stop when pointers meet (could have early answer)
- Search: stop when found
- Validation: stop when constraint violated

### 3. Memoization

**Cache expensive computations**

```python
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result
```

**Decision Points**:
- Function deterministic? (same input = same output)
- Called repeatedly with same arguments?
- Computation expensive relative to caching cost?

### 4. Precomputation

**Calculate once before any queries**

```python
# Precompute prefix sums
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

# Now range sum [l, r] = prefix[r + 1] - prefix[l]
# Was O(n), now O(1)
```

**Common precomputations**:
- Prefix/suffix sums
- Prime sieve for range [1, n]
- Factorials for combinations
- Ancestor pointers (binary lifting)

### 5. Bitwise Operations

**Fast operations on binary representations**

```python
# Check if power of 2: O(1)
if (n & (n - 1)) == 0:
    print("Power of 2")

# Count bits: O(1) with hardware, O(log n) software
popcount = bin(n).count('1')

# Get rightmost set bit: O(1)
rightmost = n & (-n)
```

### 6. Space-Time Tradeoff

**Use memory to reduce computation**

| Goal | Method | Space | Time |
|------|--------|-------|------|
| Faster search | Hash table | O(n) | O(1) avg |
| Faster updates | Segment tree | O(n) | O(log n) |
| Faster queries | Precompute | O(n) | O(1) |

---

## Micro-Optimizations

### 1. Fast I/O

**Standard input is slow**

```python
import sys
input = sys.stdin.readline
```

**Speedup**: 5-50x faster for large inputs

### 2. Cache Locality

**Access memory sequentially**

```python
# Good: row-major traversal
for i in range(rows):
    for j in range(cols):
        matrix[i][j]

# Bad: column-major traversal (cache misses)
for j in range(cols):
    for i in range(rows):
        matrix[i][j]
```

### 3. Avoid Unnecessary Copies

```python
# Bad: creates copy
data = original_list + [new_element]

# Good: modifies in place
data = original_list
data.append(new_element)
```

### 4. Use Efficient Data Structures

| Operation | Array | Set | Dict | Heap |
|-----------|-------|-----|------|------|
| Access | O(1) | - | O(1) | O(log n) |
| Insert | O(n) | O(1) | O(1) | O(log n) |
| Delete | O(n) | O(1) | O(1) | O(log n) |
| Search | O(n) | O(1) | O(1) | O(n) |

### 5. Avoid String Concatenation

```python
# Bad: creates new string each time
result = ""
for item in items:
    result += str(item)

# Good: join at end
parts = [str(item) for item in items]
result = "".join(parts)
```

---

## Algorithm-Specific Optimizations

### 1. Binary Search Optimizations

**Reduce constant factors**:
```python
# Instead of: mid = (l + r) // 2
# Use: mid = l + (r - l) // 2  # Avoids overflow

# Unroll loop
if arr[mid] < target:
    l = mid + 1
elif arr[mid] > target:
    r = mid - 1
else:
    return mid
```

### 2. DP Optimizations

**Convex Hull Trick**: O(n²) → O(n log n) for monotone recurrence

**Sliding Window**: O(n²) → O(n) for sliding constraints

**Matrix Exponentiation**: Linear recurrence → O(log n)

### 3. Graph Optimizations

**Early Termination in BFS**: Stop when destination popped (shortest path found)

**Bidirectional Search**: O(2^(n/2)) instead of O(2^n)

**Pruning in DFS**: Skip branches that can't lead to better solution

---

## Problem-Specific Strategies

### Geometry Problems

- **Rotate/translate** to align with axes
- **Monotone property**: Binary search angle, position
- **Precompute** common values (distances, angles)

### Number Theory Problems

- **Sieve** for all primes up to n
- **Precompute** factorials for combinations
- **Modular arithmetic** to avoid overflow

### String Problems

- **KMP** for pattern matching O(n + m)
- **Rolling hash** for substring comparison
- **Trie** for prefix queries on many strings

### Greedy Problems

- **Sort** by appropriate metric
- **Validate** greedy choice property holds
- **Exchange argument** for proof

---

## When to Optimize

### Priority Order

1. **Correctness first**: Algorithm must be right
2. **Complexity analysis**: Select right algorithm
3. **Micro-optimizations**: Only if still TLE
4. **Profile**: Find the bottleneck

### Premature Optimization Warning

> "Premature optimization is the root of all evil" - Donald Knuth

**Good practice**:
1. Get solution correct
2. If passes time limit: done
3. If TLE: profile and optimize

**Don't**: Optimize before you know it's slow

---

## Optimization Complexity Improvements

| From | To | Method |
|------|----|----|
| O(n²) | O(n log n) | Sort + binary search or two pointers |
| O(2^n) | O(n × 2^(n/2)) | Meet in the middle |
| O(n²) | O(n) | Monotone queue, sliding window |
| O(n²) | O(n log n) | Convex hull trick, segment tree |
| O(n!) | O(2^n × n) | DP on subsets |

