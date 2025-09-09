<div align="center">

# 🧠 [1716. Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201716-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                               |
| ------------------- | ----------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                         |
| **Acceptance Rate** | `78.6%`                                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                  |

## Description

<!-- description:start -->

<p>Hercy wants to save money for his first car. He puts money in the Leetcode&nbsp;bank <strong>every day</strong>.</p>

<p>He starts by putting in <code>$1</code> on Monday, the first day. Every day from Tuesday to Sunday, he will put in <code>$1</code> more than the day before. On every subsequent Monday, he will put in <code>$1</code> more than the <strong>previous Monday</strong>.<span style="display: none;"> </span></p>

<p>Given <code>n</code>, return <em>the total amount of money he will have in the Leetcode bank at the end of the </em><code>n<sup>th</sup></code><em> day.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 10
<strong>Explanation:</strong>&nbsp;After the 4<sup>th</sup> day, the total is 1 + 2 + 3 + 4 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 37
<strong>Explanation:</strong>&nbsp;After the 10<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2<sup>nd</sup> Monday, Hercy only puts in $2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 96
<strong>Explanation:</strong>&nbsp;After the 20<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
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

## 🔗 Related Problems

| Problem                                                                                                     | Difficulty  | Relationship  |
| ----------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| [Distribute Money to Maximum Children](https://leetcode.com/problems/distribute-money-to-maximum-children/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Day-by-Day Simulation (Brute Force)

#### 📝 Intuition

> Simulate the process of depositing money day by day.  
> Start from Monday with $1. Each next day in the week increases by +1. Each new Mon

#### 🔍 Algorithm

```pseudo
function totalMoney(n):
    total = 0, start = 1   // Monday deposit
    initialize day = 0
    for i in range(1 to n):
        total += start + (day % 7)
        if day % 7 == 6:   // Sunday → move to next Monday
            start += 1
        day += 1
    return total
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int totalMoney(int n) {
        int total = 0, start = 1;
        for (int i = 0; i < n; i++) {
            total += start + (i % 7);
            if (i % 7 == 6) start++;
        }
        return total;
    }
};
```

### 🥈 Approach 2: Week-based Iteration (Optimized Solution)

#### 📝 Intuition

> Divide n into full weeks (weeks = n / 7) and remaining days (days = n % 7).
>
> - Each week is an arithmetic progression of 7 terms.
> - Compute the total of full weeks, then add the remainder days.

#### 🔍 Algorithm

```pseudo
function totalMoney(n):
    weeks = n / 7
    days = n % 7
    total = 0
    for w in range(0 to weeks-1):
        total += (7 * (w+1)) + 21   // each week sum
    for d in range(0 to days-1):
        total += (weeks+1) + d
    return total
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7, days = n % 7;
        int total = 0;
        for (int w = 0; w < weeks; w++) {
            total += 7 * (w + 1) + 21;
        }
        for (int d = 0; d < days; d++) {
            total += (weeks + 1) + d;
        }
        return total;
    }
};
```

### 🥇 Approach 3: Mathematical Formula (Optimal Solution ⭐)

#### 📝 Intuition

> Derive a closed formula:
> **Sum of full weeks:**
>
> $$
> \text{total\_weeks} = 28 \times \text{weeks} + \frac{7 \times \text>{weeks} \times (\text{weeks} - 1)}{2}
> $$
>
> **Sum of leftover days:**
>
> $$
> \text{total\_days} = \text{days} \times (\text{weeks} + 1) + \frac>{\text{days} \times (\text{days} - 1)}{2}
> $$

#### 🔍 Algorithm

```pseudo
function totalMoney(n):
    weeks = n / 7
    days = n % 7
    total_weeks = 28 * weeks + 7 * weeks * (weeks - 1) / 2
    total_days = days * (weeks+1) + days * (days-1) / 2
    return total_weeks + total_days
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7, days = n % 7;
        int totalWeeks = 28 * weeks + 7 * (weeks * (weeks - 1)) / 2;
        int totalDays = days * (weeks + 1) + (days * (days - 1)) / 2;
        return totalWeeks + totalDays;
    }
};
```

### 🟦 Approach 4: Dynamic Programming (DP)

#### 📝 Intuition

> Define:
>
> $$
> dp[i] = \text{total money after day } i
> $$
>
> Transition:
>
> $$
> dp[i] = dp[i-1] + money\_on\_day(i)
> $$
>
> Precompute sequentially up to $n$.

#### 🔍 Algorithm

```pseudo
function totalMoney(n):
    dp[0] = 0
    start = 1
    for i in range(1 to n):
        dp[i] = dp[i-1] + (start + (i-1) % 7)
        if i % 7 == 0:
            start += 1
    return dp[n]
```

#### 💻 Implementation

```cpp
class Solution {
public:
    int totalMoney(int n) {
        vector<int> dp(n+1, 0);
        int start = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1] + start + (i-1) % 7;
            if (i % 7 == 0) start++;
        }
        return dp[n];
    }
};
```

### 🟩 Approach 5: Prefix Sum Precomputation (Multi-Query)

#### 📝 Intuition

> If multiple queries are required, precompute dp[i] = total after i days for all i up to max.
> Answer each query in O(1).

#### 🔍 Algorithm

```pseudo
function totalMoney(n):
    precompute dp[0..maxN]
    for query(n):
        return dp[n]
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
    vector<int> dp;
public:
    Solution() {
        int maxN = 1000; // per constraints
        dp.resize(maxN+1, 0);
        int start = 1;
        for (int i = 1; i <= maxN; i++) {
            dp[i] = dp[i-1] + start + (i-1) % 7;
            if (i % 7 == 0) start++;
        }
    }

    int totalMoney(int n) {
        return dp[n];
    }
};
```

## 📊 Comparison of Approaches

| Approach                 | Time Complexity | Space Complexity | Pros                    | Cons                          |
| ------------------------ | --------------- | ---------------- | ----------------------- | ----------------------------- |
| 🥉 Brute Force           | O(n)            | O(1)             | Easy to implement       | Slow for large n              |
| 🥈 Week Iteration        | O(n/7)          | O(1)             | Faster than brute force | Still loop-based              |
| 🥇 Formula ⭐            | O(1)            | O(1)             | Fastest & most elegant  | Harder to derive              |
| 🟦 DP                    | O(n)            | O(n)             | Clear transition logic  | Overkill for one query        |
| 🟩 Prefix Sum Precompute | O(1)/query      | O(n)             | Useful for many queries | Memory waste for single query |

## 🎯 Why This is Optimal?

    - Formula approach is the best for single queries (O(1), O(1)).
    - DP and Prefix Sum approaches are only meaningful if we need multiple queries.
    - Brute force & week iteration are educational but not practical for large n.

### 🔑 Key Insights

| #   | Insight                                            |
| --- | -------------------------------------------------- |
| 1   | The problem has a 7-day repeating structure.       |
| 2   | Each week forms an arithmetic progression.         |
| 3   | Full weeks can be calculated using formulas.       |
| 4   | DP/Prefix Sum is useful for multi-query scenarios. |

### 💭 Common Mistakes to Avoid

| #   | Mistake              | Description            | How to Avoid              | Example               |
| --- | -------------------- | ---------------------- | ------------------------- | --------------------- |
| 1   | Misusing AP formula  | Forget offset per week | Derive week sum carefully | Week 1 = 28           |
| 2   | Forget leftover days | Only count full weeks  | Always add remainder      | n=10 → need + (2+3+4) |
| 3   | Off-by-one errors    | Wrong Monday increment | Double check mod 7 logic  | Day 7 = Sunday        |

### 🐛 Implementation Mistakes

| #   | Mistake           | Description                | How to Avoid           | Example                |
| --- | ----------------- | -------------------------- | ---------------------- | ---------------------- |
| 1   | Wrong %7 logic    | Using (i%7==0) incorrectly | Careful with day index | Day 7 should be Sunday |
| 2   | Array size issues | Not allocating enough DP   | Always size = n+1      | dp\[n]                 |
| 3   | Overflow concerns | But here n ≤ 1000, safe    | Use int                | -                      |

### 💭 Logical Thinking Mistakes

| #   | Mistake                    | Description                      | How to Avoid                 | Prevention               |
| --- | -------------------------- | -------------------------------- | ---------------------------- | ------------------------ |
| 1   | Assume weeks are identical | Actually each week starts higher | Observe Week 1=28, Week 2=35 | Write first few weeks    |
| 2   | Over-optimizing too early  | Jump directly to formula & fail  | Start with brute force       | Verify with small inputs |
| 3   | Miscomputing remainder     | Forget offset weeks+1            | Explicitly use weeks+1       | Test with n=10           |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique    | Application                     |
| --- | ---------------------- | ------------------------------- |
| 1   | Simulation             | Brute force day by day          |
| 2   | Arithmetic Progression | Sum of weekly deposits          |
| 3   | Modular Arithmetic     | Find day within the week        |
| 4   | DP / Prefix Sum        | Precompute for multiple queries |

### 🔄 Follow-up Questions

| #   | Question                      | Answer / Approach                |
| --- | ----------------------------- | -------------------------------- |
| 1   | What if n ≤ 1e9?              | Only formula O(1) works.         |
| 2   | What if multiple queries?     | Prefix sum or DP precomputation. |
| 3   | What if deposit rule changes? | Adjust AP formula accordingly.   |

---

<div align="center">

**🎯 Problem 1716 Completed!**

_Happy Coding! 🚀_

</div>
