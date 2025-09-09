<div align="center">

# 🧠 [3560. Find Minimum Log Transportation Cost](https://leetcode.com/problems/find-minimum-log-transportation-cost/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203560-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-minimum-log-transportation-cost/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                             |
| **Acceptance Rate** | `41.5%`                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-minimum-log-transportation-cost/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                      |

## Description

<!-- description:start -->

<p>You are given integers <code>n</code>, <code>m</code>, and <code>k</code>.</p>

<p>There are two logs of lengths <code>n</code> and <code>m</code> units, which need to be transported in three trucks where each truck can carry one log with length <strong>at most</strong> <code>k</code> units.</p>

<p>You may cut the logs into smaller pieces, where the cost of cutting a log of length <code>x</code> into logs of length <code>len1</code> and <code>len2</code> is <code>cost = len1 * len2</code> such that <code>len1 + len2 = x</code>.</p>

<p>Return the <strong>minimum total cost</strong> to distribute the logs onto the trucks. If the logs don't need to be cut, the total cost is 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6, m = 5, k = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> Cut the log with length 6 into logs with length 1 and 5, at a cost equal to 1 * 5 = 5. 
Now the three logs of length 1, 5, and 5 can fit in one truck each.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, m = 4, k = 6
<strong>Output:</strong> 0
<strong>Explanation:</strong> The two logs can fit in the trucks already, hence we don't need to cut the logs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>2 &lt;= k &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= n, m &lt;= 2 * k</code></li>
    <li>The input is generated such that it is always possible to transport the logs.</li>
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

> Try all possible ways to cut the logs into pieces such that each piece fits in a truck (≤ k units) and select the combination with the minimum total cost.

#### 🔍 Algorithm

```pseudo
minCostBruteForce(n, m, k):
    for each possible cut of log n:
        for each possible cut of log m:
            if all resulting pieces ≤ k:
                compute cost of cuts
                update minimum cost
    return minimum cost
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int minCostBruteForce(int n, int m, int k) {
        int minCost = INT_MAX;
        for (int cutN = 0; cutN <= n; ++cutN) {
            for (int cutM = 0; cutM <= m; ++cutM) {
                vector<int> pieces = {cutN, n - cutN, cutM, m - cutM};
                bool valid = true;
                int cost = cutN * (n - cutN) + cutM * (m - cutM);
                for (int p : pieces) if (p > k) valid = false;
                if (valid) minCost = min(minCost, cost);
            }
        }
        return minCost == INT_MAX ? 0 : minCost;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Only cut logs that exceed k, each log at most once. If log ≤ k → no cut needed. If log > k → cut it into k and remaining part to minimize cost.

#### 🔍 Algorithm

```pseudo
minCostBruteForce(n, m, k):
    cost = 0
    for log in [n, m]:
        if log > k:
            cost += (log - k) * k
    return cost

```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity

class Solution {
public:
    int minCostGreedy(int n, int m, int k) {
        int cost = 0;
        if (n > k) cost += (n - k) * k;
        if (m > k) cost += (m - k) * k;
        return cost;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Directly compute minimal cuts using formula: for each log L > k, cut into pieces k and L-k → cost = k\*(L-k). Sum for both logs. No loops needed.

#### 🔍 Algorithm

```pseudo
minCostBruteForce(n, m, k):
    cost = 0
    if n > k:
        cost += (n - k) * k
    if m > k:
        cost += (m - k) * k
    return cost
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int minCostOptimal(int n, int m, int k) {
        return max(0, n - k) * (n > k ? k : 0) + max(0, m - k) * (m > k ? k : 0);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                  | Cons                              |
| -------------- | --------------- | ---------------- | --------------------- | --------------------------------- |
| 🥉 Brute Force | O(n\*m)         | O(1)             | Guaranteed correct    | Very slow for large n,m           |
| 🥈 Greedy      | O(1)            | O(1)             | Fast, simple          | Needs reasoning to ensure optimal |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant, minimal code | Relies on formula understanding   |

## 🎯 Why This is Optimal?

    - Brute force checks all possibilities → slow
    - Greedy uses observation that each log can be cut at most once → fast
    - Optimal uses formula → O(1), direct computation, very clean and scalable

### 🔑 Key Insights

| #   | Insight                                        |
| --- | ---------------------------------------------- |
| 1   | Only logs longer than k need to be cut         |
| 2   | Each log is cut into at most two pieces        |
| 3   | Cost formula: cost = k \* (L - k) for each log |

### 💭 Common Mistakes to Avoid

| #   | Mistake         | Description                                    | How to Avoid                 | Example                          |
| --- | --------------- | ---------------------------------------------- | ---------------------------- | -------------------------------- |
| 1   | Overcut         | Cutting logs unnecessarily                     | Only cut if L > k            | Cutting log of size 4 when k = 5 |
| 2   | Miscompute cost | Forget formula L1\*L2                          | Always apply cost = k\*(L-k) | Log 6 cut into 1+5 → 1\*5=5      |
| 3   | Swap logs       | Treating n/m as interchangeable when reasoning | Always compute separately    | n=6, m=5, k=5                    |

### 🐛 Implementation Mistakes

| #   | Mistake     | Description                                     | How to Avoid           | Example            |
| --- | ----------- | ----------------------------------------------- | ---------------------- | ------------------ |
| 1   | Indexing    | Using array indexing incorrectly in brute force | Check loops            | for cutN in 0..n   |
| 2   | Overflow    | Using int for very large n,m,k                  | Use long/long long     | n=100000, k=100000 |
| 3   | Conditional | Forget to check if log > k                      | Always guard condition | if(n>k) ...        |

### 💭 Logical Thinking Mistakes

| #   | Mistake                       | Description                      | How to Avoid      | Prevention               |
| --- | ----------------------------- | -------------------------------- | ----------------- | ------------------------ |
| 1   | Thinking all logs must be cut | Only cut logs > k                | Apply conditional | n ≤ k → 0 cost           |
| 2   | Cutting multiple times        | Only cut once per log            | Greedy choice     | L>k → cut into k + (L-k) |
| 3   | Misorder                      | Not checking which log is longer | Sort if needed    | n=6, m=5, k=5            |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                 |
| --- | ------------------- | --------------------------- |
| 1   | Greedy              | Cut only if log > k         |
| 2   | Math / Formula      | cost = k\*(L-k)             |
| 3   | Case Analysis       | Treat each log individually |

### 🔄 Follow-up Questions

| #   | Pattern / Technique | Application                 |
| --- | ------------------- | --------------------------- |
| 1   | Greedy              | Cut only if log > k         |
| 2   | Math / Formula      | cost = k\*(L-k)             |
| 3   | Case Analysis       | Treat each log individually |

---

<div align="center">

**🎯 Problem 3560 Completed!**

_Happy Coding! 🚀_

</div>
