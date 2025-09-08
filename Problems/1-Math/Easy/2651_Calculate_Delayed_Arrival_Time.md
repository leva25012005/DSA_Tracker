<div align="center">

# 🧠 [2651. Calculate Delayed Arrival Time](https://leetcode.com/problems/calculate-delayed-arrival-time/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202651-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/calculate-delayed-arrival-time/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                             |
| ------------------- | --------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                       |
| **Acceptance Rate** | `76.2%`                                                                           |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/calculate-delayed-arrival-time/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>arrivalTime</code> denoting the arrival time of a train in hours, and another positive integer <code>delayedTime</code> denoting the amount of delay in hours.</p>

<p>Return <em>the time when the train will arrive at the station.</em></p>

<p>Note that the time in this problem is in 24-hours format.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arrivalTime = 15, delayedTime = 5 
<strong>Output:</strong> 20 
<strong>Explanation:</strong> Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arrivalTime = 13, delayedTime = 11
<strong>Output:</strong> 0
<strong>Explanation:</strong> Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arrivaltime &lt;&nbsp;24</code></li>
	<li><code>1 &lt;= delayedTime &lt;= 24</code></li>
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

> The simplest idea: add arrivalTime + delayedTime to calculate the new arrival time.
> If the result is >= 24, subtract 24 repeatedly until it fits into the 24-hour format.

#### 🔍 Algorithm

```pseudo
function findDelayedArrivalTime(arrivalTime, delayedTime):
    sum = arrivalTime + delayedTime
    while sum >= 24:
        sum -= 24
    return sum
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int sum = arrivalTime + delayedTime;
        while (sum >= 24) {
            sum -= 24;
        }
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Instead of using a while loop, we just need one check:
>
> - If arrivalTime + delayedTime < 24 → return directly.
> - Otherwise → subtract 24 once.

#### 🔍 Algorithm

```pseudo
function findDelayedArrivalTime(arrivalTime, delayedTime):
    sum = arrivalTime + delayedTime
    if sum < 24:
        return sum
    else:
        return sum - 24
```

#### 💻 Implementation

```cpp
// Optimized approach with condition
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int sum = arrivalTime + delayedTime;
        return (sum < 24) ? sum : sum - 24;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> The cleanest and most elegant solution is to use modulo arithmetic.
>
> - Formula: (arrivalTime + delayedTime) % 24.
> - It automatically handles both cases: less than 24 and wrap-around at 24.

#### 🔍 Algorithm

```pseudo
findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 25;
```

#### 💻 Implementation

```cpp
/// Most optimal and elegant solution
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity  | Space Complexity | Pros                                | Cons                      |
| -------------- | ---------------- | ---------------- | ----------------------------------- | ------------------------- |
| 🥉 Brute Force | O(k) (k = delay) | O(1)             | Intuitive, simulates step-by-step   | Overkill for this problem |
| 🥈 Optimized   | O(1)             | O(1)             | Simple, readable, no loops          | Slightly more verbose     |
| 🥇 Optimal ⭐  | O(1)             | O(1)             | Short, elegant, mathematically neat | None                      |

## 🎯 Why This is Optimal?

    - Brute force repeats unnecessary subtractions.
    - Optimized removes the loop but still uses conditionals.
    - Optimal uses modulo, which is mathematically direct, fastest, and cleanest.

### 🔑 Key Insights

| #   | Insight                                                                        |
| --- | ------------------------------------------------------------------------------ |
| 1   | Time is cyclical in 24-hour format, making modulo the natural choice.          |
| 2   | Loops are unnecessary when the adjustment is predictable.                      |
| 3   | Modulo guarantees correctness in both small and large values of `delayedTime`. |

### 💭 Common Mistakes to Avoid

| #   | Mistake                 | Description                                    | How to Avoid                         | Example                                              |
| --- | ----------------------- | ---------------------------------------------- | ------------------------------------ | ---------------------------------------------------- |
| 1   | Forgetting modulo       | Returning `arrivalTime + delayedTime` directly | Always ensure result is in `[0, 23]` | Input: `13, 11` → Output `24` (wrong), should be `0` |
| 2   | Off-by-one error        | Misunderstanding midnight as 24 instead of 0   | Remember 24:00 = 0:00                | Input: `23, 1` → Wrong `24`, correct `0`             |
| 3   | Using unnecessary loops | Iteratively subtracting 24                     | Use `if` or `%` instead              | Brute force implementation                           |

### 🐛 Implementation Mistakes

| #   | Mistake                          | Description                           | How to Avoid                  | Example                                 |
| --- | -------------------------------- | ------------------------------------- | ----------------------------- | --------------------------------------- |
| 1   | Using division instead of modulo | Returns quotient instead of remainder | Use `%` not `/`               | `(15+5)/24 = 0` (wrong), should be `20` |
| 2   | Negative handling                | Assuming inputs can be negative       | Constraints ensure positivity | N/A                                     |
| 3   | Hardcoding conditions            | Writing many `if`s for each hour      | Use math formula              | Code gets too verbose                   |

### 💭 Logical Thinking Mistakes

| #   | Mistake                     | Description                    | How to Avoid                       | Prevention                 |
| --- | --------------------------- | ------------------------------ | ---------------------------------- | -------------------------- |
| 1   | Thinking 24 is valid        | Returning `24` as a valid hour | Map `24` → `0`                     | Always apply modulo        |
| 2   | Overcomplicating problem    | Adding extra checks for AM/PM  | Problem is strictly 24-hour format | Read constraints carefully |
| 3   | Forgetting edge constraints | Ignoring upper bound `24`      | Validate using `% 24`              | Test with max inputs       |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                             |
| --- | ------------------- | --------------------------------------- |
| 1   | Modular Arithmetic  | Handling cyclic values like clock time  |
| 2   | Simulation          | Brute force simulates subtraction of 24 |
| 3   | Conditional Logic   | Optimized approach without loops        |

### 🔄 Follow-up Questions

| #   | Question                                           | Answer / Approach                                                        |
| --- | -------------------------------------------------- | ------------------------------------------------------------------------ |
| 1   | What if time format is 12-hour instead of 24-hour? | Replace `% 24` with `% 12` and adjust for AM/PM.                         |
| 2   | What if we want minutes/seconds precision?         | Use modulo with `1440` (minutes in a day) or `86400` (seconds in a day). |
| 3   | How to handle negative delayed time?               | Apply `(arrivalTime + delayedTime + 24) % 24` to avoid negatives.        |

---

<div align="center">

**🎯 Problem 2651 Completed!**

_Happy Coding! 🚀_

</div>
