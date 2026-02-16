# Graph Theory

Comprehensive guide to graph algorithms and theory.

## Table of Contents

1. [Graph Representations](#graph-representations)
2. [Graph Traversal](#graph-traversal)
3. [Shortest Path Algorithms](#shortest-path-algorithms)
4. [Connectivity and Components](#connectivity-and-components)
5. [Advanced Topics](#advanced-topics)

---

## Graph Representations

### Adjacency List

**When**: Sparse graphs (E << V²)

```python
graph = {0: [1, 2], 1: [2, 3], ...}
```

**Pros**: Memory efficient, fast iteration
**Cons**: Slow edge lookup

### Adjacency Matrix

**When**: Dense graphs, edge queries frequent

```python
adj[i][j] = weight or True/False
```

**Pros**: O(1) edge lookup
**Cons**: O(V²) space always

### Edge List

**When**: Simple algorithm, edge-heavy processing

```python
edges = [(u, v, weight), ...]
```

---

## Graph Traversal

### Breadth-First Search (BFS)

**Use**: Shortest path in unweighted graphs, level-order traversal

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
```

**Complexity**: O(V + E)

### Depth-First Search (DFS)

**Use**: Connectivity, topological sort, cycle detection, paths

```python
def dfs(graph, u, visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited)
```

**Complexity**: O(V + E)

**Variants**:
- **DFS Tree**: Track parent-child relationships
- **Back Edge**: Edge to ancestor (indicates cycle)
- **Forward Edge**: Edge to descendant
- **Cross Edge**: Other edges

---

## Shortest Path Algorithms

### Dijkstra's Algorithm

**When**: Non-negative edge weights, single source

**Approach**: Greedy, relax edges in order of distance

```
while priority_queue not empty:
    u = pop minimum distance node
    for each neighbor v of u:
        if dist[u] + weight(u,v) < dist[v]:
            dist[v] = dist[u] + weight(u,v)
            push v to queue
```

**Complexity**: O((V + E) log V) with binary heap

### Bellman-Ford Algorithm

**When**: Can handle negative weights, single source

**Approach**: Relax all edges repeatedly

```
for 1 to V-1:
    for each edge (u, v, w):
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

Detect negative cycle in final iteration
```

**Complexity**: O(V · E)

### Floyd-Warshall Algorithm

**When**: All-pairs shortest path, small graphs

**Approach**: Dynamic programming on intermediate vertices

```
for k in 0..V-1:
    for i in 0..V-1:
        for j in 0..V-1:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**Complexity**: O(V³)

### 0-1 BFS

**When**: Only 0 and 1 edge weights

**Approach**: BFS with deque, add 0-edges to front

```
if weight == 0:
    deque.appendleft(v)  # Process immediately
else:
    deque.append(v)      # Process later
```

**Complexity**: O(V + E)

---

## Connectivity and Components

### Union-Find (Disjoint Set Union)

**Purpose**: Track connected components efficiently

**Operations**:
- `find(x)`: Get root/representative
- `union(x, y)`: Merge components
- `connected(x, y)`: Check same component

**Complexity**: Nearly O(1) amortized with path compression and union by rank

### Strongly Connected Components (SCC)

**Definition**: Maximal subgraph where every vertex reachable from every other

**Kosaraju's Algorithm**:
1. DFS on original graph, record finish times
2. DFS on reversed graph in decreasing finish time order
3. Each DFS tree is one SCC

**Complexity**: O(V + E)

### Bridges and Articulation Points

**Articulation Point**: Vertex whose removal disconnects graph

**Bridge**: Edge whose removal disconnects graph

**Finding** (Tarjan's Algorithm): DFS with low-link values

---

## Advanced Topics

### Minimum Spanning Tree (MST)

**Definition**: Spanning tree with minimum edge weight sum

**Kruskal's Algorithm**:
1. Sort edges by weight
2. Use Union-Find to check cycles
3. Add edge if doesn't create cycle

**Prim's Algorithm**:
1. Start from arbitrary vertex
2. Repeatedly add cheapest edge connecting tree to non-tree vertex

**Complexity**: O(E log E) for Kruskal, O(E log V) for Prim with heap

### Network Flow

**Max Flow Problem**: Find maximum flow from source to sink

**Ford-Fulkerson Method**:
- Find augmenting path using BFS/DFS
- Add min capacity along path
- Repeat until no path exists

**Complexity**: Depends on implementation, O(V · E²) naive

### Topological Sorting

**Definition**: Linear ordering where u comes before v for edge u→v

**Kahms Algorithm**: BFS with in-degrees
**DFS Algorithm**: Finish time ordering

**Complexity**: O(V + E)

---

## Implementation Checklist

- [ ] Graph immutability (no modification during traversal)
- [ ] Disconnected graphs (visit all vertices)
- [ ] Self-loops and parallel edges
- [ ] Directed vs undirected
- [ ] Weighted vs unweighted
- [ ] Large graphs (optimize space)

