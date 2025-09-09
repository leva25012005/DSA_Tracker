<div align="center">

# 🧠 [3516. Find Closest Person](https://leetcode.com/problems/find-closest-person/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203516-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-closest-person/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                            |
| **Acceptance Rate** | `83.3%`                                                                |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-closest-person/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)     |

## Description

<!-- description:start -->

<p>You are given three integers <code>x</code>, <code>y</code>, and <code>z</code>, representing the positions of three people on a number line:</p>

<ul>
    <li><code>x</code> is the position of Person 1.</li>
    <li><code>y</code> is the position of Person 2.</li>
    <li><code>z</code> is the position of Person 3, who does <strong>not</strong> move.</li>
</ul>

<p>Both Person 1 and Person 2 move toward Person 3 at the <strong>same</strong> speed.</p>

<p>Determine which person reaches Person 3 <strong>first</strong>:</p>

<ul>
    <li>Return 1 if Person 1 arrives first.</li>
    <li>Return 2 if Person 2 arrives first.</li>
    <li>Return 0 if both arrive at the <strong>same</strong> time.</li>
</ul>

<p>Return the result accordingly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 7, z = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
- Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
- Person 2 is at position 7 and can reach Person 3 in 3 steps.
Since Person 1 reaches Person 3 first, the output is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 5, z = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
- Person 2 is at position 5 and can reach Person 3 in 1 step.
Since Person 2 reaches Person 3 first, the output is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 1, y = 5, z = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
- Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
- Person 2 is at position 5 and can reach Person 3 in 2 steps.
Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= x, y, z &lt;= 100</code></li>
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

> Move Person 1 and Person 2 one step at a time toward Person 3 until one reaches. Simulate step by step.

#### 🔍 Algorithm

```pseudo
function whoReachesFirst(x, y, z):
    steps1 = 0
    steps2 = 0
    pos1 = x
    pos2 = y

    while pos1 != z or pos2 != z:
        if pos1 < z: pos1 += 1
        else if pos1 > z: pos1 -= 1
        steps1 += 1 if pos1 != z

        if pos2 < z: pos2 += 1
        else if pos2 > z: pos2 -= 1
        steps2 += 1 if pos2 != z

    return 1 if steps1 < steps2
    return 2 if steps2 < steps1
    return 0 if steps1 == steps2
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int whoReachesFirst(int x, int y, int z) {
        int pos1 = x, pos2 = y;
        int steps1 = 0, steps2 = 0;

        while(pos1 != z || pos2 != z){
            if(pos1 != z){
                pos1 += (pos1 < z ? 1 : -1);
                steps1++;
            }
            if(pos2 != z){
                pos2 += (pos2 < z ? 1 : -1);
                steps2++;
            }
        }
        if(steps1 < steps2) return 1;
        else if(steps2 < steps1) return 2;
        return 0;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> We don’t need to simulate step by step; just calculate the distance of each person to Person 3

#### 🔍 Algorithm

```pseudo
function whoReachesFirst(x, y, z):
    distance1 = abs(x - z)
    distance2 = abs(y - z)

    if distance1 < distance2: return 1
    else if distance2 < distance1: return 2
    else: return 0

```

#### 💻 Implementation

```cpp
// Optimized approach

class Solution {
public:
    int whoReachesFirst(int x, int y, int z) {
        int dist1 = abs(x - z);
        int dist2 = abs(y - z);

        if(dist1 < dist2) return 1;
        else if(dist2 < dist1) return 2;
        return 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Same as Approach 2, but written in a single-line, concise, elegant style.

#### 🔍 Algorithm

```pseudo
function whoReachesFirst(x, y, z):
    return 1 if abs(x-z) < abs(y-z) else 2 if abs(y-z) < abs(x-z) else 0
```

#### 💻 Implementation

```cpp
// Optimal and elegant

class Solution {
public:
    int whoReachesFirst(int x, int y, int z) {
        return (abs(x - z) < abs(y - z)) ? 1 : (abs(y - z) < abs(x - z)) ? 2 : 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                       | Cons                                     |
| -------------- | --------------- | ---------------- | ------------------------------------------ | ---------------------------------------- |
| 🥉 Brute Force | O(d)            | O(1)             | Simulates movement step by step; intuitive | Inefficient for large distances          |
| 🥈 Optimized   | O(1)            | O(1)             | Simple, fast, no simulation needed         | Slightly less intuitive than brute force |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Concise, elegant, minimal code             | None significant                         |

## 🎯 Why This is Optimal?

    - Brute force simulates every step, but distance can be directly computed → reduces time complexity from O(d) to O(1).
    - Optimized and Optimal approaches use absolute distance, achieving constant time and space.
    - Optimal version is also concise, clean, and highly readable.

### 🔑 Key Insights

| #   | Insight                                                               |
| --- | --------------------------------------------------------------------- |
| 1   | Only relative distance matters, not direction of movement.            |
| 2   | Absolute difference `abs(pos - target)` gives number of steps needed. |
| 3   | Tie occurs when distances are equal; careful with equality check.     |

### 💭 Common Mistakes to Avoid

| #   | Mistake                      | Description                                    | How to Avoid             | Example                         |
| --- | ---------------------------- | ---------------------------------------------- | ------------------------ | ------------------------------- |
| 1   | Forgetting absolute value    | Negative distance if not using abs             | Always use `abs()`       | `x = 2, z = 5 → distance = -3`  |
| 2   | Incorrect tie condition      | Returning 1 or 2 when distances are equal      | Use equality check `==`  | `x = 1, y = 3, z = 2`           |
| 3   | Overcomplicating brute force | Using loops when distance calculation suffices | Think analytically first | Looping 100 steps unnecessarily |

### 🐛 Implementation Mistakes

| #   | Mistake                           | Description                          | How to Avoid                        | Example                        |
| --- | --------------------------------- | ------------------------------------ | ----------------------------------- | ------------------------------ |
| 1   | Increment/decrement wrongly       | Moving away from target accidentally | Use correct comparison (`<` or `>`) | `if pos1 > z: pos1++` ❌       |
| 2   | Counting steps incorrectly        | Counting after reaching target       | Only increment when not at target   | `steps++` even if pos == z     |
| 3   | Using wrong variable for distance | Confusing x/y/z                      | Double-check variable mapping       | `abs(y - z)` used for Person 1 |

### 💭 Logical Thinking Mistakes

| #   | Mistake                           | Description                          | How to Avoid                        | Example                        |
| --- | --------------------------------- | ------------------------------------ | ----------------------------------- | ------------------------------ |
| 1   | Increment/decrement wrongly       | Moving away from target accidentally | Use correct comparison (`<` or `>`) | `if pos1 > z: pos1++` ❌       |
| 2   | Counting steps incorrectly        | Counting after reaching target       | Only increment when not at target   | `steps++` even if pos == z     |
| 3   | Using wrong variable for distance | Confusing x/y/z                      | Double-check variable mapping       | `abs(y - z)` used for Person 1 |

### 🎯 Patterns & Techniques Used

| #   | Mistake                                    | Description                           | How to Avoid                     | Prevention                  |
| --- | ------------------------------------------ | ------------------------------------- | -------------------------------- | --------------------------- |
| 1   | Assuming closer in value = closer in steps | Negative values or reversed positions | Always compute absolute distance | `abs(x - z)`                |
| 2   | Ignoring tie cases                         | Missing `distance1 == distance2`      | Check equality explicitly        | `return 0`                  |
| 3   | Thinking direction matters                 | Only distance matters                 | Focus on steps, not direction    | Step simulation unnecessary |

### 🔄 Follow-up Questions

| #   | Question                        | Answer / Approach                                         |
| --- | ------------------------------- | --------------------------------------------------------- |
| 1   | What if multiple targets exist? | Compute distances to all targets and compare minimums     |
| 2   | What if speed differs?          | Adjust formula: `time = distance / speed` for each person |
| 3   | Can positions be negative?      | Yes, absolute difference still works                      |

---

<div align="center">

**🎯 Problem 3516 Completed!**

_Happy Coding! 🚀_

</div>
