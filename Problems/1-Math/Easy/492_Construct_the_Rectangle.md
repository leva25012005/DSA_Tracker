<div align="center">

# 🧠 [492. Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20492-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/construct-the-rectangle/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                |
| **Acceptance Rate** | `61.3%`                                                                    |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/construct-the-rectangle/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)         |

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `06-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `06-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> If area % W == 0 then L = area / W.
> The simplest idea: iterate over all W values ​​from 1 → area.
> Keep the pair (L, W) that satisfy L >= W and has the smallest |L - W|.

#### 🔍 Algorithm

```pseudo
function constructRectangle(area):
    for w = 1 to area:
        if area % w == 0:
            L = area / w
            if L >= W:
                update best_pair if |L - W| smaller
    return best_pair
```

#### 💻 Implementation

```cpp
class Solution {
public:
    vector<int> solutionBruteForce(int area) {
        int bestL = area, bestW = 1;
        for (int w = 1; w <= area; w++) {
            if (area % w == 0) {
                int l = area / w;
                if (l >= w && abs(l - w) < abs(bestL - bestW)) {
                    bestL = l;
                    bestW = w;
                }
            }
        }
        return {bestL, bestW};
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Instead of going through 1..area, we only need to consider √area.
> If area % w == 0, we take L = area / w.
> The first pair found from √area down will be the closest pair.

#### 🔍 Algorithm

```pseudo
function constructRectangle(area):
    start from w = floor(sqrt(area)) down to 1:
        if area % w == 0:
            L = area / w
            return [L, w]
```

#### 💻 Implementation

```cpp
class Solution {
public:
    vector<int> solutionOptimized(int area) {
        for (int w = sqrt(area); w >= 1; w--) {
            if (area % w == 0) {
                return {area / w, w};
            }
        }
        return {area, 1}; // fallback
    }
};

```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Same as Approach 2 but use the first result from √area down.

#### 🔍 Algorithm

```pseudo
function constructRectangle(area):
    w = floor(sqrt(area))
    while w >= 1:
        if area % w == 0:
            return [area / w, w]
        w -= 1
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    vector<int> solutionOptimal(int area) {
        int w = sqrt(area);
        while (w > 0) {
            if (area % w == 0) {
                return {area / w, w};
            }
            w--;
        }
        return {area, 1};
    }
};

```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                           |
| -------------- | --------------- | ---------------- | ------------------------------- | ------------------------------ |
| 🥉 Brute Force | O(area)         | O(1)             | Simple, easy to understand idea | Too slow for large areas       |
| 🥈 Optimized   | O(√area)        | O(1)             | Faster, easy to implement       | Requires knowledge of divisors |
| 🥇 Optimal ⭐  | O(√area)        | O(1)             | Compact, efficient, scalable    | No disadvantages               |

## 🎯 Why This is Optimal?

    - Brute Force full scan → not feasible with area = 10^7.
    - Optimized reduces to O(√n), but can still scan all.
    - Optimal (starting from √area down) ensures the first pair found is the best → both fast and neat.

### 🔑 Key Insights

| #   | Insight                                         |
| --- | ----------------------------------------------- |
| 1   | The closest pair of (L, W) will be around √area |
| 2   | Only need to consider √area, no need for n      |
| 3   | The first pair from √area down is optimal       |

### 💭 Common Mistakes to Avoid

| #   | Mistake          | Description                                         | How to Avoid                   | Example                     |
| --- | ---------------- | --------------------------------------------------- | ------------------------------ | --------------------------- |
| 1   | Browse to area   | Unnecessary, easy TLE                               | Limit browsing to √area        | area = 10^7                 |
| 2   | Do not check L≥W | Can return inverted result (W > L)                  | Always ensure L = area / W     | \[1, 37] instead of \[37,1] |
| 3   | Wrong data type  | When sqrt or divide, easy to get float/int mismatch | Use int when taking sqrt(area) | sqrt(37) = 6.x → 6          |

### 🐛 Implementation Mistakes

| #   | Mistake          | Description                         | How to Avoid            | Example                |                        |     |
| --- | ---------------- | ----------------------------------- | ----------------------- | ---------------------- | ---------------------- | --- |
| 1   | Forgot to return | Don't return results in loop        | Return as soon as found |                        |                        |     |
| 2   | Abs() error      | No need to calculate                | L-W                     | if starting from √area | Just return first pair |     |
| 3   | Wrong sqrt type  | Using double without casting to int | `int w = sqrt(area)`    |                        |                        |     |

### 💭 Logical Thinking Mistakes

| #   | Mistake                     | Description                      | How to Avoid                               | Prevention          |
| --- | --------------------------- | -------------------------------- | ------------------------------------------ | ------------------- |
| 1   | Think must go through all   | Think need to check all 1..area  | Remember the symmetry property of divisors | Review factor pairs |
| 2   | Mistake L and W             | May return \[W, L] wrong request | Ensure `L = area / W`                      | Check output        |
| 3   | Ignore the case of area = 1 | Easily miss edge case            | Test smallest case                         | Input check         |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                                   |
| --- | ------------------- | --------------------------------------------- |
| 1   | Factor Pairs        | Find divisors in pairs (L, W)                 |
| 2   | Square Root Trick   | Reduce the search from n to √n                |
| 3   | Greedy Selection    | Pick the first pair that meets the conditions |

### 🔄 Follow-up Questions

| #   | Question                                  | Answer / Approach                                   |
| --- | ----------------------------------------- | --------------------------------------------------- |
| 1   | If there are many different query areas?  | Precompute divisors for all first                   |
| 2   | If you want min(L/W) instead of min(L-W)? | Replace comparison metric, still iterate from √area |
| 3   | If the area is very large (10^12)?        | Still use √area, but need long long                 |

---

<div align="center">

**🎯 Problem 492 Completed!**

_Happy Coding! 🚀_

</div>
