"""
Fenwick Tree (Binary Indexed Tree) Template

Space-efficient alternative to segment tree for range sum queries and point updates.
More cache-friendly and easier to implement than segment tree.

Time Complexity: O(log n) for update and query
Space Complexity: O(n)
"""


class FenwickTree:
    """
    Binary Indexed Tree (Fenwick Tree) for efficient prefix sum queries.
    """
    
    def __init__(self, n: int):
        """
        Initialize Fenwick Tree with n elements (1-indexed).
        
        Args:
            n: Size of array
        """
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed
    
    def update(self, idx: int, delta: int):
        """
        Add delta to element at index idx (1-indexed).
        
        Args:
            idx: Index to update (1-indexed)
            delta: Value to add
        """
        idx += 1  # Convert to 1-indexed
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)  # Add lowest set bit
    
    def query(self, idx: int) -> int:
        """
        Get prefix sum [0, idx] (0-indexed, inclusive).
        
        Args:
            idx: End index (0-indexed, inclusive)
            
        Returns:
            Sum of elements from 0 to idx
        """
        idx += 1  # Convert to 1-indexed
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)  # Remove lowest set bit
        return result
    
    def range_query(self, l: int, r: int) -> int:
        """
        Get sum in range [l, r] (0-indexed, inclusive).
        
        Args:
            l, r: Range bounds (0-indexed, inclusive)
            
        Returns:
            Sum of elements in range
        """
        if l == 0:
            return self.query(r)
        return self.query(r) - self.query(l - 1)
    
    def get(self, idx: int) -> int:
        """
        Get value at single index (slower - O(log n)).
        """
        return self.range_query(idx, idx)


# ============================================================================
# VARIANT: Range Update with Point Query (Difference Array approach)
# ============================================================================

class FenwickTreeRangeUpdate:
    """
    Fenwick Tree for range updates and point queries.
    Uses difference array technique with two Fenwick trees.
    """
    
    def __init__(self, n: int):
        self.n = n
        self.tree1 = [0] * (n + 1)
        self.tree2 = [0] * (n + 1)
    
    def _update_helper(self, tree, idx: int, val: int):
        """Helper to update a Fenwick tree."""
        idx += 1
        while idx <= self.n:
            tree[idx] += val
            idx += idx & (-idx)
    
    def _query_helper(self, tree, idx: int) -> int:
        """Helper to query a Fenwick tree."""
        idx += 1
        result = 0
        while idx > 0:
            result += tree[idx]
            idx -= idx & (-idx)
        return result
    
    def range_update(self, l: int, r: int, val: int):
        """
        Add val to all elements in range [l, r] (0-indexed, inclusive).
        """
        self._update_helper(self.tree1, l, val)
        self._update_helper(self.tree1, r + 1, -val)
        self._update_helper(self.tree2, l, val * l)
        self._update_helper(self.tree2, r + 1, -val * (r + 1))
    
    def point_query(self, idx: int) -> int:
        """
        Get value at index idx after all range updates (0-indexed).
        """
        return (
            self._query_helper(self.tree1, idx) * (idx + 1) -
            self._query_helper(self.tree2, idx)
        )


# ============================================================================
# VARIANT: 2D Fenwick Tree
# ============================================================================

class FenwickTree2D:
    """
    2D Fenwick Tree for 2D range sum queries.
    """
    
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    def update(self, r: int, c: int, delta: int):
        """Update element at (r, c) with delta."""
        r += 1
        c += 1
        while r <= self.rows:
            c_ptr = c
            while c_ptr <= self.cols:
                self.tree[r][c_ptr] += delta
                c_ptr += c_ptr & (-c_ptr)
            r += r & (-r)
    
    def query(self, r: int, c: int) -> int:
        """Get sum in rectangle [0, 0] to [r, c] (0-indexed, inclusive)."""
        r += 1
        c += 1
        result = 0
        while r > 0:
            c_ptr = c
            while c_ptr > 0:
                result += self.tree[r][c_ptr]
                c_ptr -= c_ptr & (-c_ptr)
            r -= r & (-r)
        return result
    
    def range_query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """Get sum in rectangle [r1, c1] to [r2, c2] (0-indexed, inclusive)."""
        result = self.query(r2, c2)
        if r1 > 0:
            result -= self.query(r1 - 1, c2)
        if c1 > 0:
            result -= self.query(r2, c1 - 1)
        if r1 > 0 and c1 > 0:
            result += self.query(r1 - 1, c1 - 1)
        return result


# ============================================================================
# KEY INSIGHTS
# ============================================================================

"""
FENWICK TREE VS SEGMENT TREE:

Fenwick Tree Advantages:
- Simpler implementation
- Better cache locality
- Less memory overhead
- Slightly faster in practice

Segment Tree Advantages:
- Easier to extend for other operations (min, max, etc.)
- Supports lazy propagation for range updates
- More intuitive tree structure

LOWBIT OPERATION: idx & (-idx)
- Gives lowest set bit in binary representation
- Key to understanding Fenwick Tree indexing
- Example: 6 (110) & -6 = 010 = 2

COMMON PATTERNS:
1. Point update, range query: Standard Fenwick Tree
2. Range update, point query: Use difference array variant
3. 2D queries: Use 2D Fenwick Tree
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Basic Fenwick Tree
    print("=== Basic Fenwick Tree ===")
    ft = FenwickTree(6)
    arr = [1, 3, 5, 7, 9, 11]
    for i, val in enumerate(arr):
        ft.update(i, val)
    
    print(f"Sum [0, 2]: {ft.range_query(0, 2)}")  # 1 + 3 + 5 = 9
    ft.update(1, 7)  # Add 7 to index 1 (making it 10)
    print(f"Sum [0, 2] after update: {ft.range_query(0, 2)}")  # 1 + 10 + 5 = 16
    print()
    
    # Range Update Fenwick Tree
    print("=== Range Update Fenwick Tree ===")
    frut = FenwickTreeRangeUpdate(5)
    frut.range_update(1, 3, 2)  # Add 2 to indices [1, 3]
    print(f"Value at index 0: {frut.point_query(0)}")  # 0
    print(f"Value at index 1: {frut.point_query(1)}")  # 2
    print(f"Value at index 3: {frut.point_query(3)}")  # 2
    print()
    
    # 2D Fenwick Tree
    print("=== 2D Fenwick Tree ===")
    ft2d = FenwickTree2D(3, 3)
    ft2d.update(0, 0, 1)
    ft2d.update(1, 1, 4)
    ft2d.update(2, 2, 9)
    
    print(f"Sum [0, 0] to [1, 1]: {ft2d.range_query(0, 0, 1, 1)}")  # 1 + 4 = 5
    print(f"Sum [0, 0] to [2, 2]: {ft2d.range_query(0, 0, 2, 2)}")  # 1 + 4 + 9 = 14
