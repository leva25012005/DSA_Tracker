<div align="center">

# 🧠 [3492. Maximum Containers on a Ship](https://leetcode.com/problems/maximum-containers-on-a-ship/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203492-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/maximum-containers-on-a-ship/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                           |
| ------------------- | ------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                     |
| **Acceptance Rate** | `74.7%`                                                                         |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/maximum-containers-on-a-ship/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)              |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>n</code> representing an <code>n x n</code> cargo deck on a ship. Each cell on the deck can hold one container with a weight of <strong>exactly</strong> <code>w</code>.</p>

<p>However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, <code>maxWeight</code>.</p>

<p>Return the <strong>maximum</strong> number of containers that can be loaded onto the ship.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2, w = 3, maxWeight = 15
<strong>Output:</strong> 4
<strong>Explanation:</strong> The deck has 4 cells, and each container weighs 3. The total weight of loading all containers is 12, which does not exceed <code>maxWeight</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, w = 5, maxWeight = 20
<strong>Output:</strong> 4
<strong>Explanation:</strong> The deck has 9 cells, and each container weighs 5. The maximum number of containers that can be loaded without exceeding <code>maxWeight</code> is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= n &lt;= 1000</code></li>
    <li><code>1 &lt;= w &lt;= 1000</code></li>
    <li><code>1 &lt;= maxWeight &lt;= 10<sup>9</sup></code></li>
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

> Start from zero containers and try adding containers one by one, counting until we reach either the deck limit or maximum weight. Simple simulation approach.

#### 🔍 Algorithm

```pseudo
function maxContainers(n, w,totalWeight):
maxContainers = 0
for each cell in n x n deck:
    if totalWeight + w <= maxWeight:
        totalWeight += w
        maxContainers += 1
    else:
        break
return maxContainers
```

#### 💻 Implementation

```cpp
/// Brute force approach

class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        int totalWeight = 0;
        int maxContainers = 0;
        for(int i = 0; i < n * n; ++i){
            if(totalWeight + w <= maxWeight){
                totalWeight += w;
                maxContainers++;
            } else break;
        }
        return maxContainers;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> nstead of simulating each container, calculate the total cells and the maximum containers allowed by weight. Return the minimum of the two.

#### 🔍 Algorithm

```pseudo
function maxContainers(n, w,totalWeight):
    totalCells = n * n
    maxByWeight = maxWeight / w
    return min(totalCells, maxByWeight)
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity

class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        int totalCells = n * n;
        int maxByWeight = maxWeight / w;
        return min(totalCells, maxByWeight);
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Same as Approach 2, but written in most concise, elegant, and O(1) form without any temporary variables.

#### 🔍 Algorithm

```pseudo
function maxContainers(n, w,totalWeight):
    return min(n*n, maxWeight / w)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        return min(n*n, maxWeight / w);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                       | Cons                                     |
| -------------- | --------------- | ---------------- | -------------------------- | ---------------------------------------- |
| 🥉 Brute Force | O(n²)           | O(1)             | Simple, easy to understand | Inefficient for large n                  |
| 🥈 Optimized   | O(1)            | O(1)             | Fast, simple               | Slightly less intuitive than brute force |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Concise, elegant, optimal  | None                                     |

## 🎯 Why This is Optimal?

    - Brute force loops through each cell, which is unnecessary.
    - Optimized/Optimal use arithmetic to calculate maximum containers in O(1).
    - Clean, readable, and scalable for n up to 1000

### 🔑 Key Insights

| #   | Insight                                        |
| --- | ---------------------------------------------- |
| 1   | Max containers limited by deck size or weight  |
| 2   | Arithmetic calculation avoids iteration        |
| 3   | O(1) solution is always preferable if feasible |

### 💭 Common Mistakes to Avoid

| #   | Mistake             | Description                                  | How to Avoid                | Example                                |
| --- | ------------------- | -------------------------------------------- | --------------------------- | -------------------------------------- |
| 1   | Overflow            | Using `n*n` might overflow in some languages | Use long/int64 if necessary | n=1000, n\*n = 1000000                 |
| 2   | Floor division      | Forgetting integer division for weight       | Use `maxWeight / w`         | 15/3=5 OK, 15/2=7                      |
| 3   | Exceeding maxWeight | Not checking min(totalCells, maxByWeight)    | Always take min             | totalCells=9, maxByWeight=4 → answer=4 |

### 🐛 Implementation Mistakes

| #   | Mistake            | Description                         | How to Avoid                 | Example                          |
| --- | ------------------ | ----------------------------------- | ---------------------------- | -------------------------------- |
| 1   | Off-by-one         | Counting containers incorrectly     | Carefully define loop limits | Loop i=1 to n² vs i=0 to n²-1    |
| 2   | Wrong min function | Forget min(totalCells, maxByWeight) | Always use min()             | n=3, maxByWeight=4 → answer=4    |
| 3   | Ignoring weight    | Only count cells                    | Check weight                 | maxWeight too small to fill deck |

### 💭 Logical Thinking Mistakes

| #   | Mistake                     | Description            | How to Avoid                             | Prevention                      |
| --- | --------------------------- | ---------------------- | ---------------------------------------- | ------------------------------- |
| 1   | Assuming all containers fit | May exceed maxWeight   | Always check min(deckCells, weightLimit) | Use formula                     |
| 2   | Misreading constraints      | n, w, maxWeight limits | Carefully read problem                   | Check constraints before coding |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique  | Application                         |
| --- | -------------------- | ----------------------------------- |
| 1   | Greedy / Simulation  | Approach 1                          |
| 2   | Mathematical formula | Approach 2 & 3                      |
| 3   | Min function         | Ensures we don’t exceed constraints |

### 🔄 Follow-up Questions

| #   | Question                                   | Answer / Approach                     |
| --- | ------------------------------------------ | ------------------------------------- |
| 1   | What if containers have different weights? | Use greedy or knapsack approach       |
| 2   | What if deck is rectangular?               | totalCells = rows \* cols             |
| 3   | Can we handle very large n, w?             | Use 64-bit integers to avoid overflow |

---

<div align="center">

**🎯 Problem 3492 Completed!**

_Happy Coding! 🚀_

</div>
