<div align="center">

# 🧠 [3099. Harshad Number](https://leetcode.com/problems/harshad-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203099-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/harshad-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `83.3%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/harshad-number/)  |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>An integer divisible by the <strong>sum</strong> of its digits is said to be a <strong>Harshad</strong> number. You are given an integer <code>x</code>. Return <em>the sum of the digits</em> of <code>x</code> if <code>x</code> is a <strong>Harshad</strong> number, otherwise, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 18
<strong>Output:</strong> 9
<strong>Explanation:</strong> The sum of digits of <code>x</code> is <code>9</code>. <code>18</code> is divisible by <code>9</code>. So <code>18</code> is a Harshad number and the answer is <code>9</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 23
<strong>Output:</strong> -1
<strong>Explanation:</strong> The sum of digits of <code>x</code> is <code>5</code>. <code>23</code> is not divisible by <code>5</code>. So <code>23</code> is not a Harshad number and the answer is <code>-1</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= x &lt;= 100</code></li>
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

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> Sum the digits of x and check if x is divisible by this sum. Return the sum if divisible, otherwise -1.

#### 🔍 Algorithm

```pseudo
function harshadNumber(x):
    sum_digits = sum of all digits of x
    if x % sum_digits == 0:
        return sum_digits
    else:
        return -1
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int harshadNumber(int x) {
        int sum_digits = 0, temp = x;
        while (temp > 0) {
            sum_digits += temp % 10;
            temp /= 10;
        }
        return (x % sum_digits == 0) ? sum_digits : -1;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Convert x to a string to sum digits using a more concise approach, avoiding manual division and modulo.

#### 🔍 Algorithm

```pseudo
function harshadNumber(x):
    sum_digits = sum(int(digit) for digit in str(x))
    if x % sum_digits == 0:
        return sum_digits
    else:
        return -1
```

#### 💻 Implementation

```cpp
// Optimized approach using string conversion

class Solution {
public:
    int harshadNumber(int x) {
        string s = to_string(x);
        int sum_digits = 0;
        for (char c : s) sum_digits += c - '0';
        return (x % sum_digits == 0) ? sum_digits : -1;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Use modern C++ techniques like accumulate for a clean and concise implementatio

#### 🔍 Algorithm

```pseudo
function harshadNumber(x):
    sum_digits = sum of digits using functional programming style
    if x % sum_digits == 0:
        return sum_digits
    else:
        return -1
```

#### 💻 Implementation

```cpp
// Elegant approach using accumulate

#include <numeric>

class Solution {
public:
    int harshadNumber(int x) {
        string s = to_string(x);
        int sum_digits = accumulate(s.begin(), s.end(), 0, [](int acc, char c){ return acc + (c - '0'); });
        return (x % sum_digits == 0) ? sum_digits : -1;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                       | Cons                   |
| -------------- | --------------- | ---------------- | -------------------------- | ---------------------- |
| 🥉 Brute Force | O(log x)        | O(1)             | Simple, easy to understand | Slightly verbose       |
| 🥈 String Conv | O(log x)        | O(log x)         | Cleaner than manual loop   | Extra space for string |
| 🥇 Elegant ⭐  | O(log x)        | O(log x)         | Very concise, functional   | Requires C++11+        |

## 🎯 Why This is Optimal?

    - All approaches run in O(log x) because the number of digits in x is proportional to log10(x).
    - The Elegant approach is the cleanest, scalable, and leverages modern C++ features.

### 🔑 Key Insights

| #   | Insight                                             |
| --- | --------------------------------------------------- |
| 1   | Sum of digits determines Harshad property           |
| 2   | Harshad check: x % sum_digits == 0                  |
| 3   | Functional programming can simplify digit summation |

### 💭 Common Mistakes to Avoid

| #   | Mistake                  | Description          | How to Avoid            | Example |
| --- | ------------------------ | -------------------- | ----------------------- | ------- |
| 1   | Forgetting to sum digits | Only check one digit | Always compute full sum | x = 18  |
| 2   | Division by zero         | If sum_digits is 0   | Handle x >=1            | N/A     |
| 3   | Off-by-one error         | Miscount digits      | Iterate all digits      | x = 23  |

### 🐛 Implementation Mistakes

| #   | Mistake            | Description                    | How to Avoid             | Example |
| --- | ------------------ | ------------------------------ | ------------------------ | ------- |
| 1   | Modulo wrong       | Using x % digit instead of sum | Use sum_digits correctly | x=18    |
| 2   | Integer truncation | Wrong sum due to type          | Use int for sum          | N/A     |

### 💭 Logical Thinking Mistakes

| #   | Mistake                  | Description                          | How to Avoid                | Prevention     |
| --- | ------------------------ | ------------------------------------ | --------------------------- | -------------- |
| 1   | Misunderstanding Harshad | Confusing divisible by sum vs digits | Follow definition carefully | Check examples |
| 2   | Return wrong value       | Return x instead of sum or -1        | Always check conditional    | x = 23         |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application               |
| --- | ------------------- | ------------------------- |
| 1   | Digit manipulation  | Sum digits of an integer  |
| 2   | Modular arithmetic  | Check divisibility by sum |
| 3   | Functional style    | `accumulate` with lambda  |

### 🔄 Follow-up Questions

| #   | Question                            | Answer / Approach                  |
| --- | ----------------------------------- | ---------------------------------- |
| 1   | How to extend for multiple queries? | Precompute sum of digits for range |
| 2   | What if x is very large?            | Use efficient digit sum techniques |

---

<div align="center">

**🎯 Problem 3099 Completed!**

_Happy Coding! 🚀_

</div>
