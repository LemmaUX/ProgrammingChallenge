# Data Structures

Theory and implementation of crucial data structures for competitive programming.

## Table of Contents

1. [Linear Data Structures](#linear-data-structures)
2. [Trees](#trees)
3. [Heaps and Priority Queues](#heaps-and-priority-queues)
4. [Hash-Based Structures](#hash-based-structures)
5. [Advanced Structures](#advanced-structures)

---

## Linear Data Structures

### Stack (LIFO)

**Operations**: push, pop, top
**Complexity**: O(1)
**Uses**: Parentheses matching, next greater element, undo

### Queue (FIFO)

**Operations**: enqueue, dequeue, front
**Complexity**: O(1)
**Uses**: BFS, scheduling, windowing

**Deque (Double-Ended Queue)**
- Efficient operations at both ends
- Used in sliding window maximum: O(n)

### Linked List

**Singly Linked**:
- Forward traversal
- Insert/delete O(1) with pointer

**Doubly Linked**:
- Bidirectional traversal
- Extra space per node

**Use**: When frequent insertion/deletion, not random access

---

## Trees

### Binary Search Tree (BST)

**Properties**: left < root < right

**Balanced BST** (AVL, Red-Black):
- Height O(log n)
- All operations O(log n)
- Maintains balance after insert/delete

**Uses**: Sorted data with dynamic updates

### Segment Tree

**Purpose**: Efficient range queries and updates

**Variants**:
- Sum queries
- Min/max queries
- Lazy propagation for range updates

**Complexity**: O(log n) per operation

### Fenwick Tree (Binary Indexed Tree)

**Purpose**: Efficient prefix sums and updates

**Space Efficient**: O(n) compared to O(4n) for segment tree

**Complexity**: O(log n) per operation

**Key Insight**: Uses indexing trick with lowest set bit

### Trie (Prefix Tree)

**Purpose**: Efficient string prefix searching

**Structure**: Tree where each edge is character

**Complexity**: O(|word|) for insert/search

**Uses**: Auto-complete, spell checkers, IP routing

---

## Heaps and Priority Queues

### Min/Max Heap

**Property**: Parent ≤ children (min heap)

**Array Representation**:
- Parent at i: left child at 2i+1, right child at 2i+2
- No explicit pointers needed

**Operations**:
- Insert: O(log n)
- Extract min: O(log n)
- Heapify: O(n)

**Python**: Use heapq module

### Priority Queue Applications

**Dijkstra's Algorithm**: Extract minimum distance node

**Heap Sort**: Sort using heap structure

**K-Largest Elements**: Min heap of size k

---

## Hash-Based Structures

### Hash Table (Dictionary/Map)

**Average Complexity**: O(1) operations

**Collision Handling**:
- Chaining: Linked list per bucket
- Open addressing: Find alternative slot

**Worst Case**: O(n) when hash function poor

**Load Factor**: Keep < 0.75 for good performance

### Hash Set

**Purpose**: Fast membership testing

**Python**: `set()` data structure

**Uses**: Duplicate detection, unique counting

---

## Advanced Structures

### Segment Tree with Lazy Propagation

**Purpose**: Range updates and queries efficiently

**Key Idea**: Delayed propagation of update information

**Complexity**: O(log n) for both update and query

**Uses**: Add to range, sum in range; set range to value

### Fenwick Tree Variants

**2D Fenwick Tree**: 2D range sum queries

**Range Update Fenwick Tree**: Update range, query point

**Complexity**: Still O(log² n) for 2D, O(log n) for range updates

### Disjoint Set Union (Union-Find)

**Purpose**: Track connectivity and merge sets

**Operations**:
- Find with path compression: O(α(n)) amortized
- Union by rank: O(α(n)) amortized
- α(n) ≈ 4 for all practical n

**Uses**: Connectivity, cycle detection, Kruskal's MST

### Suffix Array and Suffix Tree

**Purpose**: Efficient string pattern matching and substring queries

**Suffix Array**: Sorted array of string suffixes

**Complexity**: O(n log n) construction, O(log n + k) search

**Upper-Bound**: More space efficient than suffix tree

### Persistent Data Structures

**Idea**: Maintain all versions of data structure

**Application**: Queries over historical states

**Example**: Persistent segment tree for range queries at different time points

---

## Choosing Data Structures

| Problem | Best Structure |
|---------|---|
| Sorted dynamic data | Balanced BST or skip list |
| Range sum queries | Segment tree or Fenwick tree |
| Shortest paths | Min-heap with priority queue |
| Connectivity | Union-Find |
| String matching | Trie or suffix array |
| Frequency top-k | Max-heap |
| Sliding window | Deque |
| Next/previous element | Stack or sorted set |

---

## Implementation Checklist

- [ ] Right structure for problem constraints?
- [ ] Worst-case complexity acceptable?
- [ ] Space complexity within limits?
- [ ] Overflow in tree indices?
- [ ] Boundary conditions handled?
- [ ] Rebalancing for balanced trees?
- [ ] Hash function uniform?
- [ ] Proper comparators for custom objects?

