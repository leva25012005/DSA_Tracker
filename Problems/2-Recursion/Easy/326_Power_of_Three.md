<div align="center">

# 🧠 [326. Power of Three](https://leetcode.com/problems/power-of-three/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20326-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/power-of-three/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                                                                     |
| **Acceptance Rate** | `50.0%`                                                                                                                                         |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/power-of-three/)                                                                               |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) ![Recursion](https://img.shields.io/badge/-Recursion-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of three. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of three, if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 27
<strong>Output:</strong> true
<strong>Explanation:</strong> 27 = 3<sup>3</sup>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = (-1).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `09-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `09-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                   | Difficulty    | Relationship    |
| ------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Power of Two](https://leetcode.com/problems/power-of-two/)                                                               | 🟢 **Easy**   | Similar logic   |
| [Power of Four](https://leetcode.com/problems/power-of-four/)                                                             | 🟢 **Easy**   | Related concept |
| [Check if Number is a Sum of Powers of Three](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/) | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

- **Goldman Sachs** 📈 48.6%

---

## 💡 Solutions

### 🥉 Approach 1: Iterative Division (Brute Force)

#### 📝 Intuition

> If n is a power of 3, we can keep dividing it by 3 until we get 1. If at any point it’s not divisible by 3, then it’s not a power of 3.

#### 🔍 Algorithm

```pseudo
function isPowerOfThree(n):
    if n <= 0: return false
    while n % 3 == 0:
        n = n / 3
    return n == 1
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) return false;
        while (n % 3 == 0) {
            n /= 3;
        }
        return n == 1;
    }
};
```

### 🥈 Approach 2: Recursive Division (Optimized Solution)

#### 📝 Intuition

> Replace iteration with recursion:
> If n == 1 → return true
> If n <= 0 or n % 3 != 0 → return false
> Otherwise, recurse on n / 3.

#### 🔍 Algorithm

```pseudo
function isPowerOfThree(n):
    if n == 1: return true
    if n <= 0 or n % 3 != 0: return false
    return isPowerOfThree(n / 3)
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 1) return true;
        if (n <= 0 || n % 3 != 0) return false;
        return isPowerOfThree(n / 3);
    }
};
```

### 🥇 Approach 3: Logarithm (Optimal Solution ⭐)

#### 📝 Intuition

> Using math:
> If n is a power of 3, then log₃(n) should be an integer.
> We can check using log(n)/log(3)

#### 🔍 Algorithm

```pseudo
function isPowerOfThree(n):
    if n <= 0: return false
    x = log(n) / log(3)
    return abs(x - round(x)) < epsilon
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
#include <cmath>

class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) return false;
        double x = log10(n) / log10(3);
        return fabs(x - round(x)) < 1e-10;
    }
};
```

### ⭐ Approach 4: Max Power of 3 (Optimal)

#### 📝 Intuition

> The largest power of 3 within 32-bit signed integer range is 3^19 = 1162261467.
> If n is a power of 3, it must divide this number evenly.
> Check: 1162261467 % n == 0.

#### 🔍 Algorithm

```pseudo
function isPowerOfThree(n):
    return n > 0 and (1162261467 % n == 0)
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach     | Time Complexity | Space Complexity | Pros                                | Cons                                      |
| ------------ | --------------- | ---------------- | ----------------------------------- | ----------------------------------------- |
| 🥉 Iterative | O(log₃(n))      | O(1)             | Simple, easy to understand          | Has a loop                                |
| 🥈 Recursive | O(log₃(n))      | O(log₃(n))       | Clean recursive code                | Extra stack usage                         |
| 🥇 Logarithm | O(1)            | O(1)             | Short, constant time                | Floating-point precision issues           |
| ⭐ Max Power | O(1)            | O(1)             | Extremely fast, no precision issues | Hardcoded max value, depends on data type |

## 🎯 Why This is Optimal?

- Compared to brute force & recursion → avoids loops and recursion stack.
- Compared to logarithm → avoids floating-point precision errors.
- Max power approach is constant time, constant space, exact → the most elegant and scalable.

### 🔑 Key Insights

| #   | Insight                                                                              |
| --- | ------------------------------------------------------------------------------------ |
| 1   | Dividing repeatedly by 3 is the most intuitive check                                 |
| 2   | Logs can confirm powers but are prone to precision errors                            |
| 3   | Using the largest power of 3 in range is both optimal and exact                      |
| 4   | Recursion and iteration have the same complexity, but recursion adds memory overhead |

### 💭 Common Mistakes to Avoid

| #   | Mistake                         | Description                                  | How to Avoid              | Example                                |
| --- | ------------------------------- | -------------------------------------------- | ------------------------- | -------------------------------------- |
| 1   | Forgetting `n <= 0` check       | Negative numbers and 0 are never powers of 3 | Always check at the start | `isPowerOfThree(-3)`                   |
| 2   | Precision error with logs       | Floating-point math can misclassify numbers  | Use epsilon tolerance     | `log(243)/log(3)` may not be exactly 5 |
| 3   | Overflow when using `pow(3, x)` | Can exceed 32-bit integer range              | Use predefined max power  | `pow(3,20)` overflows in 32-bit        |

### 🐛 Implementation Mistakes

| #   | Mistake                    | Description                | How to Avoid                    | Example                      |
| --- | -------------------------- | -------------------------- | ------------------------------- | ---------------------------- |
| 1   | Using `pow(3, x)` in loop  | Risk of overflow           | Avoid computing powers directly | `while(pow(3, i) < n)`       |
| 2   | Comparing floats with `==` | Floating-point issues      | Use tolerance                   | `fabs(x - round(x)) < 1e-10` |
| 3   | Missing return cases       | Forgetting base conditions | Ensure full coverage            | `if (n <= 0) return false;`  |

### 💭 Logical Thinking Mistakes

| #   | Mistake                              | Description                     | How to Avoid                  | Prevention                 |
| --- | ------------------------------------ | ------------------------------- | ----------------------------- | -------------------------- |
| 1   | Thinking 0 is a power of 3           | Multiplying 0 always gives 0    | Definition excludes 0         | Always check `n > 0`       |
| 2   | Confusing `3^n` with `n^3`           | Misunderstanding exponentiation | Remember correct formula      | Write condition `n == 3^x` |
| 3   | Assuming recursion is more efficient | Recursion adds overhead         | Analyze time/space trade-offs | Evaluate complexity first  |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique   | Application                                 |
| --- | --------------------- | ------------------------------------------- |
| 1   | Iterative Division    | Checking divisibility repeatedly            |
| 2   | Recursion             | Cleaner representation of repeated division |
| 3   | Logarithm             | Direct mathematical validation              |
| 4   | Modulo with Max Power | Optimal divisibility check                  |

### 🔄 Follow-up Questions

| #   | Question                                            | Answer / Approach                               |
| --- | --------------------------------------------------- | ----------------------------------------------- |
| 1   | How to generalize for any base `k`?                 | Replace `3` with `k` in all approaches          |
| 2   | What about 64-bit integers?                         | Use the largest power of `3` within `long long` |
| 3   | Can we avoid loops, recursion, and logs completely? | Yes, with the **Max Power divisibility check**  |

---

<div align="center">

**🎯 Problem 326 Completed!**

_Happy Coding! 🚀_

</div>
