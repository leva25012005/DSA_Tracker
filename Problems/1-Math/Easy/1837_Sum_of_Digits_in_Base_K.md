<div align="center">

# 🧠 [1837. Sum of Digits in Base K](https://leetcode.com/problems/sum-of-digits-in-base-k/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201837-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/sum-of-digits-in-base-k/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                |
| **Acceptance Rate** | `78.2%`                                                                    |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/sum-of-digits-in-base-k/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)         |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code> (in base <code>10</code>) and a base <code>k</code>, return <em>the <strong>sum</strong> of the digits of </em><code>n</code><em> <strong>after</strong> converting </em><code>n</code><em> from base </em><code>10</code><em> to base </em><code>k</code>.</p>

<p>After converting, each digit should be interpreted as a base <code>10</code> number, and the sum should be returned in base <code>10</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 34, k = 6
<strong>Output:</strong> 9
<strong>Explanation: </strong>34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10, k = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>n is already in base 10. 1 + 0 = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 10</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `08-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `08-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code> (in base <code>10</code>) and a base <code>k</code>, return <em>the <strong>sum</strong> of the digits of </em><code>n</code><em> <strong>after</strong> converting </em><code>n</code><em> from base </em><code>10</code><em> to base </em><code>k</code>.</p>

<p>After converting, each digit should be interpreted as a base <code>10</code> number, and the sum should be returned in base <code>10</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 34, k = 6
<strong>Output:</strong> 9
<strong>Explanation: </strong>34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10, k = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>n is already in base 10. 1 + 0 = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 10</code></li>
</ul>

<!-- description:end -->

## 🔗 Related Problems

| Problem                                                                              | Difficulty  | Relationship  |
| ------------------------------------------------------------------------------------ | ----------- | ------------- |
| [ Count Symmetric Integers](https://leetcode.com/problems/count-symmetric-integers/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Modulo Simulation (sBrute Force)

#### 📝 Intuition

> The simplest way: repeatedly divide `n` by `k` and take the remainder (`n % k`). Each remainder is a digit in base `k`. Summing these remainders gives the final result.

#### 🔍 Algorithm

```pseudo
function sumBase(n, k):
    sum = 0
    while n > 0:
        digit = n % k
        sum += digit
        n = n // k
    return sum
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            sum += n % k;
            n /= k;
        }
        return sum;
    }
};
```

### 🥈 Approach 2: String Conversion (Optimized Solution)

#### 📝 Intuition

> Convert n into a string representation in base k. Then iterate over each character, convert it back to an integer, and accumulate.

#### 🔍 Algorithm

```pseudo
function sumBaseString(n, k):
    s = convert_to_base_k_string(n, k)
    sum = 0
    for char in s:
        sum += int(char)
    return sum
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    int sumBase(int n, int k) {
        string baseK = "";
        while (n > 0) {
            baseK += char('0' + (n % k));
            n /= k;
        }
        int sum = 0;
        for (char c : baseK) sum += (c - '0');
        return sum;
    }
};
```

### 🥇 Approach 3: Recursive Solution (Optimal Solution ⭐)

#### 📝 Intuition

> Define the solution recursively:
>
> $$
> \text{sumDigits}(n, k) = (n \bmod k) + \text{sumDigits}\left(\left\lfloor \frac{n}{k} \right\rfloor, k\right)
> $$

#### 🔍 Algorithm

```pseudo
function sumBaseRecursive(n, k):
    if n == 0:
        return 0
    return (n % k) + sumBaseRecursive(n / k, k)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    int sumBase(int n, int k) {
        if (n == 0) return 0;
        return (n % k) + sumBase(n / k, k);
    }
};
```

### 🏆 Approach 4: Using Built-in Conversion (Language Helper)

#### 📝 Intuition

> Some languages provide built-in methods to convert a number to a different base (e.g., Python’s format or int.toString(base)). Use them to simplify implementation.

#### 🔍 Algorithm

```pseudo
function sumBaseBuiltIn(n, k):
    s = built_in_convert(n, k)
    sum = 0
    for char in s:
        sum += int(char)
    return sum
```

#### 💻 Implementation

```cpp
class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            int quotient = n / k;
            int remainder = n - quotient * k;
            sum += remainder;
            n = quotient;
        }
        return sum;
    }
};
```

```py
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        baseK = ""
        while n > 0:
            baseK = str(n % k) + baseK
            n //= k
        return sum(int(d) for d in baseK)
```

### 🔮 Approach 5: Mathematical Formula (Quotient & Remainder)

#### 📝 Intuition

> Same as Brute Force, but explicitly decomposes n using quotient and remainder instead of %. Highlights the math behind base conversion.

#### 🔍 Algorithm

```pseudo
function sumBaseMath(n, k):
    sum = 0
    while n > 0:
        quotient = n // k
        remainder = n - quotient * k
        sum += remainder
        n = quotient
    return sum
```

#### 💻 Implementation

```cpp
class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            int quotient = n / k;
            int remainder = n - quotient * k;
            sum += remainder;
            n = quotient;
        }
        return sum;
    }
};
```

## 📊 Comparison of Approaches

| Approach                      | Time Complexity | Space Complexity | Pros                              | Cons                           |
| ----------------------------- | --------------- | ---------------- | --------------------------------- | ------------------------------ |
| 🥉 Brute Force (Modulo Loop)  | O(logₖ n)       | O(1)             | Simple, efficient, easy to write  | None really                    |
| 🥈 String Conversion          | O(logₖ n)       | O(logₖ n)        | Very intuitive and easy to debug  | Extra memory for string        |
| 🥇 Recursive Solution ⭐      | O(logₖ n)       | O(logₖ n) stack  | Elegant and clean code            | Risk of stack overflow         |
| 🏆 Built-in Conversion Helper | O(logₖ n)       | O(logₖ n)        | Short code, uses library features | Not portable across languages  |
| 🔮 Math Formula               | O(logₖ n)       | O(1)             | Shows math reasoning explicitly   | Same complexity as brute force |

## 🎯 Why This is Optimal?

    - All methods essentially reduce to O(logₖ n) since we must process each digit in base k.
    - Brute Force is already optimal in both time and space.
    - Recursive and String-based are less space-efficient but more elegant/readable.
    - Built-in methods reduce coding effort but don’t improve asymptotics.

### 🔑 Key Insights

| #   | Insight                                                                  |
| --- | ------------------------------------------------------------------------ |
| 1   | Converting a number to base `k` is essentially repeated division by `k`. |
| 2   | Each remainder directly corresponds to a digit in base `k`.              |
| 3   | The problem reduces to summing those digits.                             |
| 4   | Complexity is bound by the number of digits = `O(logₖ n)`.               |

### 💭 Common Mistakes to Avoid

| #   | Mistake                    | Description                                         | How to Avoid                            | Example            |
| --- | -------------------------- | --------------------------------------------------- | --------------------------------------- | ------------------ |
| 1   | Forgetting remainder order | Digits are extracted in reverse order               | Always use `%` then divide by `k`       | Wrong if appending |
| 2   | Mixing char with int       | When using string conversion, `‘3’ - ‘0’` is needed | Convert chars properly before summation | `'3' → 3`          |
| 3   | Off-by-one in loop         | Stopping too early (n > 0 vs n >= 0)                | Carefully handle termination condition  | Extra digit missed |

### 🐛 Implementation Mistakes

| #   | Mistake            | Description                          | How to Avoid             | Example                |
| --- | ------------------ | ------------------------------------ | ------------------------ | ---------------------- |
| 1   | Infinite loop      | Forgetting to update `n`             | Always divide `n` by `k` | `while(n>0)` stuck     |
| 2   | Wrong accumulation | Adding `n` instead of remainder      | Use `(n % k)` only       | sum += n (wrong)       |
| 3   | Stack overflow     | Recursive approach without base case | Add `if n == 0 return 0` | Missing base condition |

### 💭 Logical Thinking Mistakes

| #   | Mistake              | Description                              | How to Avoid                      | Prevention                  |
| --- | -------------------- | ---------------------------------------- | --------------------------------- | --------------------------- |
| 1   | Overcomplicating     | Using heavy math when simple loop works  | Stick to simple `%` and `/` loop  | Don’t over-optimize         |
| 2   | Misinterpreting base | Thinking k=10 means no conversion needed | Still compute digit sum properly  | Example: n=10, k=10 → sum=1 |
| 3   | Ignoring constraints | Assuming `n` is huge                     | Note: n ≤ 100, trivial complexity | Simpler solutions suffice   |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                              |
| --- | ------------------- | ---------------------------------------- |
| 1   | Modulo Arithmetic   | Extract digits in base `k`               |
| 2   | Divide & Conquer    | Recursive digit decomposition            |
| 3   | String Manipulation | Alternative base representation handling |

### 🔄 Follow-up Questions

| #   | Question                                | Answer / Approach                                      |
| --- | --------------------------------------- | ------------------------------------------------------ |
| 1   | What if `n` is extremely large (10^18)? | Use iterative modulo/division to avoid overflow.       |
| 2   | What if `k > 10` (e.g., hexadecimal)?   | Need mapping for digits > 9 (A-F).                     |
| 3   | Can this be solved without division?    | Use bitwise tricks if `k` is power of 2 (2, 4, 8, 16). |

---

<div align="center">

**🎯 Problem 1837 Completed!**

_Happy Coding! 🚀_

</div>
