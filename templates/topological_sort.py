"""
Topological Sort Template

Ordering of directed acyclic graph (DAG) vertices such that for every edge u -> v,
u comes before v in the ordering.

Use Cases:
- Course prerequisites
- Task scheduling with dependencies
- Build system dependency resolution
- Instruction scheduling

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import defaultdict, deque
from typing import List, Dict


def topological_sort_kahn(n_vertices: int, edges: List[tuple]) -> List[int]:
    """
    Kahn's algorithm using in-degree and BFS.
    
    Args:
        n_vertices: Number of vertices (0 to n_vertices-1)
        edges: List of (u, v) representing edge from u to v
        
    Returns:
        List of vertices in topological order, or empty if cycle detected
    """
    # Build adjacency list and in-degree
    graph = defaultdict(list)
    in_degree = [0] * n_vertices
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Start with all vertices of in-degree 0
    queue = deque(v for v in range(n_vertices) if in_degree[v] == 0)
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # Reduce in-degree for all neighbors
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # If all vertices processed, no cycle; otherwise, cycle exists
    return result if len(result) == n_vertices else []


def topological_sort_dfs(n_vertices: int, edges: List[tuple]) -> List[int]:
    """
    DFS-based topological sort (more intuitive for some problems).
    
    Args:
        n_vertices: Number of vertices (0 to n_vertices-1)
        edges: List of (u, v) representing edge from u to v
        
    Returns:
        List of vertices in topological order
    """
    graph = defaultdict(list)
    visited = [0] * n_vertices  # 0: unvisited, 1: visiting, 2: visited
    result = []
    has_cycle = False
    
    def dfs(u):
        nonlocal has_cycle
        
        if visited[u] == 1:  # Currently visiting - cycle detected
            has_cycle = True
            return
        if visited[u] == 2:  # Already visited
            return
        
        visited[u] = 1  # Mark as visiting
        
        for v in graph[u]:
            dfs(v)
        
        visited[u] = 2  # Mark as visited
        result.append(u)  # Add to result AFTER visiting all descendants
    
    for u, v in edges:
        graph[u].append(v)
    
    # Visit all vertices
    for i in range(n_vertices):
        if visited[i] == 0:
            dfs(i)
    
    if has_cycle:
        return []
    
    result.reverse()  # DFS results in reverse topological order
    return result


# ============================================================================
# VARIANT: Longest Path in DAG (Using Topological Sort)
# ============================================================================

def longest_path_in_dag(n_vertices: int, edges: List[tuple], weights: Dict[tuple, int] = None) -> Dict[int, int]:
    """
    Find longest path from each vertex (weight = 1 by default).
    
    Args:
        n_vertices: Number of vertices
        edges: List of (u, v) edges
        weights: Dictionary mapping edge to weight (default 1)
        
    Returns:
        Dictionary where longest_path[u] = longest path starting from u
    """
    if weights is None:
        weights = {}
    
    graph = defaultdict(list)
    in_degree = [0] * n_vertices
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Kahn's algorithm to get topological order
    queue = deque(v for v in range(n_vertices) if in_degree[v] == 0)
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # DP on DAG: process in reverse topological order
    longest_path = [0] * n_vertices
    
    for u in reversed(topo_order):
        for v in graph[u]:
            edge_weight = weights.get((u, v), 1)
            longest_path[u] = max(longest_path[u], edge_weight + longest_path[v])
    
    return {i: longest_path[i] for i in range(n_vertices)}


# ============================================================================
# VARIANT: All Paths Enumeration in DAG
# ============================================================================

def count_paths_in_dag(n_vertices: int, edges: List[tuple], start: int) -> int:
    """
    Count number of paths from start to each vertex.
    """
    graph = defaultdict(list)
    in_degree = [0] * n_vertices
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Topological sort
    queue = deque(v for v in range(n_vertices) if in_degree[v] == 0)
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # DP: count paths
    dp = [0] * n_vertices
    dp[start] = 1
    
    for u in topo_order:
        for v in graph[u]:
            dp[v] += dp[u]
    
    return {i: dp[i] for i in range(n_vertices)}


# ============================================================================
# KEY INSIGHTS
# ============================================================================

"""
CHOOSING ALGORITHM:

Kahn's Algorithm:
- Better for cycle detection
- Clearer when we need in-degree concept
- More intuitive for level-based problems

DFS Algorithm:
- More compact code
- Works well with recursive substructures
- Better for path reconstruction

DETECTING CYCLES:

Kahn: If result size < n_vertices, cycle exists

DFS: 
- Use visited states: 0 (unvisited), 1 (visiting), 2 (visited)
- Cycle = visiting same node while still in DFS recursion

APPLICATIONS:

1. Course Prerequisites
   - Edge: course A must be taken before B
   - Problem: Find valid enrollment order

2. Task Scheduling
   - Edge: task A must complete before B
   - Problem: Find minimum completion time

3. Build Systems
   - Edge: source file depends on header
   - Problem: Find compilation order

4. Longest Path in DAG
   - Use DP on topological order
   - O(V + E) instead of brute force
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Basic topological sort (Kahn's algorithm)
    print("=== Kahn's Algorithm ===")
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    result = topological_sort_kahn(5, edges)
    print(f"Topological order: {result}")
    # Expected: [0, 1, 2, 3, 4] or [0, 2, 1, 3, 4], etc.
    print()
    
    # DFS-based topological sort
    print("=== DFS Topological Sort ===")
    result_dfs = topological_sort_dfs(5, edges)
    print(f"Topological order (DFS): {result_dfs}")
    print()
    
    # Cycle detection
    print("=== Cycle Detection ===")
    cycle_edges = [(0, 1), (1, 2), (2, 0)]  # Creates cycle
    result_cycle = topological_sort_kahn(3, cycle_edges)
    print(f"Result (should be empty): {result_cycle}")
    print()
    
    # Longest path in DAG
    print("=== Longest Path in DAG ===")
    dag_edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    longest = longest_path_in_dag(4, dag_edges)
    print(f"Longest paths: {longest}")
    # From 0: paths go to 1->3 (2 edges) or 2->3 (2 edges), so 2
    print()
    
    # Count paths
    print("=== Count Paths ===")
    path_counts = count_paths_in_dag(4, dag_edges, 0)
    print(f"Path counts from 0: {path_counts}")
    # To 3: can go 0->1->3 or 0->2->3, so 2 paths
