# Algorithms Foundations

Core concepts and analytical tools essential for algorithmic thinking.

## Table of Contents

1. [Computational Complexity](#computational-complexity)
2. [Asymptotic Analysis](#asymptotic-analysis)
3. [Problem Solving Paradigms](#problem-solving-paradigms)
4. [Correctness and Proof](#correctness-and-proof)

---

## Computational Complexity

### What is Complexity?

Complexity measures resource usage (time and space) as function of input size n.

**Time Complexity**: Operations performed (relative to input size)
**Space Complexity**: Memory used (relative to input size)

### Why Measure Complexity?

- Predict algorithm performance on large inputs
- Compare algorithms objectively
- Identify bottlenecks and optimization opportunities
- Understand scalability limits

### Practical Running Times

| Complexity | n = 100 | n = 1,000 | n = 10,000 | n = 1,000,000 |
|-----------|---------|----------|-----------|---------------|
| O(log n)  | < 1 ms  | < 1 ms   | < 1 ms    | < 1 ms        |
| O(n)      | < 1 ms  | 1 ms     | 10 ms     | 1 sec         |
| O(n log n)| < 1 ms  | 10 ms    | 130 ms    | 20 sec        |
| O(n²)     | 10 ms   | 1 sec    | 100 sec   | 10¹⁰ years    |
| O(2ⁿ)     | 10¹²    | 10²⁹⁸    | -         | -             |

---

## Asymptotic Analysis

### Big-O Notation

**Definition**: O(g(n)) = functions that grow no faster than g(n)

Formally: f(n) = O(g(n)) if ∃ c, n₀ : f(n) ≤ c·g(n) for all n ≥ n₀

**Intuition**: Upper bound on growth rate

```
O(1)        - Constant time
O(log n)    - Logarithmic (binary search)
O(n)        - Linear (scanning array)
O(n log n)  - Linearithmic (merge sort)
O(n²)       - Quadratic (nested loops)
O(n³)       - Cubic
O(2ⁿ)       - Exponential (subsets)
O(n!)       - Factorial (permutations)
```

### Omega (Ω) Notation

**Definition**: Lower bound on growth rate
**Intuition**: Algorithm requires AT LEAST this much time

### Theta (Θ) Notation

**Definition**: Tight bound (both upper and lower)
**When to use**: Most accurate description of algorithm's behavior

### Practical Rules

1. Drop constants: O(2n) = O(n)
2. Drop lower order terms: O(n² + n) = O(n²)
3. Simplify products: O(log n · n) = O(n log n)

### Recurrence Relations

**Master Theorem**: For T(n) = a·T(n/b) + f(n)

- If f(n) = O(n^(log_b(a) - ε)): T(n) = O(n^log_b(a))
- If f(n) = Θ(n^log_b(a)): T(n) = Θ(n^log_b(a) · log n)
- If f(n) = Ω(n^(log_b(a) + ε)): T(n) = Θ(f(n))

---

## Problem Solving Paradigms

### Brute Force

**Definition**: Try all possibilities

```
Time: O(2ⁿ) to O(n!)
Space: Usually O(n)
```

**When appropriate**: Small input size (n ≤ 20)

**Optimization**: Backtracking, pruning

### Divide and Conquer

**Definition**: Split problem, solve recursively, combine solutions

**Pattern**:
1. Divide problem into smaller subproblems
2. Recursively solve subproblems
3. Combine results

**Examples**: Merge sort, quicksort, binary search

**Complexity Analysis**: Use recurrence relations

### Dynamic Programming

**Definition**: Solve overlapping subproblems using memoization

**Key Properties**:
- Optimal substructure: Solution built from optimal solutions
- Overlapping subproblems: Same subproblem solved multiple times

**Approaches**:
- Top-down: Recursion + memoization
- Bottom-up: Iterative DP table

**Complexity**: Usually O(number of states · time per state)

### Greedy Algorithms

**Definition**: Make locally optimal choices

**Challenge**: Proving correctness (exchange argument)

**When works**: Problems with greedy choice property

### Graph Algorithms

**Core techniques**:
- BFS: Shortest path (unweighted)
- DFS: Connectivity, ordering
- Dijkstra: Shortest path (non-negative weights)
- Bellman-Ford: Shortest path (including negative)
- Floyd-Warshall: All-pairs shortest path

---

## Correctness and Proof

### Mathematical Induction

Prove statement P(n) for all n ≥ n₀:

1. **Base case**: Show P(n₀) true
2. **Inductive step**: Assume P(k) true, show P(k+1) true

### Exchange Argument (for Greedy)

1. Assume optimal solution differs from greedy
2. Show we can swap local choice without decreasing optimality
3. Repeat until greedy solution obtained
4. Conclude greedy solution is optimal

### Proof by Contradiction

Assume statement is false, derive impossibility

### Well-Founded Induction

For problems with no "natural" ordering, define well-founded metric

---

## Competitive Programming Perspective

**Memory Limit**: Usually 256-512 MB
**Time Limit**: Usually 1-2 seconds per test
**Testing Strategy**: Test on examples first, then edge cases

**Optimization Checklist**:
- [ ] Correct algorithm chosen?
- [ ] Time complexity acceptable for constraints?
- [ ] Space complexity within limits?
- [ ] Edge cases handled?
- [ ] Input parsing correct?
- [ ] Off-by-one errors?
- [ ] Integer overflow?
- [ ] Output format exact?

---

## References

- CLRS: Introduction to Algorithms
- DPV: Algorithms by Dasgupta, Papadimitriou, Vazirani
- CP3: Competitive Programming by Halim & Halim
