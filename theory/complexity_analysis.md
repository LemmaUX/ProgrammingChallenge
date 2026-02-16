# Complexity Analysis

Rigorous method for evaluating algorithm efficiency.

## Table of Contents

1. [Time Complexity](#time-complexity)
2. [Space Complexity](#space-complexity)
3. [Analyzing Recursive Algorithms](#analyzing-recursive-algorithms)
4. [Amortized Analysis](#amortized-analysis)

---

## Time Complexity

### Definition

**Time Complexity**: Function T(n) describing maximum operations performed for input size n

### Common Categories

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array scan |
| O(n log n) | Linearithmic | Merge sort, heapsort |
| O(n²) | Quadratic | Bubble sort, nested loops |
| O(n³) | Cubic | 3D matrix operations |
| O(2ⁿ) | Exponential | Subset generation |
| O(n!) | Factorial | Permutation generation |

### Why Big-O Notation?

1. **Constants don't matter**: O(1000n) = O(n)
2. **Lower terms don't matter**: O(n² + n) = O(n²)
3. **Focus on dominant term**: Behavior for large n

### Analysis Techniques

**Counting Operations**:
1. Identify innermost operations
2. Count how many times executed
3. Combine counts for overall complexity

**Example**: Nested loops

```python
for i in range(n):           # n times
    for j in range(n):       # n times per i
        operation()          # 1 unit

# Total: n * n = O(n²)
```

### Loop Analysis

**Simple loop**:
```python
for i in range(n):
    operation()
```
Complexity: O(n)

**Halving loop**:
```python
while n > 1:
    operation()
    n //= 2
```
Complexity: O(log n)

**Multiplying loop**:
```python
i = 1
while i < n:
    operation()
    i *= 2
```
Complexity: O(log n)

---

## Space Complexity

### Definition

**Space Complexity**: Amount of additional memory (extra space) required

**Note**: Often count problem memory only, not input

### Categories

| Type | Space |
|------|-------|
| Constant space | O(1) |
| Linear space | O(n) |
| Quadratic space | O(n²) |
| Logarithmic space | O(log n) |

### Stack Space (Recursion)

**Depth of recursion**: d
**Space per call**: s
**Total**: O(d × s)

**Example**: Binary search recursion depth O(log n), O(1) per call = O(log n) total

### Space Optimization Techniques

**1. Rolling Array**
```python
# Instead of: prev = [0] * n, curr = [0] * n
# Use: prev, curr = [0] * n, [0] * n
# Then reuse: prev, curr = curr, [0] * n
```

**2. In-Place Modifications**
```python
# Swap instead of creating new array
a, b = b, a
```

**3. Generator Functions**
```python
# Yield results instead of storing all
def generate_permutations(items):
    yield from permutations(items)
```

---

## Analyzing Recursive Algorithms

### Recurrence Relations

**Form**: T(n) = a·T(n/b) + f(n)

**Where**:
- a: number of subproblems
- n/b: size reduction
- f(n): work outside recursion

### Master Theorem

Given T(n) = a·T(n/b) + f(n):

**Case 1**: If f(n) = O(n^(log_b(a) - ε))
- **Result**: T(n) = O(n^log_b(a))

**Case 2**: If f(n) = Θ(n^log_b(a))
- **Result**: T(n) = Θ(n^log_b(a) · log n)

**Case 3**: If f(n) = Ω(n^(log_b(a) + ε))
- **Result**: T(n) = Θ(f(n))

### Example: Merge Sort

```
T(n) = 2·T(n/2) + O(n)
```

- a = 2, b = 2, f(n) = n
- log_b(a) = log_2(2) = 1
- f(n) = n = Θ(n¹) → **Case 2**
- **Result**: T(n) = O(n log n)

### Example: Binary Search

```
T(n) = T(n/2) + O(1)
```

- a = 1, b = 2, f(n) = 1
- log_b(a) = log_2(1) = 0
- f(n) = O(n⁰) → **Case 1** (f(n) < n⁰)
- **Result**: T(n) = O(1) — **WRONG!**

Actually T(n) = O(log n) because single recursive call: T(n) = T(n/2) + c

---

## Amortized Analysis

### Definition

**Amortized**: Average cost over sequence of operations

**Why needed**: Single operation might be expensive, but average is cheap

### Example: Dynamic Array (Vector)

**Single append**:
- Usually O(1) if space available
- Occasionally O(n) when resizing

**Amortized**: O(1) per append

**Proof**:
- Resize when array full, double capacity
- Total work to insert n items: n + (1 + 2 + 4 + ... + n) = O(n)
- Average per item: O(n)/n = O(1)

### Three Methods

**1. Aggregate Analysis**
- Total cost for n operations
- Divide by n for average

**2. Accounting Method**
- Assign "tokens" to operations
- Expensive operation uses saved tokens
- Show tokens never go negative

**3. Potential Method**
- Define potential function φ(state)
- Amortized cost = actual cost + Δφ
- Sum amortized costs

### Common Examples

| Operation | Worst | Amortized |
|-----------|-------|-----------|
| Dynamic array append | O(n) | O(1) |
| Incrementing counter | O(log n) | O(1) |
| Disjoint set union | O(log n) | O(α(n)) |

---

## Practical Analysis for Competitive Programming

### Memory Limits

- Typical: 256-512 MB
- 10⁶ integers ≈ 4 MB
- 10⁷ integers ≈ 40 MB

### Time Limits

- Typical: 1-2 seconds
- ~10⁸ simple operations per second

### Rule of Thumb for Input Size n

| n | Acceptable |
|---|---|
| ≤ 10 | O(n!) or O(2ⁿ) |
| ≤ 20 | O(2ⁿ) or O(n²·2^n) |
| ≤ 500 | O(n³) |
| ≤ 10⁴ | O(n²) |
| ≤ 10⁶ | O(n log n) or O(n) |
| ≤ 10⁹ | O(log n) or O(1) |

### Analysis Checklist

- [ ] Time complexity within bounds for n?
- [ ] Space complexity within memory limit?
- [ ] Constant factors considered?
- [ ] Cache efficiency (arrays better than trees)?
- [ ] I/O bottleneck (use fast I/O)?
- [ ] Tested on maximum input?

