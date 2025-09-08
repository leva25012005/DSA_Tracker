<div align="center">

# 🧠 [1317. Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201317-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                           |
| **Acceptance Rate** | `54.3%`                                                                                               |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                    |

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

<p><strong>No-Zero integer</strong> is a positive integer that <strong>does not contain any <code>0</code></strong> in its decimal representation.</p>

<p>Given an integer <code>n</code>, return <em>a list of two integers</em> <code>[a, b]</code> <em>where</em>:</p>

<ul>
	<li><code>a</code> and <code>b</code> are <strong>No-Zero integers</strong>.</li>
	<li><code>a + b = n</code></li>
</ul>

<p>The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [1,1]
<strong>Explanation:</strong> Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> [2,9]
<strong>Explanation:</strong> Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Hudson River Trading** 🔥 97.8%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Linear Scan (Brute Force)

#### 📝 Intuition

> Try every possible split a + b = n. For each a check if both a and b are No-Zero Integers. Return the first valid pair.

#### 🔍 Algorithm

```pseudo
function isNoZero(x):
    while x > 0:
        if last digit == 0: return false
        x = x // 10
    return true

function getNoZeroIntegers(n):
for a in [1..n-1]:
    b = n - a
    if isNoZero(a) and isNoZero(b):
        return [a, b]
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        for (int a = 1; a < n; a++) {
            int b = n - a;
            if (isNoZero(a) && isNoZero(b)) return {a, b};
        }
        return {};
    }
};
```

### 🥈 Approach 2: Greedy Adjustment (Optimized Solution)

#### 📝 Intuition

> Start with a simple guess (a = 1, b = n-1). If b contains zero, increment a until both numbers are valid.

#### 🔍 Algorithm

```pseudo
function getNoZeroIntegers(n):
    a = 1
    b = n - a
    while not (isNoZero(a) and isNoZero(b)):
        a += 1
        b = n - a
    return [a, b]
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        int a = 1, b = n - 1;
        while (!isNoZero(a) || !isNoZero(b)) {
            a++;
            b = n - a;
        }
        return {a, b};
    }
};
```

### ⚡ Approach 4: Randomized

#### 📝 Intuition

> CRandomly pick a in [1..n-1], compute b = n-a, and check validity. Works fast for constraints.

#### 🔍 Algorithm

```pseudo
function getNoZeroIntegers(n):
    repeat until found:
    a = random(1..n-1)
    b = n - a
    if isNoZero(a) and isNoZero(b):
        return [a, b]
```

#### 💻 Implementation

```cpp
#include <cstdlib>
#include <ctime>

class Solution {
public:
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        srand(time(0));
        while (true) {
            int a = rand() % (n - 1) + 1;
            int b = n - a;
            if (isNoZero(a) && isNoZero(b)) return {a, b};
        }
    }
};
```

### 📦 Approach 5: Precomputation Table

#### 📝 Intuition

> Precompute answers for all n in [2..10000] once. Answer in O(1).

#### 🔍 Algorithm

```pseudo
function getNoZeroIntegers(n):
    table = {}
    for each n in [2..10000]:
        find first valid (a, b)
        store in table[n]
    return table[input]

```

#### 💻 Implementation

```cpp
class Solution {
    vector<vector<int>> table;
public:
    Solution() {
        table.resize(10001);
        for (int n = 2; n <= 10000; n++) {
            for (int a = 1; a < n; a++) {
                int b = n - a;
                if (isNoZero(a) && isNoZero(b)) {
                    table[n] = {a, b};
                    break;
                }
            }
        }
    }

    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        return table[n];
    }
};
```

## 📊 Comparison of Approaches

| Approach                 | Time Complexity | Space Complexity | Pros                         | Cons                       |
| ------------------------ | --------------- | ---------------- | ---------------------------- | -------------------------- |
| 🥉 Brute Force           | O(n)            | O(1)             | Simple, easy to implement    | Slow for larger `n`        |
| 🥈 Greedy Adjustment     | O(n) worst      | O(1)             | Faster in practice           | Still linear in worst case |
| 🥇 Digit Construction ⭐ | O(log n)        | O(1)             | Elegant, optimal, guaranteed | More complex logic         |
| ⚡ Randomized            | O(1) expected   | O(1)             | Fun, works fast              | Not deterministic          |
| 📦 Precomputation        | O(10000) setup  | O(10000)         | Instant queries              | High memory, preprocessing |

## 🎯 Why This is Optimal?

    - Brute force works but can be inefficient.
    - Greedy improves average performance.
    - Digit-by-digit construction ensures O(log n) and is the cleanest + most scalable.
    - Precomputation is good if multiple queries, but memory heavy.

### 🔑 Key Insights

| #   | Insight                                    |
| --- | ------------------------------------------ |
| 1   | No-Zero integers mean no digit `0` allowed |
| 2   | Borrowing helps fix zeros during split     |
| 3   | Optimal solution only needs `O(log n)`     |

### 💭 Common Mistakes to Avoid

| #   | Mistake          | Description                          | How to Avoid              | Example         |
| --- | ---------------- | ------------------------------------ | ------------------------- | --------------- |
| 1   | Forget digit `0` | Missing check for `0` in isNoZero    | Always validate digits    | `n=101` fails   |
| 2   | Infinite loop    | Bad randomization logic              | Add termination condition | Random approach |
| 3   | Wrong borrow     | Mishandling `d=0` in digit splitting | Carefully subtract 1      | `n=1000` issues |

### 🐛 Implementation Mistakes

| #   | Mistake             | Description                       | How to Avoid        | Example         |
| --- | ------------------- | --------------------------------- | ------------------- | --------------- |
| 1   | Off-by-one          | Looping `a <= n` instead of `< n` | Careful loop bounds | `n=2` breaks    |
| 2   | Not updating `b`    | Forgetting to recompute `b`       | Always set `b=n-a`  | Wrong outputs   |
| 3   | Precomputation leak | Not initializing table properly   | Resize vector first | Segfault issues |

### 💭 Logical Thinking Mistakes

| #   | Mistake         | Description                         | How to Avoid                | Prevention       |
| --- | --------------- | ----------------------------------- | --------------------------- | ---------------- |
| 1   | Overthinking    | Trying too complex math formulas    | Keep it digit-based         | Stick to basics  |
| 2   | Assuming unique | Thinking only one answer exists     | Accept multiple valid pairs | \[2,9] vs \[8,3] |
| 3   | Ignoring limits | Forget constraints (1971..2100 etc) | Always read constraints     | Careful parsing  |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique  | Application                          |
| --- | -------------------- | ------------------------------------ |
| 1   | Brute Force Search   | Try all splits                       |
| 2   | Greedy Increment     | Adjust until valid                   |
| 3   | Digit DP-like logic  | Build digit by digit                 |
| 4   | Randomized Search    | Monte Carlo style validation         |
| 5   | Precomputation Table | Store all answers for fast retrieval |

### 🔄 Follow-up Questions

| #   | Question                               | Answer / Approach                       |
| --- | -------------------------------------- | --------------------------------------- |
| 1   | What if `n` goes up to `10^9`?         | Digit-by-digit still works (`O(log n)`) |
| 2   | What if multiple queries asked?        | Use precomputation or memoization       |
| 3   | Can we extend to `k` no-zero integers? | Yes, recursively split into more parts  |

---

<div align="center">

**🎯 Problem 1317 Completed!**

_Happy Coding! 🚀_

</div>
