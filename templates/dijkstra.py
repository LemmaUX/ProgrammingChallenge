"""
Dijkstra's Algorithm Template

Single-source shortest path algorithm for graphs with non-negative weights.
Greedy algorithm that always expands the closest unexplored node.

Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict
from typing import List, Tuple, Dict


def dijkstra_basic(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Find shortest paths from start node to all other nodes.
    
    Args:
        graph: Adjacency list, graph[u] = [(v, weight), ...]
        start: Starting node
        
    Returns:
        Dictionary where dist[node] = shortest distance from start
    """
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    
    # Min heap of (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        # If we popped a stale entry with larger distance, skip
        if d > dist[u]:
            continue
        
        # Relax edges
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist


def dijkstra_with_path(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Tuple[Dict[int, int], Dict[int, int]]:
    """
    Dijkstra with path reconstruction.
    
    Returns:
        (distances, parents) where parents[node] = previous node on shortest path
    """
    dist = defaultdict(lambda: float('inf'))
    parent = {}
    dist[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return dist, parent


def reconstruct_path(parent: Dict[int, int], start: int, end: int) -> List[int]:
    """
    Reconstruct path from parent dictionary.
    """
    path = []
    current = end
    while current in parent:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path if path[-1] == end else []  # Empty if no path


# ============================================================================
# VARIANT: 0-1 BFS (For graphs with only 0 and 1 weights)
# ============================================================================

def dijkstra_01_bfs(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    0-1 BFS: Optimized for graphs with only 0 and 1 weighted edges.
    Uses deque instead of heap for better performance.
    
    Args:
        graph: Adjacency list with weights 0 or 1 only
        start: Starting node
        
    Returns:
        Dictionary of shortest distances
    """
    from collections import deque
    
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    
    dq = deque([start])
    
    while dq:
        u = dq.popleft()
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                if weight == 0:
                    dq.appendleft(v)  # 0-weight edges processed first
                else:
                    dq.append(v)
    
    return dist


# ============================================================================
# VARIANT: Multi-source Dijkstra
# ============================================================================

def dijkstra_multi_source(graph: Dict[int, List[Tuple[int, int]]], sources: List[int]) -> Dict[int, int]:
    """
    Find shortest distance from any source to all nodes.
    
    Args:
        graph: Adjacency list
        sources: List of source nodes
        
    Returns:
        Dictionary of shortest distances from any source
    """
    dist = defaultdict(lambda: float('inf'))
    for s in sources:
        dist[s] = 0
    
    pq = [(0, s) for s in sources]
    heapq.heapify(pq)
    visited = set()
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist


# ============================================================================
# COMMON PITFALLS & OPTIMIZATIONS
# ============================================================================

"""
PITFALLS:

1. Negative weights
   - Dijkstra does NOT work with negative edges
   - Use Bellman-Ford for negative weights
   - Use 0-1 BFS only if all weights are 0 or 1

2. Stale queue entries
   - Don't remove from queue when distance improves
   - Instead, check if d > dist[u] when popping and skip
   - Or use visited set to skip already processed nodes

3. Unbounded graph
   - If using defaultdict(lambda: float('inf')), be careful
   - Ensure graph is finite and reachable from source

4. Integer overflow
   - If weights are large, ensure distances don't overflow
   - In Python this isn't an issue, but watch in other languages

OPTIMIZATIONS:

1. Early termination
   - If only need distance to one target, stop when popped
   
2. 0-1 BFS
   - Use deque instead of heap for 0-1 weights
   - Faster than heap-based Dijkstra
   
3. Bidirectional search
   - Search from both start and end simultaneously
   - Meet in the middle for faster results
   
4. Constraint propagation
   - Skip relaxing edges that won't help
   - Prune based on heuristics (A* algorithm)
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Basic Dijkstra
    print("=== Basic Dijkstra ===")
    graph = {
        0: [(1, 4), (2, 2)],
        1: [(2, 1), (3, 5)],
        2: [(3, 8), (4, 10)],
        3: [(4, 2)],
        4: []
    }
    
    dist = dijkstra_basic(graph, 0)
    print(f"Distances from 0: {dict(dist)}")
    # Expected: {0: 0, 1: 4, 2: 2, 3: 7, 4: 9}
    print()
    
    # Dijkstra with path reconstruction
    print("=== Dijkstra with Path ===")
    dist, parent = dijkstra_with_path(graph, 0)
    print(f"Path from 0 to 4: {reconstruct_path(parent, 0, 4)}")
    print(f"Distance: {dist[4]}")
    print()
    
    # Multi-source Dijkstra
    print("=== Multi-source Dijkstra ===")
    dist_multi = dijkstra_multi_source(graph, [0, 1])
    print(f"Distances from sources {0, 1}: {dict(dist_multi)}")
