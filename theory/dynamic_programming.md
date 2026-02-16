# Dynamic Programming

Systematic technique for solving problems with overlapping subproblems and optimal substructure.

## Table of Contents

1. [Core Principles](#core-principles)
2. [State Space Design](#state-space-design)
3. [Optimization Techniques](#optimization-techniques)
4. [Common Patterns](#common-patterns)

---

## Core Principles

### Definition

**Dynamic Programming**: Method of solving complex problems by breaking them into simpler subproblems and storing results to avoid recomputation.

### Requirements for DP

**1. Optimal Substructure**
- Problem's optimal solution contains optimal solutions to subproblems
- Example: Shortest path has subpath that is also shortest
- Counter-example: Longest simple path (subpath may not be longest)

**2. Overlapping Subproblems**
- Same subproblems solved multiple times
- Without this, divide-and-conquer sufficient
- Example: fib(n) = fib(n-1) + fib(n-2) - massive overlap

### Approaches

**Top-Down (Memoization)**
```
Recursion + cache results
Risk: Stack overflow for deep recursion
Better readability for some problems
```

**Bottom-Up (Tabulation)**
```
Iterate through states, build solution
No recursion overhead
Easier to optimize space
```

---

## State Space Design

### Defining DP State

**DP[state] = answer for subproblem state**

Critical choices:
- What parameters define a unique subproblem?
- How many dimensions needed?
- What are state boundaries?

### Example: Coin Change

**Problem**: Minimum coins to make amount n

**State Definition**: dp[i] = min coins to make amount i

**Recurrence**: dp[i] = 1 + min(dp[i - coin]) for each coin ≤ i

**Complexity**: O(n · num_coins)

### Example: Longest Common Subsequence (LCS)

**Problem**: Longest common sequence of two strings

**State Definition**: dp[i][j] = LCS length for s1[0..i] and s2[0..j]

**Recurrence**:
- If s1[i] == s2[j]: dp[i][j] = 1 + dp[i-1][j-1]
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

**Complexity**: O(m · n) time, O(m · n) space → O(min(m,n)) with rolling array

### Common DP Dimensions

**1D DP**
- Linear sequences, prefixes
- Example: Maximum subarray sum

**2D DP**
- Two sequences, matrix problems
- Example: Edit distance, LCS

**3D+ DP**
- Multiple sequences or additional parameters
- Example: Knapsack with multiple constraints

---

## Optimization Techniques

### Space Optimization

**Rolling Array**
- If dp[i] depends only on dp[i-1], use two arrays
- Or use modulo arithmetic with one array

**Space Reduction Pattern**:
```
O(n²) → O(n) if previous row solves current row
```

### Time Optimization

**Convex Hull Trick**
- For specific recurrence: dp[i] = min(dp[j] + cost(i,j))
- When cost satisfies quadrangle inequality
- Reduces O(n²) to O(n log n)

**Monotone Queue Optimization**
- When state transitions form monotonic sequence
- Reduces some O(n²) to O(n)

**Digit DP Optimization**
- For problems on numerical values
- Digit-by-digit decomposition

### Transition Optimization

**Segment Tree DP**
- When need range query on previous states
- Query any dp[j] efficiently

**Fenwick Tree DP**
- Similar to segment tree
- Lower overhead

---

## Common Patterns

### 1. Unbounded Knapsack

Given items with weight w_i and value v_i, maximize value with total weight ≤ W:

```python
dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
```

### 2. 0/1 Knapsack

Each item used at most once:

```python
for item in items:
    for w in range(W, weight[item]-1, -1):
        dp[w] = max(dp[w], dp[w - weight[item]] + value[item])
```

### 3. Longest Increasing Subsequence (LIS)

**O(n²) approach** (DP):
```
dp[i] = 1 + max(dp[j]) for all j < i where arr[j] < arr[i]
```

**O(n log n) approach** (Binary search):
```
Maintain sorted lis_tails, binary search to insert
```

### 4. Minimum Edit Distance

Transform string A to string B with minimum operations:

```
dp[i][j] = min of:
  - dp[i-1][j] + 1     (delete)
  - dp[i][j-1] + 1     (insert)
  - dp[i-1][j-1] +0/1  (match/replace)
```

### 5. Tree DP

DP on tree structures:

```python
def dfs(node):
    if leaf:
        return base_case()
    
    result = 0
    for child in children:
        result += combine(dfs(child))
    
    return result
```

### 6. Bitmask DP

DP with sets represented as bitmasks:

```python
dp[mask][i] = answer when subset=mask, ending at i
```

Use cases: TSP, subset problems, assignment problems

---

## Debugging DP Solutions

**Checklist**:
- [ ] Base cases correct?
- [ ] Recurrence relation verified?
- [ ] State transitions valid?
- [ ] No integer overflow?
- [ ] Loop bounds correct?
- [ ] Space optimization maintains correctness?
- [ ] Test on provided examples
- [ ] Test on edge cases (empty, single, maximum)

---

## References

- Algorithm textbooks: CLRS, DPV
- CP3: Competitive Programming
- LeetCode DP category (100+ problems)
