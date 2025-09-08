<div align="center">

# 🧠 [1523. Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201523-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                               |
| **Acceptance Rate** | `50.7%`                                                                                   |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                        |

|

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `08-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `08-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## Description

<!-- description:start -->

<p>Given two non-negative integers <code>low</code> and <code><font face="monospace">high</font></code>. Return the <em>count of odd numbers between </em><code>low</code><em> and </em><code><font face="monospace">high</font></code><em>&nbsp;(inclusive)</em>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input:</strong> low = 3, high = 7

<strong>Output:</strong> 3

<b>Explanation: </b>The odd numbers between 3 and 7 are [3,5,7].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> low = 8, high = 10

<strong>Output:</strong> 1

<b>Explanation: </b>The odd numbers between 8 and 10 are [9].</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>0 &lt;= low &lt;= high &lt;= 10^9</code></li>
</ul>

<!-- description:end -->

## 🔗 Related Problems

| Problem                                                                                                         | Difficulty  | Relationship  |
| --------------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| [Check if Bitwise OR Has Trailing Zeros](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Linear Scan (Brute Force)

#### 📝 Intuition

> The simplest way: iterate from `low` to `high`, check each number if it is odd, and count it.

#### 🔍 Algorithm

```pseudo
function countOdds(low, high):
    count = 0
    for i from low to high:
        if i % 2 == 1:
            count += 1
    return count
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int countOdds(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            if (i % 2 == 1) count++;
        }
        return count;
    }
};
```

### 🥈 Approach 2: Parity Trick (Optimized Solution)

#### 📝 Intuition

> Instead of scanning every number, we can use a formula:
> The count of odd numbers = (high - low) / 2 + 1 if either low or high is odd, otherwise (high - low) / 2.

#### 🔍 Algorithm

```pseudo
function countOdds(low, high):
    count = (high - low) / 2
    if (low % 2 == 1 or high % 2 == 1):
        count += 1
    return count
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    int countOdds(int low, int high) {
        int count = (high - low) / 2;
        if (low % 2 == 1 || high % 2 == 1) count++;
        return count;
    }
};

```

### 🥇 Approach 3: Math Formula (Optimal Solution ⭐)

#### 📝 Intuition

> Use a prefix function: the number of odd numbers from 0 to x is (x + 1) / 2.
> Then result = f(high) - f(low - 1).

#### 🔍 Algorithm

```pseudo
function f(x):
    return (x + 1) / 2

function countOdds(low, high):
    return f(high) - f(low - 1)

```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int countOdds(int low, int high) {
        auto f = [](int x) { return (x + 1) / 2; };
        return f(high) - f(low - 1);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                          | Cons                          |
| -------------- | --------------- | ---------------- | ----------------------------- | ----------------------------- |
| 🥉 Brute Force | O(high - low)   | O(1)             | Easy to implement             | Too slow for large ranges     |
| 🥈 Optimized   | O(1)            | O(1)             | Simple formula                | Slightly less elegant         |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Very clean, scalable, elegant | Requires mathematical insight |

## 🎯 Why This is Optimal?

    - Brute force is infeasible for large ranges (up to 1e9).
    - Optimized formula is already O(1).
    - The prefix-function solution is even cleaner and generalizable.

### 🔑 Key Insights

| #   | Insight                                       |
| --- | --------------------------------------------- |
| 1   | Odd numbers appear every 2 steps.             |
| 2   | Counting odds can be reduced to a formula.    |
| 3   | Prefix sums generalize the formula elegantly. |

### 💭 Common Mistakes to Avoid

| #   | Mistake                   | Description                       | How to Avoid                  | Example         |
| --- | ------------------------- | --------------------------------- | ----------------------------- | --------------- |
| 1   | Using brute force         | Iterating up to 1e9 is too slow   | Use math formula              | low=0, high=1e9 |
| 2   | Off-by-one errors         | Forgetting inclusive range        | Always test with small inputs | low=3, high=7   |
| 3   | Integer division mistakes | Using `/` incorrectly in odd/even | Carefully handle `(x+1)/2`    | low=0, high=0   |

### 🐛 Implementation Mistakes

| #   | Mistake                 | Description                                   | How to Avoid                | Example                   |
| --- | ----------------------- | --------------------------------------------- | --------------------------- | ------------------------- |
| 1   | Using float division    | Can cause wrong results                       | Always use integer division | `(x+1)/2` not `(x+1)/2.0` |
| 2   | Not checking boundaries | low=0 may break `low-1`                       | Handle `low=0` properly     | `f(-1)=0`                 |
| 3   | Wrong condition for odd | Using `i%2!=0` is fine, but bitwise is faster | Use `(i & 1)` if needed     | 7 is odd                  |

### 💭 Logical Thinking Mistakes

| #   | Mistake                 | Description                            | How to Avoid           | Prevention         |
| --- | ----------------------- | -------------------------------------- | ---------------------- | ------------------ |
| 1   | Forgetting inclusive    | Excluding `high` or `low` accidentally | Explicitly test bounds | Use test cases     |
| 2   | Misinterpreting formula | Confusing count of numbers with odds   | Derive step by step    | Write examples     |
| 3   | Overengineering         | Using loops unnecessarily              | Stick to math          | Recognize patterns |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique     | Application            |
| --- | ----------------------- | ---------------------- |
| 1   | Brute force counting    | First naive solution   |
| 2   | Mathematical formula    | Efficient counting     |
| 3   | Prefix sums / functions | Elegant generalization |

### 🔄 Follow-up Questions

| #   | Question                               | Answer / Approach                                    |
| --- | -------------------------------------- | ---------------------------------------------------- |
| 1   | How to count even numbers?             | Use `f(high) - f(low-1)` but adapt formula for evens |
| 2   | How to count odds in multiple queries? | Precompute prefix function and reuse                 |

---

<div align="center">

**🎯 Problem 1523 Completed!**

_Happy Coding! 🚀_

</div>
