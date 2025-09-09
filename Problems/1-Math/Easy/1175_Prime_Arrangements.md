<div align="center">

# 🧠 [1175. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201175-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/prime-arrangements/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                 |
| ------------------- | --------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                           |
| **Acceptance Rate** | `60.0%`                                                               |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/prime-arrangements/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)    |

## Description

<!-- description:start -->

<p>Return the number of permutations of 1 to <code>n</code> so that prime numbers are at prime indices (1-indexed.)</p>

<p><em>(Recall that an integer&nbsp;is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers&nbsp;both smaller than it.)</em></p>

<p>Since the answer may be large, return the answer <strong>modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 12
<strong>Explanation:</strong> For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> 682289015
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `07-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `07-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Theoretical (Only for intuition, not feasible - Brute Force)

#### 📝 Intuition

> The most straightforward way to solve this problem is to generate all possible permutations of numbers from `1` to `n` and check if prime numbers are located only at prime indices. If yes, count that permutation as valid.
> This is intuitive but extremely inefficient, since `n!` grows faster than exponential.

#### 🔍 Algorithm

```pseudo
function numPrimeArrangements(n):
    primes = list of primes ≤ n
    total = 0
    for each permutation perm of [1..n]:
        if all primes are at prime indices in perm:
            total += 1
    return total % (1e9+7)
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int numPrimeArrangements(int n) {
        vector<int> arr(n);
        iota(arr.begin(), arr.end(), 1);
        long long mod = 1e9+7;
        long long count = 0;

        do {
            bool valid = true;
            for (int i = 0; i < n; i++) {
                if (isPrime(arr[i]) && !isPrime(i+1)) {
                    valid = false;
                    break;
                }
            }
            if (valid) count++;
        } while (next_permutation(arr.begin(), arr.end()));

        return count % mod;
    }

    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i*i <= x; i++)
            if (x % i == 0) return false;
        return true;
    }
};
```

### 🥈 Approach 2: Precomputation version → small optimization (Optimized Solution)

#### 📝 Intuition

> Instead of checking all permutations, we can count directly:
>
> - Let p = number of primes ≤ n.
> - We need to place primes into p prime indices → there are p! ways.
> - The remaining n-p non-primes go into n-p non-prime indices → (n-p)! ways.
> - Answer = (p! \* (n-p)!) % mod.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    p = countPrimes(n)
    return factorial(p) * factorial(n-p) % (1e9+7)
```

#### 💻 Implementation

```cpp
// Optimized approach with prime counting
class Solution {
    const int MOD = 1e9+7;

    long long factorial(int x) {
        long long res = 1;
        for (int i = 2; i <= x; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }

    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i*i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

public:
    int solutionOptimized(int n) {
        int primeCount = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) primeCount++;
        }
        int nonPrimeCount = n - primeCount;
        return (factorial(primeCount) * factorial(nonPrimeCount)) % MOD;
    }
};
```

### 🥇 Approach 3: Precomputation version (Optimal Solution ⭐)

#### 📝 Intuition

> Since n ≤ 100, we can precompute:
>
> - Prime numbers count up to 100 using sieve.
> - Factorials up to 100 modulo 1e9+7.
> - This reduces runtime to O(1) for each query

#### 🔍 Algorithm

```pseudo
precompute primes up to 100 using sieve
precompute factorials up to 100 modulo MOD

function optimal(n):
    p = primeCount[n]
    return factorial[p] * factorial[n-p] % MOD

```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
    const int MOD = 1e9+7;
    vector<long long> fact;
    vector<int> primeCount;

public:
    Solution() {
        // Precompute factorials up to 100
        fact.resize(101, 1);
        for (int i = 2; i <= 100; i++) {
            fact[i] = (fact[i-1] * i) % MOD;
        }

        // Precompute prime counts using sieve
        vector<bool> isPrime(101, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i*i <= 100; i++) {
            if (isPrime[i]) {
                for (int j = i*i; j <= 100; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        primeCount.resize(101, 0);
        for (int i = 1; i <= 100; i++) {
            primeCount[i] = primeCount[i-1] + (isPrime[i] ? 1 : 0);
        }
    }

    int solutionOptimal(int n) {
        int p = primeCount[n];
        return (fact[p] * fact[n-p]) % MOD;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                          | Cons                            |
| -------------- | --------------- | ---------------- | ----------------------------- | ------------------------------- |
| 🥉 Brute Force | O(n! \* n)      | O(n)             | Easy to understand            | Not feasible for n > 10         |
| 🥈 Optimized   | O(n√n + n)      | O(1)             | Works efficiently for n ≤ 100 | Slightly repetitive prime check |
| 🥇 Optimal ⭐  | O(1) per query  | O(n) precompute  | Very fast, scalable, clean    | Requires preprocessing          |

## 🎯 Why This is Optimal?

    - Avoids generating permutations → huge performance gain.
    - Uses precomputation of primes and factorials.
    - Clean, scalable, works instantly for any n ≤ 100.

### 🔑 Key Insights

| #   | Insight                                               |
| --- | ----------------------------------------------------- |
| 1   | The core is counting primes ≤ `n`.                    |
| 2   | Prime positions and prime values must match in count. |
| 3   | Factorial precomputation makes queries O(1).          |

### 💭 Common Mistakes to Avoid

| #   | Mistake                             | Description                                               | How to Avoid                            | Example                                         |
| --- | ----------------------------------- | --------------------------------------------------------- | --------------------------------------- | ----------------------------------------------- |
| 1   | Confusing prime indices with values | Index positions (1-based) must be prime, not array values | Always check index, not the value       | Index=2 is prime, value can be any prime number |
| 2   | Forgetting modulo in factorial      | Factorials grow extremely fast                            | Apply `% 1e9+7` at each multiplication  | `(res * i) % MOD`                               |
| 3   | Miscounting primes ≤ n              | Off-by-one when counting                                  | Use sieve or well-tested prime function | For n=10, prime count=4 (2,3,5,7)               |

### 🐛 Implementation Mistakes

| #   | Mistake                          | Description                       | How to Avoid                 | Example                                |
| --- | -------------------------------- | --------------------------------- | ---------------------------- | -------------------------------------- |
| 1   | Using 0-index instead of 1-index | Prime indices are 1-based         | Be explicit in loops (`i+1`) | Checking `isPrime(i)` instead of `i+1` |
| 2   | Integer overflow in factorial    | Even for small n, factorial > int | Use `long long` and modulo   | `20!` exceeds 32-bit int               |
| 3   | Recomputing sieve for each query | Inefficient and redundant         | Precompute primes once       | Sieve up to 100 before queries         |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                 | Description               | How to Avoid                                     | Prevention                         |
| --- | --------------------------------------- | ------------------------- | ------------------------------------------------ | ---------------------------------- |
| 1   | Thinking permutations must be generated | Leads to exponential time | Realize factorial structure of primes/non-primes | Reduce to counting, not generating |
| 2   | Assuming `n` large (like 1e9)           | Might overcomplicate      | Re-read constraints (`n ≤ 100`)                  | Use simple precomputation          |
| 3   | Forgetting non-prime arrangement        | Only counting primes      | Must multiply both `p!` and `(n-p)!`             | Write explicit formula             |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique            | Application                             |
| --- | ------------------------------ | --------------------------------------- |
| 1   | Counting instead of generating | Count valid permutations mathematically |
| 2   | Sieve of Eratosthenes          | Efficient prime counting                |
| 3   | Factorial precomputation       | O(1) query evaluation                   |

### 🔄 Follow-up Questions

| #   | Question                                       | Answer / Approach                                            |
| --- | ---------------------------------------------- | ------------------------------------------------------------ |
| 1   | How would this change if `n` were up to `1e6`? | Still feasible with sieve + factorial precomputation         |
| 2   | What if indices were 0-based?                  | Then prime positions shift; need to redefine prime index set |

---

<div align="center">

**🎯 Problem 1175 Completed!**

_Happy Coding! 🚀_

</div>
