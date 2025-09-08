<div align="center">

# 🧠 [2894. Divisible and Non-divisible Sums Difference](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202894-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                    |
| **Acceptance Rate** | `91.2%`                                                                                        |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                             |

## Description

<!-- description:start -->

<p>You are given positive integers <code>n</code> and <code>m</code>.</p>

<p>Define two integers as follows:</p>

<ul>
	<li><code>num1</code>: The sum of all integers in the range <code>[1, n]</code> (both <strong>inclusive</strong>) that are <strong>not divisible</strong> by <code>m</code>.</li>
	<li><code>num2</code>: The sum of all integers in the range <code>[1, n]</code> (both <strong>inclusive</strong>) that are <strong>divisible</strong> by <code>m</code>.</li>
</ul>

<p>Return <em>the integer</em> <code>num1 - num2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10, m = 3
<strong>Output:</strong> 19
<strong>Explanation:</strong> In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, m = 6
<strong>Output:</strong> 15
<strong>Explanation:</strong> In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 5, m = 1
<strong>Output:</strong> -15
<strong>Explanation:</strong> In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `08-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `08-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> Simply iterate through all numbers from 1 to n and sum them based on whether they are divisible by m or not.

#### 🔍 Algorithm

```pseudo
function differenceOfSums(n, m):
    num1 = 0
    num2 = 0
    for i from 1 to n:
        if i % m == 0:
            num2 += i
        else:
            num1 += i
    return num1 - num2
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int differenceOfSums(int n, int m) {
        int num1 = 0, num2 = 0;
        for (int i = 1; i <= n; i++) {
            if (i % m == 0) num2 += i;
            else num1 += i;
        }
        return num1 - num2;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Use the formula for sum of first n integers and sum of multiples of m to compute num1 and num2 in O(1) time.

#### 🔍 Algorithm

```pseudo
function differenceOfSums(n, m):
    total_sum = n * (n + 1) / 2
    k = n / m  // number of multiples of m
    sum_multiples = m * k * (k + 1) / 2
    num2 = sum_multiples
    num1 = total_sum - num2
    return num1 - num2
```

#### 💻 Implementation

```cpp
// Optimized mathematical approach

class Solution {
public:
    int differenceOfSums(int n, int m) {
        int total = n * (n + 1) / 2;
        int k = n / m;
        int num2 = m * k * (k + 1) / 2;
        int num1 = total - num2;
        return num1 - num2;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Precompute prefix sums up to n to handle multiple queries efficiently.

#### 🔍 Algorithm

```pseudo
function differenceOfSums(n, m):
    prefix[0] = 0
    for i from 1 to n:
        prefix[i] = prefix[i-1] + i
    num2 = sum of prefix[i] where i % m == 0
    num1 = prefix[n] - num2
    return num1 - num2
```

#### 💻 Implementation

```cpp
// Prefix sum approach

class Solution {
public:
    int differenceOfSums(int n, int m) {
        vector<int> prefix(n + 1, 0);
        for (int i = 1; i <= n; i++) prefix[i] = prefix[i-1] + i;

        int num2 = 0;
        for (int i = m; i <= n; i += m) num2 += i;

        int num1 = prefix[n] - num2;
        return num1 - num2;
    }
};
```

## 📊 Comparison of Approaches

| Approach         | Time Complexity    | Space Complexity | Pros                        | Cons                                  |
| ---------------- | ------------------ | ---------------- | --------------------------- | ------------------------------------- |
| 🥉 Brute Force   | O(n)               | O(1)             | Simple and straightforward  | Slower for large n                    |
| 🥈 Optimized     | O(1)               | O(1)             | Fast and elegant            | Requires mathematical formula         |
| 🥇 Prefix Sum ⭐ | O(n) preprocessing | O(n)             | Useful for multiple queries | Extra memory, slower for single query |

## 🎯 Why This is Optimal?

    - The mathematical approach computes the answer in O(1) time and constant space, making it the most efficient solution.
    - Brute force is easy to implement but inefficient for large n.
    - Prefix sum approach is only beneficial if there are multiple queries for different m values.

### 🔑 Key Insights

| #   | Insight                                                      |
| --- | ------------------------------------------------------------ |
| 1   | Sum of first n integers = n\*(n+1)/2                         |
| 2   | Sum of multiples of m = m\*(k\*(k+1)/2), k = n/m             |
| 3   | num1 = total sum - sum of multiples; num2 = sum of multiples |

### 💭 Common Mistakes to Avoid

| #   | Mistake                   | Description                                 | How to Avoid         | Example  |
| --- | ------------------------- | ------------------------------------------- | -------------------- | -------- |
| 1   | Off-by-one error          | Forgetting to include n in the range        | Use <= n in loop     | n=10     |
| 2   | Division rounding mistake | Not using integer division for multiples    | Floor division (n/m) | n=10,m=3 |
| 3   | Miscalculating total sum  | Using wrong formula for sum of first n nums | Use n\*(n+1)/2       | n=5      |

### 🐛 Implementation Mistakes

| #   | Mistake                | Description                  | How to Avoid      | Example |
| --- | ---------------------- | ---------------------------- | ----------------- | ------- |
| 1   | Index errors           | Accessing prefix array wrong | Always size n+1   | i=0     |
| 2   | Forgetting m multiples | Skip first multiple          | Start loop from m | i=m     |

### 💭 Logical Thinking Mistakes

| #   | Mistake                      | Description                          | How to Avoid   | Prevention |
| --- | ---------------------------- | ------------------------------------ | -------------- | ---------- |
| 1   | Misunderstanding problem     | Confusing divisible vs non-divisible | Read carefully | Example    |
| 2   | Forgetting subtraction order | Return num1 - num2 not num2 - num1   | Check formula  | Example    |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique  | Application                          |
| --- | -------------------- | ------------------------------------ |
| 1   | Mathematical formula | Sum of integers, sum of multiples    |
| 2   | Prefix sum           | Precompute sums for multiple queries |
| 3   | Brute force          | Iterate and check divisibility       |

### 🔄 Follow-up Questions

| #   | Question                               | Answer / Approach                      |
| --- | -------------------------------------- | -------------------------------------- |
| 1   | How to handle multiple queries quickly | Use prefix sum or mathematical formula |
| 2   | What if n is very large                | Only mathematical approach feasible    |

---

<div align="center">

**🎯 Problem 2894 Completed!**

_Happy Coding! 🚀_

</div>
