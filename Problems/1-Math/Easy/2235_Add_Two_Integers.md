<div align="center">

# 🧠 [2235. Add Two Integers](https://leetcode.com/problems/add-two-integers/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202235-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/add-two-integers/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                         |
| **Acceptance Rate** | `88.0%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/add-two-integers/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

Given two integers <code>num1</code> and <code>num2</code>, return <em>the <strong>sum</strong> of the two integers</em>.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 12, num2 = 5
<strong>Output:</strong> 17
<strong>Explanation:</strong> num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = -10, num2 = 4
<strong>Output:</strong> -6
<strong>Explanation:</strong> num1 + num2 = -6, so -6 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100 &lt;= num1, num2 &lt;= 100</code></li>
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

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Jane Street** ⭐ 76.5%

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

📊 Low Frequency Companies

- **Atlassian** 📊 30.0%

---

## 💡 Solutions

### 🥉 Approach 1: Direct Addition (Brute Force)

#### 📝 Intuition

> Since the task is to return the sum of two integers, directly using the `+` operator is the cleanest and most efficient.

#### 🔍 Algorithm

```pseudo
function add(num1, num2):
    return num1 + num2
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int sum(int num1, int num2) {
        return num1 + num2;
    }
};
```

### 🥇 Approach 3: Bit Manipulation (XOR + AND) (Optimal Solution ⭐)

#### 📝 Intuition

> Addition can be done using only bitwise operations:
> XOR (^) → sum without carry
> AND (&) and shift → carry

#### 🔍 Algorithm

```pseudo
function add(num1, num2):
    while num2 != 0:
        carry = (num1 AND num2) << 1
        num1 = num1 XOR num2
        num2 = carry
    return num1
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    int sum(int num1, int num2) {
        while (num2 != 0) {
            int carry = (num1 & num2) << 1;
            num1 = num1 ^ num2;
            num2 = carry;
        }
        return num1;
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                        | Cons                        |
| ------------- | --------------- | ---------------- | --------------------------- | --------------------------- |
| 🥉 Direct Add | O(1)            | O(1)             | Simplest, optimal           | None                        |
| 🥇 Bitwise ⭐ | O(1)            | O(1)             | Good for learning low-level | More complex than necessary |

---

<div align="center">

**🎯 Problem 2235 Completed!**

_Happy Coding! 🚀_

</div>
