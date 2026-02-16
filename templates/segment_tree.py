"""
Segment Tree Template

Efficient range query and point update data structure.
Supports minimum, maximum, sum queries and range updates (lazy propagation).

Time Complexity: O(log n) for point update and range query
Space Complexity: O(n)
"""


class SegmentTree:
    """
    Standard segment tree for range sum queries and point updates.
    """
    
    def __init__(self, arr: list[int]):
        """
        Build segment tree from array.
        
        Args:
            arr: Input array
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        """Build tree recursively."""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def update(self, idx: int, val: int):
        """Update element at index idx to value val."""
        self._update_helper(idx, val, 0, 0, self.n - 1)
    
    def _update_helper(self, idx, val, node, start, end):
        """Helper function for update."""
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update_helper(idx, val, 2 * node + 1, start, mid)
            else:
                self._update_helper(idx, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, l: int, r: int) -> int:
        """
        Query sum in range [l, r].
        
        Args:
            l, r: Query range (inclusive)
            
        Returns:
            Sum of elements in range
        """
        return self._query_helper(l, r, 0, 0, self.n - 1)
    
    def _query_helper(self, l, r, node, start, end):
        """Helper function for query."""
        if r < start or end < l:
            return 0  # Out of range
        if l <= start and end <= r:
            return self.tree[node]  # Completely in range
        
        # Partially overlapping
        mid = (start + end) // 2
        left_sum = self._query_helper(l, r, 2 * node + 1, start, mid)
        right_sum = self._query_helper(l, r, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum


# ============================================================================
# SEGMENT TREE WITH LAZY PROPAGATION (Range Updates)
# ============================================================================

class LazySegmentTree:
    """
    Segment tree with lazy propagation for range updates.
    Supports:
    - Range update: Add value to all elements in range
    - Range query: Sum in range
    """
    
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)  # Lazy propagation array
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        """Build tree recursively."""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def _push(self, node, start, end):
        """Push lazy value down to children."""
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            
            if start != end:  # Not a leaf
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            
            self.lazy[node] = 0
    
    def range_update(self, l: int, r: int, val: int):
        """
        Add val to all elements in range [l, r].
        """
        self._range_update_helper(l, r, val, 0, 0, self.n - 1)
    
    def _range_update_helper(self, l, r, val, node, start, end):
        """Helper for range update."""
        self._push(node, start, end)
        
        if r < start or end < l:
            return  # Out of range
        
        if l <= start and end <= r:
            self.lazy[node] += val
            self._push(node, start, end)
            return
        
        mid = (start + end) // 2
        self._range_update_helper(l, r, val, 2 * node + 1, start, mid)
        self._range_update_helper(l, r, val, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def range_query(self, l: int, r: int) -> int:
        """Query sum in range [l, r]."""
        return self._range_query_helper(l, r, 0, 0, self.n - 1)
    
    def _range_query_helper(self, l, r, node, start, end):
        """Helper for range query."""
        if r < start or end < l:
            return 0
        
        self._push(node, start, end)
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self._range_query_helper(l, r, 2 * node + 1, start, mid)
        right_sum = self._range_query_helper(l, r, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Basic Segment Tree
    print("=== Basic Segment Tree ===")
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    
    print(f"Sum [0, 2]: {st.query(0, 2)}")  # 1 + 3 + 5 = 9
    st.update(1, 10)  # Change 3 to 10
    print(f"Sum [0, 2] after update: {st.query(0, 2)}")  # 1 + 10 + 5 = 16
    print()
    
    # Lazy Segment Tree
    print("=== Lazy Segment Tree (Range Update) ===")
    arr2 = [1, 2, 3, 4, 5]
    lst = LazySegmentTree(arr2)
    
    print(f"Sum [0, 4]: {lst.range_query(0, 4)}")  # 15
    lst.range_update(1, 3, 2)  # Add 2 to elements [1,3]
    print(f"Sum [0, 4] after range update: {lst.range_query(0, 4)}")  # 15 + 2*3 = 21
    print(f"Sum [1, 3]: {lst.range_query(1, 3)}")  # (2+2) + (3+2) + (4+2) = 15
