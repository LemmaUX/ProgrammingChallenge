# Bitmask and Combinatorics

Efficient techniques using bit manipulation and combinatorial counting.

## Table of Contents

1. [Bitwise Operations](#bitwise-operations)
2. [Bitmask Techniques](#bitmask-techniques)
3. [Combinatorial Counting](#combinatorial-counting)
4. [Inclusion-Exclusion Principle](#inclusion-exclusion-principle)

---

## Bitwise Operations

### Fundamental Operations

**And (&)**: Intersection of bits
**Or (|)**: Union of bits
**Xor (^)**: Toggle/difference
**Not (~)**: Inversion
**Shift (<<, >>)**: Multiplication/division by powers of 2

### Useful Tricks

```python
# Check if bit i set
if (mask & (1 << i)) != 0:

# Set bit i
mask |= (1 << i)

# Clear bit i
mask &= ~(1 << i)

# Toggle bit i
mask ^= (1 << i)

# Get lowest set bit
mask & (-mask)

# Count set bits
bin(mask).count('1')

# Check if power of 2
if (mask & (mask - 1)) == 0:
```

### Common Patterns

**Check if bit set**: `mask & (1 << i)`
**Set bit**: `mask | (1 << i)`
**Clear bit**: `mask & ~(1 << i)`
**Toggle bit**: `mask ^ (1 << i)`
**Get rightmost set bit**: `mask & -mask`
**Remove rightmost set bit**: `mask & (mask - 1)`

---

## Bitmask Techniques

### Subset Enumeration

**Iterate all subsets of a set**:

```python
mask = full_set
while mask > 0:
    process(mask)
    mask = (mask - 1) & full_set
```

This goes: full set → ... → empty set

Complexity: O(3^n) if process all subsets of all subsets

### Bitmask DP

**State Compression**: Use bitmask as part of DP state

Example: TSP with dp[mask][i] = min cost visiting cities in mask, ending at i

### Maximum Clique in Small Graph

**Definition**: Clique is subset where every vertex connected to every other

**Algorithm**: Check all 2^V subsets, verify clique property

```python
for mask in range(1, 1 << n):
    if is_clique(mask):
        max_size = max(max_size, popcount(mask))
```

---

## Combinatorial Counting

### Permutations and Combinations

**Permutations of n items**: n! = n × (n-1) × ... × 1

**Permutations of n items taken k at a time**:
$$P(n,k) = \frac{n!}{(n-k)!}$$

**Combinations of n items taken k at a time**:
$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

### Pascal's Triangle

**Construction**: C(n, k) = C(n-1, k-1) + C(n-1, k)

```python
C = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    C[i][0] = 1
    for j in range(1, min(i + 1, k + 1)):
        C[i][j] = C[i-1][j-1] + C[i-1][j]
```

**Complexity**: O(n · k)

### Modular Arithmetic for Large Factorials

When computing C(n, k) mod p:

```python
# Precompute factorials modulo p
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = (fact[i-1] * i) % MOD

# Use Fermat's little theorem for modular inverse (p prime)
def modinv(a, p):
    return pow(a, p - 2, p)

def C(n, k, p):
    return fact[n] * modinv(fact[k], p) % p * modinv(fact[n-k], p) % p
```

---

## Inclusion-Exclusion Principle

### Formula

To count elements in union of sets A₁, A₂, ..., Aₙ:

$$|A_1 \cup A_2 \cup ... \cup A_n| = \sum |A_i| - \sum |A_i \cap A_j| + \sum |A_i \cap A_j \cap A_k| - ...$$

### Example: Counting Integers with Constraints

**Problem**: Count integers 1 to n NOT divisible by any of primes p₁, p₂, ...

**Solution**:
1. Start with n (all integers)
2. Subtract those divisible by p₁, p₂, ... 
3. Add back those divisible by pairs (p₁p₂), ...
4. Subtract those divisible by triples
5. Continue alternating

### Implementation Pattern

```python
def count_with_constraints(n, bad_elements):
    """
    Count elements in [1, n] avoiding bad_elements.
    Uses inclusion-exclusion.
    """
    count = 0
    
    # Iterate all subsets of bad_elements
    for mask in range(1, 1 << len(bad_elements)):
        product = 1
        bits = bin(mask).count('1')
        
        for i in range(len(bad_elements)):
            if mask & (1 << i):
                product *= bad_elements[i]
        
        divisible = n // product
        
        # Even number of constraints: add
        # Odd number of constraints: subtract
        if bits % 2 == 1:
            count -= divisible
        else:
            count += divisible
    
    return n - count
```

---

## Advanced Combinatorics

### Derangements

**Definition**: Permutation where no element in original position

$$D(n) = n! \sum_{i=0}^{n} \frac{(-1)^i}{i!}$$

Approximately n!/e

### Catalan Numbers

**Definition**: C_n = (1/(n+1)) × C(2n, n)

Applications: Binary trees, parentheses matching, paths

```python
catalan = [1]
for n in range(1, limit + 1):
    catalan.append(catalan[-1] * 2 * (2*n - 1) // (n + 1))
```

### Stirling Numbers

**1st kind**: Permutations by cycle count
**2nd kind**: Partitions into non-empty subsets

---

## Performance Notes

**Bitwise Operations**: O(1)
**Popcount (count set bits)**: O(log n) or O(1) with hardware support
**Subset enumeration**: O(2^n)
**Triple loop subset**: O(3^n)
**Factorial with mod**: O(n) preprocessing, O(log n) per query

