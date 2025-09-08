<div align="center">

# 🧠 [3622. Check Divisibility by Digit Sum and Product](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203622-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                    |
| **Acceptance Rate** | `64.1%`                                                                                        |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                             |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>n</code>. Determine whether <code>n</code> is divisible by the <strong>sum</strong> of the following two values:</p>

<ul>
    <li>The <strong>digit sum</strong> of <code>n</code> (the sum of its digits).</li>
    <li>The <strong>digit product</strong> of <code>n</code> (the product of its digits).</li>
</ul>

<p>Return <code>true</code> if <code>n</code> is divisible by this sum; otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 99
<strong>Output:</strong> true
<strong>Explanation:</strong> Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 23
<strong>Output:</strong> false
<strong>Explanation:</strong> Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
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

> Convert the number to a string, compute sum and product of digits by iterating through all digits, then check divisibility.

#### 🔍 Algorithm

```pseudo
function isDivisibleByDigitSumProduct(x):
    convert n to string
    digit_sum = 0
    digit_product = 1
    for each digit in string:
        digit_sum += digit
        digit_product *= digit
    return n % (digit_sum + digit_product) == 0
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    bool isDivisibleByDigitSumProduct(int n) {
        string s = to_string(n);
        int sum = 0, prod = 1;
        for (char c : s) {
            int d = c - '0';
            sum += d;
            prod *= d;
        }
        return n % (sum + prod) == 0;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Avoid converting to string. Use modulo and integer division to extract digits and compute sum/product in a single pass

#### 🔍 Algorithm

```pseudo
function isDivisibleByDigitSumProduct(x):
    digit_sum = 0
    digit_product = 1
    temp = n
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_product *= digit
        temp = temp / 10
    return n % (digit_sum + digit_product) == 0
```

#### 💻 Implementation

```cpp
// Optimized approach without string conversion

class Solution {
public:
    bool isDivisibleByDigitSumProduct(int n) {
        int sum = 0, prod = 1, temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            sum += digit;
            prod *= digit;
            temp /= 10;
        }
        return n % (sum + prod) == 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Combine the operations into a one-liner loop using minimal variables; no extra storage, linear time in number of digits (O(log n)).

#### 🔍 Algorithm

```pseudo
function isDivisibleByDigitSumProduct(x):
    initialize sum = 0, product = 1
    for each digit in n extracted by modulo:
        sum += digit
        product *= digit
    return n % (sum + product) == 0
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    bool isDivisibleByDigitSumProduct(int n) {
        int sum = 0, prod = 1;
        for (int temp = n; temp > 0; temp /= 10) {
            int d = temp % 10;
            sum += d;
            prod *= d;
        }
        return n % (sum + prod) == 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros | Cons |
| -------------- | --------------- | ---------------- | ---- | ---- |
| 🥉 Brute Force | O(?)            | O(?)             | ...  | ...  |
| 🥈 Optimized   | O(?)            | O(?)             | ...  | ...  |
| 🥇 Optimal ⭐  | O(?)            | O(?)             | ...  | ...  |
| ...            | ....            | ...              | ...  | ...  |

## 🎯 Why This is Optimal?

    - The optimal solution avoids extra memory for string conversion.
    - All approaches have linear time complexity relative to the number of digits (O(log n)), but the optimal one minimizes space and operations.
    - Clean, readable, and scalable even for large n up to 10^6.

### 🔑 Key Insights

| #   | Insight                                                                     |
| --- | --------------------------------------------------------------------------- |
| 1   | Sum and product of digits can be computed in one pass using modulo/division |
| 2   | String conversion is convenient but uses extra space                        |
| 3   | Minimal variables and one loop yield optimal performance                    |
| ... | Further optimization is unnecessary for given constraints                   |

### 💭 Common Mistakes to Avoid

| #   | Mistake                                  | Description                      | How to Avoid                  | Example                                     |
| --- | ---------------------------------------- | -------------------------------- | ----------------------------- | ------------------------------------------- |
| 1   | Forgetting to multiply product correctly | Initial product must be 1, not 0 | Initialize `product = 1`      | n = 23 → 2\*3 = 6                           |
| 2   | Using string conversion unnecessarily    | Increases space usage            | Use integer division/modulo   | n = 99 → convert to string, unnecessary     |
| 3   | Dividing by zero accidentally            | If sum + product = 0             | Ensure correct initialization | n = 0 (outside constraints, but be careful) |

### 🐛 Implementation Mistakes

| #   | Mistake                                  | Description                      | How to Avoid                  | Example                                     |
| --- | ---------------------------------------- | -------------------------------- | ----------------------------- | ------------------------------------------- |
| 1   | Forgetting to multiply product correctly | Initial product must be 1, not 0 | Initialize `product = 1`      | n = 23 → 2\*3 = 6                           |
| 2   | Using string conversion unnecessarily    | Increases space usage            | Use integer division/modulo   | n = 99 → convert to string, unnecessary     |
| 3   | Dividing by zero accidentally            | If sum + product = 0             | Ensure correct initialization | n = 0 (outside constraints, but be careful) |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                     | Description                           | How to Avoid                  | Prevention            |
| --- | ------------------------------------------- | ------------------------------------- | ----------------------------- | --------------------- |
| 1   | Forgetting product for single-digit numbers | Product must be 1 initially           | Initialize properly           | n = 5 → sum=5, prod=5 |
| 2   | Misinterpreting divisibility                | Confusing sum or product individually | Sum + product must be checked | n = 23 → sum+prod=11  |
| 3   | Off-by-one in loops                         | Incorrect digit extraction            | Verify loop conditions        | temp /= 10            |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique  | Application                          |
| --- | -------------------- | ------------------------------------ |
| 1   | Digit manipulation   | Extract digits using modulo/division |
| 2   | Arithmetic checks    | Check divisibility by sum+product    |
| 3   | One-pass computation | Compute sum and product in same loop |

### 🔄 Follow-up Questions

| #   | Question                                | Answer / Approach                               |
| --- | --------------------------------------- | ----------------------------------------------- |
| 1   | Can this work for larger numbers?       | Yes, works up to n ≤ 10^6 efficiently           |
| 2   | What if product exceeds int range?      | Use long long for product to avoid overflow     |
| 3   | Can we handle numbers with zero digits? | Yes, product multiplication handles 0 correctly |

---

<div align="center">

**🎯 Problem 3622 Completed!**

_Happy Coding! 🚀_

</div>
