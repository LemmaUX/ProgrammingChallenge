# Mistakes Log

Document of common errors, root causes, and preventive measures.

## Categories of Mistakes

### 1. Logic Errors

#### Off-by-One Errors
**Mistake**: Loop bounds wrong, array access out of bounds
**Root Cause**: Confusing inclusive vs. exclusive bounds
**Prevention**: 
- Use [0, n) convention consistently
- Test boundary carefully: first, last, middle elements
- Draw diagrams for loops

**Example**:
```python
# Wrong:
for i in range(1, n):  # Skips index 0!

# Right:
for i in range(n):
```

#### Boundary Conditions
**Mistake**: Edge cases not handled (empty, size 1, null)
**Root Cause**: Assuming general case always works
**Prevention**:
- Always consider: empty, single element, maximum size
- Write edge cases early, don't save for end

#### Wrong Comparison
**Mistake**: Using > instead of >=, reversed condition
**Root Cause**: Thinking about problem differently than code
**Prevention**:
- Trace through logic with examples
- Match variable semantics with logic

---

### 2. Algorithmic Errors

#### Wrong Algorithm Choice
**Mistake**: Pick slower algorithm than needed
**Root Cause**: Didn't analyze complexity for constraints
**Prevention**:
- Calculate complexity for given n
- Know rule of thumb: 10⁶ operations per second
- Time limit usually 1-2 seconds

#### Incomplete Implementation
**Mistake**: Understood algorithm but implementation buggy
**Root Cause**: Coding faster than thinking
**Prevention**:
- Write pseudocode first
- Code incrementally, test frequently
- Use templates from /templates directory

#### State Not Tracked Properly
**Mistake**: DP state missing important information
**Root Cause**: Incomplete problem analysis
**Prevention**:
- Draw state transition diagram
- Verify all needed information in state
- Check sample traces by hand

---

### 3. Implementation Details

#### Integer Overflow
**Mistake**: Result exceeds integer max
**Root Cause**: Multiplying/adding large numbers
**Prevention**:
- Use 64-bit integers when suspicious
- Check intermediate values
- Use modular arithmetic early

**Example**:
```python
# Python handles arbitrary precision, but other languages:
# a * b might overflow before modulo
result = (a % MOD * b % MOD) % MOD
```

#### Uninitialized Variables
**Mistake**: Using value that was never set
**Root Cause**: Typo or forgotten initialization
**Prevention**:
- Initialize all arrays to proper value
- Use meaningful defaults (0, INF, empty list)

#### Modifying While Iterating
**Mistake**: Changing collection while iterating over it
**Root Cause**: Forgot iteration invalidates references
**Prevention**:
- Iterate over copy if modifying original
- Build new list instead of modifying

---

### 4. Input/Output

#### Wrong Input Parsing
**Mistake**: Reading input incorrectly
**Root Cause**: Didn't read problem format carefully
**Prevention**:
- Read problem line-by-line
- Look at input specification section
- Test parsing on provided examples

#### Output Format Wrong
**Mistake**: Extra spaces, wrong precision, missing newline
**Root Cause**: Not matching expected format exactly
**Prevention**:
- Print exactly as shown in examples
- Check: spaces, newlines, decimal places
- Use strip() carefully

#### Index Off
**Mistake**: 0-indexed vs. 1-indexed confusion
**Root Cause**: Problem uses 1-indexed, code is 0-indexed
**Prevention**:
- Be explicit: add comment for indexing choice
- Use problem's natural indexing when possible

---

### 5. Performance

#### Time Limit Exceeded (TLE)
Common causes:
- Inefficient algorithm (should be O(n log n), using O(n²))
- Repeated computation (should memoize)
- String concatenation in loop (use join)
- Unnecessary list copies

Solution:
- Profile: which line is slow?
- Optimize algorithm, not just code
- Use fast I/O (sys.stdin.readline)

#### Memory Limit Exceeded (MLE)
Common causes:
- Creating unnecessary copies
- Recursion too deep (stack space)
- Storing all partial results

Solution:
- Use generators instead of lists
- Space optimization techniques (rolling array)
- Increase stack size if needed

---

## Prevention Checklist

### Pre-Coding
- [ ] Problem understood completely
- [ ] Input/output format clear
- [ ] Constraints analyzed for algorithm choice
- [ ] Examples traced by hand
- [ ] Edge cases identified

### Coding
- [ ] Incrementally code and test
- [ ] Use templates for common patterns
- [ ] Comments on non-obvious logic
- [ ] Meaningful variable names
- [ ] No commented-out code left

### Testing
- [ ] All provided examples pass
- [ ] Edge cases work
- [ ] Time complexity verified acceptable
- [ ] No warnings or errors
- [ ] Spot-check one manual trace

### Submission
- [ ] Read output format again
- [ ] No debug prints left
- [ ] Removed unnecessary comments
- [ ] Final version tested once more

---

## Learning from Mistakes

### When You Get Wrong Answer (WA)

1. **Reread problem** - You missed something
2. **Check examples** - Does your output match?
3. **Add print statements** - Debug your logic
4. **Consider edge cases** - Empty, single, maximum
5. **Verify algorithm** - Is approach correct?

### When You Get Time Limit (TLE)

1. **Calculate complexity** - Is it acceptable for n?
2. **Profile code** - Where is time spent?
3. **Optimize algorithm** - Not just code tricks
4. **Use fast I/O** - sys.stdin for competitive programming
5. **Prune search space** - Skip obviously bad choices

### When WA Only on Large Cases

1. **Integer overflow** - Use modulo or larger type
2. **Off-by-one** - Boundary conditions wrong
3. **Unhandled edge case** - Empty, single, maximum
4. **Precision** - Floating point rounding
5. **Time limits** - Solution is O(n²) thinking it's O(n)

---

## Debugging Techniques

### Print Statements
```python
print(f"DEBUG: x={x}, y={y}, state={state}")
```

### Assertions
```python
assert len(arr) > 0, "Array should not be empty"
assert n <= 1000000, "n exceeded maximum"
```

### Trace by Hand
- Pick small example
- Execute algorithm step by step
- Match output to expected

### Binary Search on Answer
- If WA on latest test: disable half of changes
- Find which change broke it
- Focus on that area

