<div align="center">

# 🧠 [2652. Sum Multiples](https://leetcode.com/problems/sum-multiples/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202652-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/sum-multiples/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `85.5%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/sum-multiples/)   |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, find the sum of all integers in the range <code>[1, n]</code> <strong>inclusive</strong> that are divisible by <code>3</code>, <code>5</code>, or <code>7</code>.</p>

<p>Return <em>an integer denoting the sum of all numbers in the given range satisfying&nbsp;the constraint.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 21
<strong>Explanation:</strong> Numbers in the range <code>[1, 7]</code> that are divisible by <code>3</code>, <code>5,</code> or <code>7 </code>are <code>3, 5, 6, 7</code>. The sum of these numbers is <code>21</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 40
<strong>Explanation:</strong> Numbers in the range <code>[1, 10] that are</code> divisible by <code>3</code>, <code>5,</code> or <code>7</code> are <code>3, 5, 6, 7, 9, 10</code>. The sum of these numbers is 40.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> 30
<strong>Explanation:</strong> Numbers in the range <code>[1, 9]</code> that are divisible by <code>3</code>, <code>5</code>, or <code>7</code> are <code>3, 5, 6, 7, 9</code>. The sum of these numbers is <code>30</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>3</sup></code></li>
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

> The simplest idea is to iterate through all numbers from `1 → n`, and if a number is divisible by `3`, `5`, or `7`, add it to the sum.

#### 🔍 Algorithm

```pseudo
function sumOfMultiples(n):
    sum = 0
    for i from 1 to n:
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            sum += i
    return sum
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int sumOfMultiples(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution wiht Boolean Array

#### 📝 Intuition

> Instead of checking each number, we can directly add the multiples of 3, 5, 7 into a set or boolean array to avoid duplicates, then sum them up.

#### 🔍 Algorithm

```pseudo
function sumOfMultiples(n):
    mark = boolean array size n+1
    sum = 0
    for divisor in [3, 5, 7]:
        for i = divisor to n step divisor:
            if not mark[i]:
                sum += i
                mark[i] = true
    return sum
```

#### 💻 Implementation

```cpp
// Optimized approach with boolean array
class Solution {
public:
    int sumOfMultiples(int n) {
        vector<bool> seen(n + 1, false);
        int sum = 0;
        for (int d : {3, 5, 7}) {
            for (int i = d; i <= n; i += d) {
                if (!seen[i]) {
                    sum += i;
                    seen[i] = true;
                }
            }
        }
        return sum;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Math - Inclusion Exclusion)

#### 📝 Intuition

> Use the arithmetic progression sum formula:
>
> $$
> S(d) = d \times k \times \frac{k+1}{2}, \quad k = \left\lfloor \frac{n}{d}  \right\rfloor
> $$
>
> Apply Inclusion-Exclusion Principle:
>
> $$
> \text{Result} = S(3) + S(5) + S(7) - S(15) - S(21) - S(35) + S(105)
> $$

#### 🔍 Algorithm

```pseudo
function sumDivisibleBy(d, n):
    k = n // d
    return d * k * (k + 1) / 2

function sumOfMultiples(n):
    return sumDivisibleBy(3,n) + sumDivisibleBy(5,n) + sumDivisibleBy(7,n)
           - sumDivisibleBy(15,n) - sumDivisibleBy(21,n) - sumDivisibleBy(35,n)
           + sumDivisibleBy(105,n)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution using math
class Solution {
public:
    long long sumDivisibleBy(int d, int n) {
        long long k = n / d;
        return 1LL * d * k * (k + 1) / 2;
    }

    int sumOfMultiples(int n) {
        return sumDivisibleBy(3, n) + sumDivisibleBy(5, n) + sumDivisibleBy(7, n)
             - sumDivisibleBy(15, n) - sumDivisibleBy(21, n) - sumDivisibleBy(35, n)
             + sumDivisibleBy(105, n);
    }
};
```

### 🆕 Approach 4: Prefix Sum Array

#### 📝 Intuition

> We can build a prefix sum array prefix[i] = sum of all numbers divisible by 3, 5, 7 in [1..i].
> Return prefix[n]. Useful when there are multiple queries.

#### 🔍 Algorithm

```pseudo
function sumOfMultiples(n):
    prefix = array of size n+1
    prefix[0] = 0
    for i from 1 to n:
        prefix[i] = prefix[i-1]
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            prefix[i] += i
    return prefix[n]
```

#### 💻 Implementation

```cpp
// Prefix sum array approach
class Solution {
public:
    int sumOfMultiples(int n) {
        vector<int> prefix(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1];
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                prefix[i] += i;
            }
        }
        return prefix[n];
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                              | Cons                               |
| -------------- | --------------- | ---------------- | --------------------------------- | ---------------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Very simple and easy to implement | Slow for large n                   |
| 🥈 Optimized   | O(n)            | O(n)             | Avoids double counting            | Uses extra memory                  |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fastest, clean math solution      | Requires understanding of formulas |
| 🆕 Prefix Sum  | O(n)            | O(n)             | Useful for multiple queries       | Higher memory cost                 |

## 🎯 Why This is Optimal?

    - Compared to brute force: reduces from O(n) to O(1).
    - Compared to boolean array: no extra memory usage.
    - Inclusion-Exclusion is the cleanest and most scalable solution.t

### 🔑 Key Insights

| #   | Insight                                           |
| --- | ------------------------------------------------- |
| 1   | Arithmetic progression helps compute sums quickly |
| 2   | Inclusion-Exclusion avoids double counting        |
| 3   | Prefix sum is useful for multiple queries         |

### 💭 Common Mistakes to Avoid

| #   | Mistake             | Description              | How to Avoid              | Example                          |
| --- | ------------------- | ------------------------ | ------------------------- | -------------------------------- |
| 1   | Forgetting overlaps | Leads to double counting | Apply Inclusion-Exclusion | e.g. counting 15 in both 3 and 5 |
| 2   | Using `int` only    | Can overflow             | Use `long long`           | Large sums with n=1000           |
| 3   | Wrong prefix index  | Off-by-one errors        | Update carefully          | `prefix[i] = prefix[i-1] + val`  |

### 🐛 Implementation Mistakes

| #   | Mistake                 | Description              | How to Avoid            | Example        |
| --- | ----------------------- | ------------------------ | ----------------------- | -------------- |
| 1   | Integer overflow        | Sum too large            | Use `long long`         | sumDivisibleBy |
| 2   | Forgetting to reset sum | Accumulates wrong values | Always reinitialize sum | sum = 0        |
| 3   | Wrong loop step         | Inefficient loops        | Increment by divisor    | for (i += d)   |

### 💭 Logical Thinking Mistakes

| #   | Mistake                           | Description               | How to Avoid     | Prevention         |
| --- | --------------------------------- | ------------------------- | ---------------- | ------------------ |
| 1   | Assuming full iteration is needed | Ignores math optimization | Use formula      | Understand AP sum  |
| 2   | Forgetting 24h format edge cases  | Incorrect results         | Always apply `%` | Check sample cases |
| 3   | Ignoring multiple queries         | Suboptimal approach       | Use prefix sums  | Add Approach 4     |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique   | Application                   |
| --- | --------------------- | ----------------------------- |
| 1   | Brute Force Iteration | Check each number             |
| 2   | Boolean Array / Set   | Avoid duplicates              |
| 3   | Inclusion-Exclusion   | Fast mathematical computation |
| 4   | Prefix Sum Array      | Handle multiple queries       |

### 🔄 Follow-up Questions

| #   | Question                                             | Answer / Approach                     |
| --- | ---------------------------------------------------- | ------------------------------------- |
| 1   | What if there are multiple queries with different n? | Use Prefix Sum to answer each in O(1) |
| 2   | What if more divisors are added (e.g., 3,5,7,11)?    | Generalize Inclusion-Exclusion        |
| 3   | What if n is very large (10^12)?                     | Only use formula O(1), no iteration   |

---

<div align="center">

**🎯 Problem 2652 Completed!**

_Happy Coding! 🚀_

</div>
