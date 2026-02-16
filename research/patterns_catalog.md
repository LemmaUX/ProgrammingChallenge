# Common Patterns and Techniques

Catalog of recurring problem patterns and their optimal solutions.

## Pattern Categories

### 1. Array/String Patterns

#### Two Pointers
- **Problem**: Find pair in array satisfying condition
- **Approach**: Expand/contract from ends
- **Examples**: Container with most water, 3sum, valid palindrome

#### Sliding Window
- **Problem**: Optimal subarray/substring with constraint
- **Approach**: Maintain window, expand/shrink based on condition
- **Examples**: Longest substring without repeating, minimum window

#### Prefix/Suffix
- **Problem**: Query depends on elements before/after index
- **Approach**: Precompute prefix sums, suffix sums
- **Examples**: Product of array except self, trapping rain water

### 2. Tree Patterns

#### DFS on Tree
- **Problem**: Value from recursive structure
- **Approach**: Bottom-up recursion, aggregate from children
- **Examples**: Tree height, total sum, diameter

#### Tree Path Query
- **Problem**: LCA, path sums
- **Approach**: Ancestor tracking, binary lifting, tree DP
- **Examples**: Kth ancestor, sum on path

#### Tree Reconstruction
- **Problem**: Build tree from pre/in/post-order
- **Approach**: Find root in inorder, partition recursively
- **Examples**: Construct binary tree from traversals

### 3. Graph Patterns

#### Connected Components
- **Problem**: Find/count separate subgraphs
- **Approach**: DFS/BFS or Union-Find
- **Examples**: Number of islands, cycle detection

#### Shortest Path
- **Problem**: Minimum cost path
- **Approach**: Dijkstra (non-negative), Bellman-Ford (negative), 0-1 BFS
- **Examples**: Network delay time, path with maximum gold

#### Topological Sort
- **Problem**: Dependencies ordering
- **Approach**: Kahns (in-degree) or DFS post-order
- **Examples**: Course prerequisites, build order

### 4. DP Patterns

#### 1D DP
- **State**: dp[i] = answer for prefix [0..i]
- **Examples**: House robber, max subarray, climbing stairs

#### 2D DP
- **State**: dp[i][j] = answer for subproblems on i and j
- **Examples**: LCS, edit distance, matrix path

#### Tree DP
- **State**: dp[node] = answer for subtree
- **Examples**: Max sum path, node counting

#### Bitmask DP
- **State**: dp[mask] = answer when subset is mask
- **Examples**: TSP, subset sum, independent set

### 5. Greedy Patterns

#### Activity Selection
- **Approach**: Sort by end time, greedily pick non-overlapping
- **Examples**: Interval scheduling, task assignment

#### Huffman Coding
- **Approach**: Always merge two smallest
- **Examples**: Optimize any combining operation

#### Fraction Knapsack
- **Approach**: Sort by value/weight, select greedily
- **Examples**: Fractional knapsack (not 0/1)

---

## Problem Type Recognition

### Identify the Pattern

**Step 1**: Understand constraints
- Array? String? Tree? Graph?
- Single or multiple dimensions?
- Static or dynamic?

**Step 2**: Recognize pattern
- What does "optimal" mean?
- Do subproblems overlap?
- Can you build from smaller solutions?

**Step 3**: Code recognition features
- Look at examples
- Identify what varies
- Notice relationships

**Step 4**: Match to known pattern
- Have you seen similar problem?
- What algorithm solved it?
- What modifications needed?

---

## Red Flags and Gotchas

### Common Mistakes

1. **Array indices**: Off-by-one in loops, boundary conditions
2. **Integer overflow**: When multiplying/adding large numbers
3. **Negative numbers**: Modulo, comparisons, special cases
4. **Empty input**: Arrays of size 0, empty strings
5. **Infinite loops**: Ensure loop condition changes

### Optimization Opportunities

1. **Two-pointer**: Instead of nested loops
2. **Precomputation**: Instead of repeated calculation
3. **Early termination**: When answer found
4. **Space optimization**: Rolling arrays for DP
5. **Memoization**: Cache expensive computations

### Testing Strategy

1. **Provided examples**: Must pass first
2. **Edge cases**: Empty, single element, maximum values
3. **Type boundaries**: Negative, zero, positive
4. **Stress testing**: Large inputs, time limits

---

## Implementation Framework

### Before Coding

- [ ] Understood problem completely?
- [ ] Identified algorithm/pattern?
- [ ] Worked through examples by hand?
- [ ] Considered time/space complexity?
- [ ] Thought about edge cases?

### While Coding

- [ ] Clear variable names?
- [ ] Comments for non-obvious logic?
- [ ] Early returns for edge cases?
- [ ] Proper initialization?
- [ ] Loop bounds verified?

### After Coding

- [ ] Compiles/runs without errors?
- [ ] Passes provided examples?
- [ ] Passes edge cases?
- [ ] Time complexity acceptable?
- [ ] No unnecessary copies/allocations?

