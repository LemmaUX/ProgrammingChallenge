# Number Theory

Mathematical foundations for competitive programming problems involving numbers.

## Table of Contents

1. [Modular Arithmetic](#modular-arithmetic)
2. [Greatest Common Divisor](#greatest-common-divisor)
3. [Prime Numbers](#prime-numbers)
4. [Factorization](#factorization)
5. [Advanced Topics](#advanced-topics)

---

## Modular Arithmetic

### Basic Properties

For integer modulus m:

- **(a + b) mod m** = ((a mod m) + (b mod m)) mod m
- **(a - b) mod m** = ((a mod m) - (b mod m) + m) mod m
- **(a × b) mod m** = ((a mod m) × (b mod m)) mod m

### Modular Inverse

**Definition**: a⁻¹ mod m such that a × a⁻¹ ≡ 1 (mod m)

**Exists** when gcd(a, m) = 1

**Computation**:
- Extended GCD for any modulus
- Fermat's Little Theorem if m is prime: a⁻¹ = a^(m-2) mod m

### Modular Exponentiation

**Problem**: Compute a^b mod m efficiently

**Solution**: Binary exponentiation

```python
def powmod(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b & 1:
            result = (result * a) % m
        a = (a * a) % m
        b >>= 1
    return result
```

**Complexity**: O(log b)

---

## Greatest Common Divisor

### Euclidean Algorithm

**Principle**: gcd(a, b) = gcd(b, a mod b)

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

**Complexity**: O(log min(a, b))

### Extended Euclidean Algorithm

**Find**: x, y such that ax + by = gcd(a, b)

```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_val, x, y
```

**Application**: Finding modular inverse

```python
_, x, _ = extended_gcd(a, m)
inv_a = (x % m + m) % m  # Ensure positive
```

---

## Prime Numbers

### Trial Division

```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

**Complexity**: O(√n)

### Sieve of Eratosthenes

**Find all primes** ≤ n

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]
```

**Complexity**: O(n log log n)

### Miller-Rabin Primality Test

**Probabilistic test** for large numbers

**Complexity**: O(k log³ n) for k rounds (negligible error)

---

## Factorization

### Prime Factorization

```python
def prime_factorize(n):
    factors = {}
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return factors
```

**Complexity**: O(√n)

**Optimization**: Check 2 separately, then iterate odd numbers only

### Number of Divisors

**If n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ**, then:

**Number of divisors** = (a₁ + 1) × (a₂ + 1) × ... × (aₖ + 1)

**Sum of divisors** = ∏(1 + p_i + p_i² + ... + p_i^(a_i))

---

## Advanced Topics

### Chinese Remainder Theorem (CRT)

**Problem**: Solve system of congruences

$$x ≡ a_1 \pmod{m_1}$$
$$x ≡ a_2 \pmod{m_2}$$

**Assumption**: gcd(m₁, m₂) = 1

**Solution**:

$$x = a_1 × M_1 × (M_1^{-1} \bmod m_2) + a_2 × M_2 × (M_2^{-1} \bmod m_1)$$

where M₁ = m₂, M₂ = m₁

**Complexity**: O(log min(m₁, m₂))

### Euler's Totient Function

**Definition**: φ(n) = count of integers ≤ n coprime to n

**Formula**:
$$\phi(n) = n \prod_{p | n} (1 - \frac{1}{p})$$

**Computing**:

```python
def euler_totient(n):
    result = n
    p = 2
    
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    if n > 1:
        result -= result // n
    
    return result
```

### Fermat's Little Theorem

**For prime p and a not divisible by p**:

$$a^{p-1} ≡ 1 \pmod{p}$$

**Application**: Compute a^b mod p when p is prime

$$a^b ≡ a^{b \bmod (p-1)} \pmod{p}$$

---

## Practical Competitive Programming

**Common Modulus**: 10⁹ + 7 (prime)

**Large Number Operations**:
1. Always mod intermediate results
2. Watch for negative numbers: (x % p + p) % p
3. Use modular inverse for division

**Optimization Checklist**:
- [ ] Precompute primes with sieve?
- [ ] Precompute factorials for combinatorics?
- [ ] Use powmod for exponentials?
- [ ] Handle edge cases (0, 1, negative)?
- [ ] Overflow check (n² can overflow)?

