<div align="center">

# 🧠 [2806. Account Balance After Rounded Purchase](https://leetcode.com/problems/account-balance-after-rounded-purchase/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202806-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/account-balance-after-rounded-purchase/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                               |
| **Acceptance Rate** | `55.3%`                                                                                   |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/account-balance-after-rounded-purchase/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                        |

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

<p>Initially, you have a bank account balance of <strong>100</strong> dollars.</p>

<p>You are given an integer <code>purchaseAmount</code> representing the amount you will spend on a purchase in dollars, in other words, its price.</p>

<p>When making the purchase, first the <code>purchaseAmount</code> <strong>is rounded to the nearest multiple of 10</strong>. Let us call this value <code>roundedAmount</code>. Then, <code>roundedAmount</code> dollars are removed from your bank account.</p>

<p>Return an integer denoting your final bank account balance after this purchase.</p>

<p><strong>Notes:</strong></p>

<ul>
    <li>0 is considered to be a multiple of 10 in this problem.</li>
    <li>When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> purchaseAmount = 9
<strong>Output:</strong> 90
<strong>Explanation:</strong> The nearest multiple of 10 to 9 is 10. So your account balance becomes 100 - 10 = 90.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> purchaseAmount = 15
<strong>Output:</strong> 80
<strong>Explanation:</strong> The nearest multiple of 10 to 15 is 20. So your account balance becomes 100 - 20 = 80.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> purchaseAmount = 10
<strong>Output:</strong> 90
<strong>Explanation:</strong> 10 is a multiple of 10 itself. So your account balance becomes 100 - 10 = 90.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>0 &lt;= purchaseAmount &lt;= 100</code></li>
</ul>

<!-- description:end -->

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> Round the purchase amount manually by checking all possible multiples of 10.

#### 🔍 Algorithm

```pseudo
function accountBalanceAfterPurchase(purchaseAmount):
    for i in range 0 to 100 step 10:
    if abs(purchaseAmount - i) is minimal:
            roundedAmount = i
    finalBalance = 100 - roundedAmount
    return finalBalance

```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int solutionBruteForce(int purchaseAmount) {
        int closest = 0;
        int minDiff = 100;
        for (int i = 0; i <= 100; i += 10) {
            if (abs(purchaseAmount - i) < minDiff) {
                minDiff = abs(purchaseAmount - i);
                closest = i;
            }
        }
        return 100 - closest;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Use arithmetic rounding instead of iterating over all multiples of 10.

#### 🔍 Algorithm

```pseudo
function accountBalanceAfterPurchase(purchaseAmount):
    roundedAmount = ((purchaseAmount + 5) / 10) * 10
    finalBalance = 100 - roundedAmount
    return finalBalance
```

#### 💻 Implementation

```cpp
// Optimized approach with arithmetic

class Solution {
public:
    int solutionOptimized(int purchaseAmount) {
        int roundedAmount = ((purchaseAmount + 5) / 10) * 10;
        return 100 - roundedAmount;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Elegant one-liner using arithmetic, clean and readable.

#### 🔍 Algorithm

```pseudo
function accountBalanceAfterPurchase(purchaseAmount):
    return 100 - ((purchaseAmount + 5) / 10 * 10)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int solutionOptimal(int purchaseAmount) {
        return 100 - ((purchaseAmount + 5) / 10 * 10);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                         | Cons                    |
| -------------- | --------------- | ---------------- | ---------------------------- | ----------------------- |
| 🥉 Brute Force | O(10)           | O(1)             | Simple, easy to understand   | Inefficient loop        |
| 🥈 Optimized   | O(1)            | O(1)             | Fast, no loop                | Slightly less intuitive |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant, clean, minimal code | None                    |

## 🎯 Why This is Optimal?

    - Avoids unnecessary loops.
    - Uses simple arithmetic for constant-time solution.
    - Clean and readable for maintenance.

### 🔑 Key Insights

| #   | Insight                                      |
| --- | -------------------------------------------- |
| 1   | Purchase amount always rounded to nearest 10 |
| 2   | 5 is rounded upward                          |
| 3   | Final balance = 100 - roundedAmount          |

### 💭 Common Mistakes to Avoid

| #   | Mistake                  | Description                      | How to Avoid                 | Example |
| --- | ------------------------ | -------------------------------- | ---------------------------- | ------- |
| 1   | Forgetting to round 5 up | 5, 15, 25 must round to next 10  | Always add 5 before division | 15 → 20 |
| 2   | Using floating point     | Could introduce precision errors | Use integer arithmetic       | N/A     |
| 3   | Ignoring 0 multiple case | 0 is considered multiple of 10   | Handle 0 correctly           | 0 → 0   |

### 🐛 Implementation Mistakes

| #   | Mistake              | Description                 | How to Avoid                   | Example         |
| --- | -------------------- | --------------------------- | ------------------------------ | --------------- |
| 1   | Off-by-one error     | Incorrect rounding          | Use `(purchaseAmount + 5)/10`  | 14 → 10 (wrong) |
| 2   | Forget subtraction   | Forget to subtract from 100 | Always compute `100 - rounded` | 15 → 100?       |
| 3   | Using float division | Causes precision issues     | Use integer division           | 15/10=1?        |

### 💭 Logical Thinking Mistakes

| #   | Mistake                   | Description                 | How to Avoid                | Prevention      |
| --- | ------------------------- | --------------------------- | --------------------------- | --------------- |
| 1   | Misunderstanding rounding | Thinking 5 rounds down      | Remember 5 always rounds up | Test edge cases |
| 2   | Forget initial balance    | Ignoring starting 100       | Always subtract from 100    | N/A             |
| 3   | Mixing float and int math | Could lead to wrong results | Stick to integer arithmetic | N/A             |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                     |
| --- | ------------------- | ------------------------------- |
| 1   | Arithmetic rounding | Round to nearest multiple of 10 |
| 2   | Greedy              | Always take closest multiple    |
| 3   | Constant time       | Compute directly without loops  |

### 🔄 Follow-up Questions

| #   | Question                                       | Answer / Approach                   |
| --- | ---------------------------------------------- | ----------------------------------- |
| 1   | What if balance ≠ 100?                         | Subtract roundedAmount from balance |
| 2   | What if purchaseAmount > 100?                  | Apply same rounding logic           |
| 3   | How to handle multiple purchases sequentially? | Update balance each time            |

---

<div align="center">

**🎯 Problem 2806 Completed!**

_Happy Coding! 🚀_

</div>
