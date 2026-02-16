"""
Fast I/O Template

Optimized input/output for competitive programming.
Standard input/output can be slow for large test cases.
Fast I/O patterns provide significant speedup.

Performance Impact:
- Standard input(): Can be 10-100x slower for large inputs
- sys.stdin.readline(): 5-50x faster
- Pre-compiled regex: Minimal overhead
"""

import sys
from io import StringIO
from typing import List, Tuple, Any


# ============================================================================
# METHOD 1: sys.stdin for Fast Input
# ============================================================================

def fast_input() -> str:
    """Read single line of input quickly."""
    return sys.stdin.readline().rstrip()


def read_int() -> int:
    """Read single integer."""
    return int(sys.stdin.readline())


def read_ints() -> List[int]:
    """Read line of space-separated integers."""
    return list(map(int, sys.stdin.readline().split()))


def read_string() -> str:
    """Read single string (strip whitespace)."""
    return sys.stdin.readline().strip()


def read_strings() -> List[str]:
    """Read line of space-separated strings."""
    return sys.stdin.readline().split()


# ============================================================================
# METHOD 2: Batch Reading for Large Inputs
# ============================================================================

def read_all_input() -> str:
    """Read entire input at once (fastest for very large inputs)."""
    return sys.stdin.read()


def fast_input_loader(n_lines: int) -> List[str]:
    """Pre-load n lines for batch processing."""
    return [sys.stdin.readline().rstrip() for _ in range(n_lines)]


# ============================================================================
# METHOD 3: Optimized Output
# ============================================================================

class FastOutput:
    """Buffer output to reduce system calls."""
    
    def __init__(self):
        self.buffer = []
    
    def write(self, obj: Any) -> None:
        """Add to output buffer."""
        self.buffer.append(str(obj))
    
    def writeln(self, obj: Any) -> None:
        """Add to output buffer with newline."""
        self.buffer.append(str(obj))
        self.buffer.append('\n')
    
    def flush(self) -> None:
        """Print all buffered output at once."""
        sys.stdout.write(''.join(self.buffer))
        self.buffer.clear()


def print_fast(*args, **kwargs) -> None:
    """Faster print (though standard print is okay for most problems)."""
    sys.stdout.write(' '.join(map(str, args)))
    sys.stdout.write('\n')


# ============================================================================
# METHOD 4: Specialized Readers for Common Patterns
# ============================================================================

def read_matrix(rows: int, cols: int = None) -> List[List[int]]:
    """Read matrix of integers."""
    if cols is None:
        return [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
    return [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]


def read_graph(n_vertices: int, n_edges: int) -> dict:
    """Read graph as adjacency list."""
    from collections import defaultdict
    graph = defaultdict(list)
    
    for _ in range(n_edges):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    return graph


def read_weighted_graph(n_vertices: int, n_edges: int) -> dict:
    """Read weighted graph."""
    from collections import defaultdict
    graph = defaultdict(list)
    
    for _ in range(n_edges):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    return graph


# ============================================================================
# COMPETITIVE PROGRAMMING TEMPLATE (Ready to Copy)
# ============================================================================

def solve():
    """
    Main solution. Replace this with your algorithm.
    """
    # Fast input
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    # Your solution here
    result = sum(arr)
    
    # Fast output
    print(result)


# ============================================================================
# ADVANCED: Custom Parsing
# ============================================================================

def parse_line(line: str, types: List[type] = None) -> List[Any]:
    """
    Parse line with specific types.
    
    Args:
        line: Input line
        types: List of types to convert to (default all int)
        
    Returns:
        Parsed values
    """
    if types is None:
        return list(map(int, line.split()))
    
    parts = line.split()
    return [t(p) for t, p in zip(types, parts)]


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

"""
TIMING RESULTS (approximate, for 1 million integers):

Method                          Time (seconds)
-----------------------------------------------
input() in loop                 3.5-5.0
sys.stdin.readline() loop       0.15-0.3
sys.stdin.read() + split()      0.05-0.1
Pre-compiled + sys.stdin        0.04-0.08

CODEFORCES/LEETCODE VERDICT:
- Standard input/print: Works for most problems
- Use fast I/O when: TLE with standard methods

OUTPUT OPTIMIZATION:
- print(): "Slow" for many small prints
- sys.stdout.write(): Faster for many small outputs
- Buffer approach: Fastest for very many outputs
"""


# ============================================================================
# TEMPLATE: Complete Fast Solution
# ============================================================================

"""
# ============================================================
# COPY THIS TEMPLATE FOR FAST I/O SOLUTION
# ============================================================

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Your solution code here
    result = sum(arr)
    
    print(result)

if __name__ == "__main__":
    solve()

# ============================================================
# Alternative: Using sys.stdin directly
# ============================================================

import sys
from collections import defaultdict

def main():
    lines = sys.stdin.read().strip().split('\\n')
    
    # Parse input
    n = int(lines[0])
    commands = []
    for i in range(1, n + 1):
        commands.append(lines[i].split())
    
    # Process and output
    results = []
    for cmd in commands:
        # Processing
        results.append(str(result_value))
    
    sys.stdout.write('\\n'.join(results) + '\\n')

if __name__ == "__main__":
    main()

# ============================================================
# Pattern: Competitive Programming Template
# ============================================================

import sys
input = sys.stdin.readline

def solve():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Solution
        answer = calculate_answer(arr)
        print(answer)

def calculate_answer(arr):
    # Your algorithm
    return sum(arr)

if __name__ == "__main__":
    solve()
"""


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Example: Reading and processing with fast I/O
    # Uncomment to test:
    
    # # Fast output example
    # output = FastOutput()
    # for i in range(5):
    #     output.writeln(f"Result {i}: {i * 2}")
    # output.flush()
    
    # # Matrix reading example (requires input)
    # # matrix = read_matrix(3, 3)
    # # print(matrix)
    
    print("Fast I/O template ready for use.")
    print("Use: import sys; input = sys.stdin.readline")
