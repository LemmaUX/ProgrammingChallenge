# Interview Strategies

Tactical and strategic approaches for excelling in technical interviews.

## Pre-Interview Preparation

### 1. Problem Categories to Master

**Must Know**: Arrays, Strings, Trees, Graphs, Sorting, Dynamic Programming

**Should Know**: Heaps, Stacks, Queues, Tries, Hash Tables, Linked Lists

**Nice to Know**: Geometry, System Design, Advanced DP

### 2. Build Mental Framework

**Algorithm Recognition Pattern**:
1. **Constraints** → Algorithm choice
2. **Data structure** → Memory layout
3. **Time complexity** → Feasibility
4. **Edge cases** → Special handling

### 3. Practice Strategically

**Focus on understanding**, not memorization:
- Solve same problem 3 different ways
- Trace through examples carefully
- Explain solution aloud (practice verbalizing)
- Write without looking at solution

**Progression**:
- Week 1-2: Easy problems, refine ability to code cleanly
- Week 3-4: Medium problems, practice communicating
- Week 5-6: Hard problems, work on time management
- Week 7+: Contest-style timed problems

---

## During Interview

### 1. Problem Understanding Phase

**Allocate 2-3 minutes**

**Actions**:
- Read problem carefully (twice)
- Clarify ambiguities with interviewer
- Ask about constraints: n range, duplicates, negative?
- Confirm outputs and error cases

**Red flags**:
- Unclear what "optimal" means
- Input format ambiguous
- Hidden constraints

### 2. Problem Analysis Phase

**Allocate 5-10 minutes**

**Actions**:
- Trace through provided examples
- Identify patterns: sorted? duplicate-free? small n?
- Consider multiple approaches (brute → optimized)
- State time/space complexity for each approach

**Discuss with interviewer**:
> "Brute force would be O(n²), which might be too slow. Let me try a binary search approach instead: O(n log n)."

### 3. Design Phase

**Allocate 2-5 minutes (for medium) or 10+ (for system design)**

**Actions**:
- Pseudocode or rough approach
- Walk through approach on example
- Get interviewer approval before coding

**Sample explanation**:
> "I'll use a hash map to track frequencies, then iterate through the array once. For each element, check if its complement (target - element) exists in the map."

### 4. Coding Phase

**Allocate 10-15 minutes**

**Principles**:
- **Clarity first**: Use meaningful variable names
- **Comments**: Explain non-obvious logic
- **Incremental**: Code part, test part
- **Ask aloud**: "Should I handle null input?"

**Clean code patterns**:
```python
def solution(arr, target):
    """Solve problem for given arr and target."""
    # Handle edge cases
    if not arr:
        return None
    
    # Main logic
    result = calculate(arr)
    
    # Validate and return
    return result
```

### 5. Testing Phase

**Allocate 5-10 minutes**

**Test categories** (in order):
1. **Provided examples**: Must pass
2. **Edge cases**: Empty, single, duplicates
3. **Boundary values**: Min/max possible
4. **Custom cases**: Particularly tricky for algorithm

**While testing**:
- Walk through code line-by-line
- Verify variable state at each step
- Catch off-by-one errors

### 6. Optimization Phase

**Only if time remains or interviewer asks**

**Approaches**:
- **Algorithm optimization**: Faster approach if exists
- **Constant optimization**: Remove unnecessary work
- **Space optimization**: Reduce extra memory

> "The current solution is O(n²) time. There's no better algorithm for this problem, but I could optimize constants by..."

---

## Communication Strategies

### 1. Explain Your Thinking

**Good**: "I'll sort the array first because we can use binary search."

**Bad**: Silent for 5 minutes, then show code.

### 2. Ask Clarifying Questions

**Good questions**:
- "Can the array have duplicates?"
- "Should I handle negative numbers?"
- "Is O(n²) acceptable for n = 10⁶?"

**Signals competence**: Shows you think about edge cases and constraints.

### 3. State Complexity

**After each approach**: "This is O(n log n) time, O(n) space."

**Interviewer might say**: "Can you do better on space?"

**Then you optimize or confirm optimal.**

### 4. Explain Trade-offs

> "A hash table uses O(n) space but gives O(1) lookups. Alternatively, I could sort first (O(n log n) time, O(1) space) and use binary search."

### 5. Admit When Stuck

**Good**: "I'm not sure about this edge case. Let me think... Could you clarify if duplicates are expected?"

**Bad**: Silent struggle for 2 minutes; never ask for help.

**Interviewers respect**: Asking for hints over being stuck.

---

## Common Problem Patterns

### 1. Array/String

**Recognize**: Two pointers, sliding window, hash map, sorting

**Interview strategy**:
- Clarify: sorted? unique elements? constraints?
- Propose: brute O(n²), then optimize to O(n)
- Code: clean with comments

### 2. Tree

**Recognize**: DFS, BFS, recursion, level-order

**Interview strategy**:
- Draw the tree problem out
- Trace recursive solutions clearly
- Discuss: in-order vs. post-order vs. pre-order

### 3. Graph

**Recognize**: Connected components, paths, cycles, topological sort

**Interview strategy**:
- Clarify: directed? weighted? path definition?
- Choose: DFS vs. BFS vs. Dijkstra
- Code: adjacency list for sparse, matrix for dense

### 4. DP

**Recognize**: Optimal substructure, overlapping subproblems

**Interview strategy**:
- Define state clearly: "dp[i] = max value using first i items"
- Write recurrence: "dp[i] = max(dp[i-1], dp[i-1] + value[i])"
- Trace on example
- Code bottom-up (avoid stack overflow risk)

---

## Time Management

### Ideal Timeline for 45-minute Interview

- 0-2 min: Understand
- 2-7 min: Analyze & design
- 7-25 min: Code
- 25-35 min: Test
- 35-45 min: Optimize / discuss

**Flexible** based on problem difficulty:
- Easy problem: Spend more time testing, discussing
- Hard problem: Spend more time designing

**Danger signs**:
- Code at 20-minute mark → likely TLE
- Still designing at 15-minute mark → might not finish

---

## Handling Wrong Answers

### If Logic Error

**Strategy**:
1. Don't immediately rewrite
2. Find the bug by tracing
3. Fix specific line
4. Re-test that case only

### If Algorithm Wrong

**Strategy**:
1. Acknowledge: "Actually, this approach won't work because..."
2. Propose new: "Let me try..."
3. Get approval before recoding

### If Time Pressure

**Strategy**:
1. Code what you have (partial credit)
2. Write pseudocode for rest
3. Explain what would happen if completed

---

## Post-Interview

### What Interviewers Evaluate

✅ **Problem-solving**: Correct approach, optimization
✅ **Coding**: Clean code, no off-by-one errors
✅ **Communication**: Explaining thinking process
✅ **Testing**: Finding edge cases
✅ **Complexity analysis**: Understanding efficiency

❌ **Poor signs**:
- Silent for long periods
- Can't trace own code
- Ignores edge cases
- Finish correctly but can't optimize

### Learning from Interview

After each practice/real interview:
1. What went well?
2. What was hard?
3. What would you do differently next time?
4. Practice that specific weakness

---

## Company-Specific Strategies

### FAANG Companies

**Google**: System design, optimization, clear thinking
**Facebook**: Fast coding, communication, trade-off discussion
**Apple**: Strong fundamentals, edge case handling
**Amazon**: Efficiency (time/space), scalability thinking
**Microsoft**: Clean code, problem variations

### Preparation Levels

**Level 1**: LeetCode Easy (need 50+)
**Level 2**: LeetCode Medium (need 30+)
**Level 3**: Some Hard plus problem variations
**Expert**: Hard problems, novel approaches, extensions

---

## Resources and Practice

**Online Judges**: LeetCode, HackerRank, CodeForces
**Books**: Cracking the Coding Interview, System Design Interview
**Strategy**: Do problems, review solutions, do variants, simulate interviews

