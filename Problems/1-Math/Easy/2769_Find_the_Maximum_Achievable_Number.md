<div align="center">

# 🧠 [2769. Find the Maximum Achievable Number](https://leetcode.com/problems/find-the-maximum-achievable-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202769-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-the-maximum-achievable-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                           |
| **Acceptance Rate** | `91.0%`                                                                               |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-the-maximum-achievable-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                    |

## Description

<!-- description:start -->

<p>Given two integers, <code>num</code> and <code>t</code>. A <strong>number </strong><code>x</code><strong> </strong>is <strong>achievable</strong> if it can become equal to <code>num</code> after applying the following operation <strong>at most</strong> <code>t</code> times:</p>

<ul>
    <li>Increase or decrease <code>x</code> by <code>1</code>, and <em>simultaneously</em> increase or decrease <code>num</code> by <code>1</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> possible value of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 4, t = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> Apply the following operation once to make the maximum achievable number equal to <code>num</code>:
- Decrease the maximum achievable number by 1, and increase <code>num</code> by 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 3, t = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Apply the following operation twice to make the maximum achievable number equal to <code>num</code>:
- Decrease the maximum achievable number by 1, and increase <code>num</code> by 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= num, t &lt;= 50</code></li>
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

> Simulate each of the t operations step by step. At each operation, increase x by 1 and decrease num by 1 to maximize x.

#### 🔍 Algorithm

```pseudo
maxAchievableNumber(x, num, t):
    for i from 1 to t:
        x = x + 1
        num = num - 1
    return x
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int maximumAchievableX(int num, int t) {
        int x = num;
        for (int i = 0; i < t; i++) {
            x += 1;
            num -= 1;
        }
        return x;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Each operation increases x by 2 relative to the original num. After t operations, the maximum achievable value of x can be computed directly using a formula without simulating each step.

#### 🔍 Algorithm

```pseudo
maxAchievableNumber(num, t):
    return num + 2 * t
```

#### 💻 Implementation

```cpp
// Optimal approach using direct formula

class Solution {
public:
    int maximumAchievableX(int num, int t) {
        return num + 2 * t;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                              | Cons                       |
| -------------- | --------------- | ---------------- | --------------------------------- | -------------------------- |
| 🥉 Brute Force | O(t)            | O(1)             | Simple, easy to understand        | Slower for large t         |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fast, elegant, direct calculation | Needs mathematical insight |

## 🎯 Why This is Optimal?

    - Direct formula avoids loops and provides O(1) solution.
    - Reduces time complexity from O(t) to O(1) and uses minimal space.
    - Clean, scalable, and easy to implement.

### 🔑 Key Insights

| #   | Insight                                              |
| --- | ---------------------------------------------------- |
| 1   | Each operation increases x by 2 relative to num.     |
| 2   | Simulation is unnecessary if formula is applied.     |
| 3   | Direct computation ensures constant time complexity. |

### 💭 Common Mistakes to Avoid

| #   | Mistake                        | Description                                 | How to Avoid                                       | Example           |
| --- | ------------------------------ | ------------------------------------------- | -------------------------------------------------- | ----------------- |
| 1   | Forgetting the relative change | Only increase x by 1 without decreasing num | Remember x increases by 2 relative to original num | t=3, num=4, x=10? |
| 2   | Using wrong formula            | Using num + t instead of num + 2\*t         | Derive carefully from the operation                | -                 |

### 🐛 Implementation Mistakes

| #   | Mistake                         | Description                           | How to Avoid           | Example |
| --- | ------------------------------- | ------------------------------------- | ---------------------- | ------- |
| 1   | Loop bounds incorrect           | Using i <= t instead of i < t         | Check iteration limits | -       |
| 2   | Modifying input unintentionally | Changing num outside loop incorrectly | Track variable usage   | -       |

### 💭 Logical Thinking Mistakes

| #   | Mistake                       | Description                               | How to Avoid                              | Prevention |
| --- | ----------------------------- | ----------------------------------------- | ----------------------------------------- | ---------- |
| 1   | Misinterpreting the operation | Not realizing x increases relative to num | Analyze the effect of operation carefully | -          |
| 2   | Overcomplicating the solution | Attempting simulation when formula works  | Derive formula instead                    | -          |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                  |
| --- | ------------------- | ---------------------------- |
| 1   | Simulation          | Approach 1                   |
| 2   | Direct computation  | Approach 2 (Optimal Formula) |

### 🔄 Follow-up Questions

| #   | Question                               | Answer / Approach                     |
| --- | -------------------------------------- | ------------------------------------- |
| 1   | What if t is very large?               | Approach 2 still works in O(1)        |
| 2   | Can we track intermediate values of x? | Yes, simulation approach records them |

---

<div align="center">

**🎯 Problem 2769 Completed!**

_Happy Coding! 🚀_

</div>
