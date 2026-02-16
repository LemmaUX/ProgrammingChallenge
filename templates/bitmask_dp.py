"""
Bitmask DP Template

Dynamic programming on subsets using bitmasks.
Efficiently represents which elements are included in a subset.

Use Cases:
- Traveling Salesman Problem (TSP)
- Picking subsets with constraints
- Game state exploration
- Assignment problems

Time Complexity: O(2^n * n) or O(2^n * n^2) depending on problem
Space Complexity: O(2^n)
"""

from typing import List


# ============================================================================
# TEMPLATE 1: Subset Enumeration
# ============================================================================

def iterate_all_subsets(mask: int, n: int) -> List[int]:
    """
    Iterate through all subsets of a mask.
    
    Args:
        mask: Bitmask representing a set
        n: Total number of bits
        
    Returns:
        List of all submasks
    """
    submasks = []
    submask = mask
    
    while submask > 0:
        submasks.append(submask)
        submask = (submask - 1) & mask
    
    submasks.append(0)  # Empty subset
    return submasks


# ============================================================================
# TEMPLATE 2: Traveling Salesman Problem (TSP)
# ============================================================================

def tsp_dp(n: int, dist: List[List[int]]) -> int:
    """
    Solve TSP using dynamic programming with bitmasks.
    
    Args:
        n: Number of cities
        dist: n x n distance matrix where dist[i][j] = distance from i to j
        
    Returns:
        Minimum cost of visiting all cities starting and ending at city 0
    """
    INF = float('inf')
    
    # dp[mask][i] = min cost to visit cities in mask, ending at city i
    dp = [[INF] * n for _ in range(1 << n)]
    
    # Base case: start at city 0
    dp[1][0] = 0
    
    # Iterate through all subsets
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):  # u not in mask
                continue
            if dp[mask][u] == INF:
                continue
            
            # Try extending to next city
            for v in range(n):
                if mask & (1 << v):  # v already in mask
                    continue
                
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
    
    # Find minimum cost: visited all cities, return to city 0
    all_cities = (1 << n) - 1
    result = INF
    for i in range(1, n):
        result = min(result, dp[all_cities][i] + dist[i][0])
    
    return result


# ============================================================================
# TEMPLATE 3: Subset Sum - Maximum Value
# ============================================================================

def subset_sum_max(n: int, items: List[int], target_sum: int) -> int:
    """
    Find maximum value when selecting items with sum <= target_sum.
    
    Standard DP solution illustrating bitmask for state enumeration.
    """
    INF = float('inf')
    
    # dp[mask] = total value when selecting items in mask
    dp = [-1] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == -1:
            continue
        
        for i in range(n):
            if mask & (1 << i):  # Already selected
                continue
            
            new_mask = mask | (1 << i)
            new_value = dp[mask] + items[i]
            dp[new_mask] = max(dp[new_mask], new_value)
    
    # Find maximum value with sum <= target
    result = 0
    for mask in range(1 << n):
        if dp[mask] != -1:
            result = max(result, dp[mask])
    
    return result


# ============================================================================
# TEMPLATE 4: Hamiltonian Path in Small Graph
# ============================================================================

def count_hamiltonian_paths(n: int, adj: List[List[int]]) -> int:
    """
    Count number of Hamiltonian paths (visiting each vertex exactly once).
    
    Args:
        n: Number of vertices
        adj: Adjacency list
        
    Returns:
        Number of Hamiltonian paths
    """
    # dp[mask][i] = number of paths that visit vertices in mask, ending at i
    dp = [[0] * n for _ in range(1 << n)]
    
    # Base case: single vertex paths
    for i in range(n):
        dp[1 << i][i] = 1
    
    # Build up paths
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):  # u not in mask
                continue
            if dp[mask][u] == 0:
                continue
            
            # Extend path to neighbor v
            for v in u + 1 if u < n else []:  # Only need to check next vertices
                for v in adj[u]:
                    if mask & (1 << v):  # v already in path
                        continue
                    
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] += dp[mask][u]
    
    # Count paths visiting all vertices
    all_vertices = (1 << n) - 1
    return sum(dp[all_vertices])


# ============================================================================
# TEMPLATE 5: Maximum Independent Set in Small Graph
# ============================================================================

def maximum_independent_set(n: int, adj: List[List[int]]) -> int:
    """
    Find maximum independent set (largest set where no two vertices are adjacent).
    
    Args:
        n: Number of vertices
        adj: Adjacency list
        
    Returns:
        Size of maximum independent set
    """
    # dp[mask] = True if mask represents an independent set
    dp = [True] * (1 << n)
    
    for mask in range(1 << n):
        # Check if this mask is an independent set
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            
            for v in adj[u]:
                if mask & (1 << v):  # Both u and v in mask (adjacent) - not independent
                    dp[mask] = False
                    break
            
            if not dp[mask]:
                break
    
    # Find maximum size independent set
    result = 0
    for mask in range(1 << n):
        if dp[mask]:
            result = max(result, bin(mask).count('1'))
    
    return result


# ============================================================================
# BITWISE OPERATIONS REFERENCE
# ============================================================================

"""
ESSENTIAL BITWISE OPERATIONS:

1. Check if bit i is set:
   if (mask & (1 << i)) != 0:

2. Set bit i:
   mask |= (1 << i)
   
3. Clear bit i:
   mask &= ~(1 << i)
   
4. Toggle bit i:
   mask ^= (1 << i)
   
5. Count number of set bits:
   bin(mask).count('1')
   
6. Iterate through all subsets of mask:
   submask = mask
   while submask > 0:
       process(submask)
       submask = (submask - 1) & mask

7. Check if mask is subset of another:
   if (mask & full_mask) == mask:

PERFORMANCE:

- For n <= 20: O(2^n) time is acceptable
- For n <= 25: O(2^n) might be tight
- For n > 25: Usually need different approach

"""


# ============================================================================
# KEY INSIGHTS & PATTERNS
# ============================================================================

"""
COMMON DP STATES:

1. dp[mask] = answer when considering subset mask
   - Used when order doesn't matter
   
2. dp[mask][i] = answer when considering mask, ending/at position i
   - TSP, Hamiltonian path problems
   - Allows tracking dependencies on final position
   
3. dp[mask][i] = answer considering first i elements, with mask as extra state
   - Combining bitmask with position
   
OPTIMIZATIONS:

1. Early termination
   - If current solution worse than best found, skip
   
2. Pruning infeasible states
   - Skip states that can never lead to valid solution
   
3. Meeting in the middle
   - For larger n (25-30), split problem in half
   - Enumerate first half (2^(n/2)) and second half separately
   - Combine results

GOTCHAS:

1. Integer overflow
   - Python handles, but watch in C++
   
2. Off-by-one in loop bounds
   - When checking conditions, be careful with bit manipulation
   
3. Submask enumeration direction
   - Goes down to 0, must handle (submask - 1) & mask carefully
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Subset enumeration
    print("=== Subset Enumeration ===")
    mask = 0b101  # Subsets of {0, 2}
    submasks = iterate_all_subsets(mask, 3)
    print(f"Submasks of 0b101: {[bin(s) for s in submasks]}")
    print()
    
    # Maximum independent set (small example)
    print("=== Maximum Independent Set ===")
    n = 4
    adj = [
        [1, 2],      # 0 connected to 1, 2
        [0, 3],      # 1 connected to 0, 3
        [0, 3],      # 2 connected to 0, 3
        [1, 2]       # 3 connected to 1, 2
    ]
    mis_size = maximum_independent_set(n, adj)
    print(f"Maximum independent set size: {mis_size}")
    print()
    
    # Subset enumeration with value
    print("=== Subset with Maximum Value ===")
    items = [1, 2, 3, 4]
    max_val = subset_sum_max(len(items), items, 10)
    print(f"Maximum value (all fit): {max_val}")
