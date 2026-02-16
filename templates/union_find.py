"""
Union-Find (Disjoint Set Union) Template

Efficiently manages dynamic connectivity and cycle detection.
Implements path compression and union by rank optimizations.

Time Complexity: Nearly O(1) amortized with path compression and union by rank
Space Complexity: O(n)
"""


class UnionFind:
    """
    Standard Union-Find data structure with path compression and union by rank.
    """
    
    def __init__(self, n: int):
        """
        Initialize Union-Find with n elements (0-indexed).
        
        Args:
            n: Number of elements in the set
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  # Size of each connected component
    
    def find(self, x: int) -> int:
        """
        Find the root/representative of element x with path compression.
        
        Path compression: Make every element directly point to root.
        This dramatically speeds up future operations.
        
        Args:
            x: Element to find root for
            
        Returns:
            Root/representative of x's component
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """
        Union two elements (merge their components).
        Uses union by rank to keep tree depth small.
        
        Args:
            x: First element
            y: Second element
            
        Returns:
            True if union occurred (were in different sets), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank: attach smaller tree to larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x: int, y: int) -> bool:
        """
        Check if two elements are in the same component.
        """
        return self.find(x) == self.find(y)
    
    def get_size(self, x: int) -> int:
        """
        Get size of component containing x.
        """
        return self.size[self.find(x)]
    
    def get_num_components(self) -> int:
        """
        Get number of distinct components.
        """
        return len(set(self.find(i) for i in range(len(self.parent))))


# ============================================================================
# VARIANT: Weighted Union-Find (for potential differences)
# ============================================================================

class WeightedUnionFind:
    """
    Union-Find that maintains potential differences between connected elements.
    Useful for "relation" problems where we need to know distance/difference.
    
    Maintains: potential[i] = potential[find(i)] - potential[i]
    """
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.potential = [0] * n  # Potential difference from parent
    
    def find(self, x: int) -> int:
        """
        Find root and update potential to account for all ancestors.
        """
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            self.potential[x] += self.potential[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]
    
    def union(self, x: int, y: int, weight: int) -> bool:
        """
        Union x and y with relationship: value[y] - value[x] = weight
        
        Args:
            x: First element
            y: Second element
            weight: y's potential - x's potential
            
        Returns:
            True if union successful (were in different sets)
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # potential[root_y] + potential[y] - potential[x] = weight
        # potential[root_y] = weight + potential[x] - potential[y]
        self.potential[root_y] = weight + self.potential[x] - self.potential[y]
        self.parent[root_y] = root_x
        
        return True
    
    def get_difference(self, x: int, y: int) -> int:
        """
        Get potential difference between x and y if in same component.
        Returns None if not in same component.
        """
        if self.find(x) != self.find(y):
            return None
        return self.potential[y] - self.potential[x]


# ============================================================================
# COMMON USE CASES
# ============================================================================

"""
USE CASES:

1. Connected Components
   - Find number of connected components in graph
   - Check if two nodes are connected
   
2. Cycle Detection
   - Detect cycle in undirected graph
   - If union returns False, adding edge creates cycle
   
3. Kruskal's Algorithm
   - Minimum spanning tree construction
   - Union edges in weight order, skip if creates cycle
   
4. Equivalence Relations
   - Group elements where certain relations hold
   - More efficient than DFS/BFS for static connectivity
   
5. Potential Differences
   - "Relation" problems: know exact distances
   - Difference constraints: check if configuration valid

WHEN TO USE vs DFS/BFS:
- Union-Find: Static connectivity queriesafter all unions known (offline)
- DFS/BFS: Dynamic connectivity or graph algorithms needing actual traversal
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Basic Union-Find: Detecting cycle in undirected graph
    print("=== Basic Union-Find Example ===")
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # Contains cycle
    uf = UnionFind(4)
    
    has_cycle = False
    for u, v in edges:
        if not uf.union(u, v):
            print(f"Cycle detected: edge ({u}, {v}) creates cycle")
            has_cycle = True
        else:
            print(f"Union {u} and {v}")
    
    print(f"Has cycle: {has_cycle}")
    print(f"Connected components: {uf.get_num_components()}")
    print()
    
    # Weighted Union-Find: Relation problems
    print("=== Weighted Union-Find Example ===")
    wuf = WeightedUnionFind(3)
    
    # x + 2 = y
    wuf.union(0, 1, 2)
    print(f"Difference 0->1: {wuf.get_difference(0, 1)}")
    
    # y + 3 = z => x + 5 = z
    wuf.union(1, 2, 3)
    print(f"Difference 0->2: {wuf.get_difference(0, 2)}")
