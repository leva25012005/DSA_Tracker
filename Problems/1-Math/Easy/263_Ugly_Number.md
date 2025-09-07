<div align="center">

# 🧠 [263. Ugly Number](https://leetcode.com/problems/ugly-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20263-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/ugly-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `42.5%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/ugly-number/)     |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>An <strong>ugly number</strong> is a <em>positive</em> integer which does not have a prime factor other than 2, 3, and 5.</p>

<p>Given an integer <code>n</code>, return <code>true</code> <em>if</em> <code>n</code> <em>is an <strong>ugly number</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> 6 = 2 &times; 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 has no prime factors.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> 14 is not ugly since it includes the prime factor 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `06-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `06-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                         | Difficulty    | Relationship    |
| --------------------------------------------------------------- | ------------- | --------------- |
| [Happy Number](https://leetcode.com/problems/happy-number/)     | 🟢 **Easy**   | Similar logic   |
| [Count Primes](https://leetcode.com/problems/count-primes/)     | 🟡 **Medium** | Related concept |
| [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

📊 Low Frequency Companies

- **J.P. Morgan** 📊 36.3%

---

## 💡 Solutions

### 🥇 Approach 1a: : Iterative Division (Brute Force - Optimal Solution ⭐)

#### 📝 Intuition

> The simplest idea: Continuously divide number n by 2, 3, 5 if it is divisible. If there is 1 left at the end, it is an Ugly Number, but if there is another number, it is not.

#### 🔍 Algorithm

```pseudo
function isUgly(x):
    if n <= 0
        return false
    while n % 2 == 0
        n = n / 2
    while n % 3 == 0
        n = n / 3
    while n % 5 == 0
        n = n / 5
    return n == 1
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        return n == 1;
    }
};
```

### 🥇 Approach 1b: : Hardcoded Iterative (Compact Loop)

#### 📝 Intuition

> A more concise version of Approach 1: Run the loop while n % 2 == 0 || n % 3 == 0 || n % 5 == 0 then divide by the correct factor.

#### 🔍 Algorithm

```pseudo
function isUgly(x):
    if n <= 0 → return false
while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    if n % 2 == 0 → n = n / 2
    else if n % 3 == 0 → n = n / 3
    else → n = n / 5
return n == 1
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        while (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) {
            if (n % 2 == 0) n /= 2;
            else if (n % 3 == 0) n /= 3;
            else n /= 5;
        }
        return n == 1;
    }
};
```

### 🥈 Approach 2: Recursive Division (Optimized Solution)

#### 📝 Intuition

> If n == 1 → true. If divisible by 2, 3 or 5 then continue with n/2, n/3, n/5. Otherwise → false.

#### 🔍 Algorithm

```pseudo
function isUgly(x):
    if n == 1
        return true
    if n <= 0
        return false
    if n % 2 == 0
        return isUgly(n / 2)
    if n % 3 == 0
        return isUgly(n / 3)
    if n % 5 == 0
        return isUgly(n / 5)
    return false
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isUgly(int n) {
        if (n == 1) return true;
        if (n <= 0) return false;
        if (n % 2 == 0) return isUgly(n / 2);
        if (n % 3 == 0) return isUgly(n / 3);
        if (n % 5 == 0) return isUgly(n / 5);
        return false;
    }
};
```

### 🥉 Approach 3: Prime Factorization

#### 📝 Intuition

> Instead of just dividing 2,3,5 directly, we factorize n. If there are factors other than {2,3,5} → not Ugly.

#### 🔍 Algorithm

```pseudo
function isUgly(x):
    if n <= 0 → return false
    for p in [2..sqrt(n)]:
        while n % p == 0:
            if p not in {2,3,5} → return false
            n /= p
    if n > 1 and n not in {2,3,5} → return false
    return true
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        for (int p = 2; p * p <= n; p++) {
            while (n % p == 0) {
                if (p != 2 && p != 3 && p != 5) return false;
                n /= p;
            }
        }
        return n == 1 || n == 2 || n == 3 || n == 5;
    }
};
```

## 📊 Comparison of Approaches

| Approach               | Time Complexity | Space Complexity | Pros              | Cons                      |
| ---------------------- | --------------- | ---------------- | ----------------- | ------------------------- |
| 🥇 Iterative Division  | O(log n)        | O(1)             | Ngắn gọn, dễ hiểu | Lặp lại chia 3 vòng while |
| 🥈 Recursive Division  | O(log n)        | O(log n) (stack) | Elegant, dễ đọc   | Tốn stack, chậm hơn       |
| 🥉 Prime Factorization | O(√n)           | O(1)             | Toán học rõ ràng  | Chậm hơn, không cần thiết |
| 🥉 Hardcoded Iterative | O(log n)        | O(1)             | Code gọn          | Logic ít trực quan hơn    |

## 🎯 Why Iterative Division is Optimal?

    - Just divide by 2,3,5 until none remain.
    - Avoid overhead recursion, avoid prime factorization.
    - Time O(log n), Space O(1).

### 🔑 Key Insights

| #   | Insight                                                     |
| --- | ----------------------------------------------------------- |
| 1   | Ugly Number has only prime factors in {2,3,5}.              |
| 2   | Every Ugly Number can be reduced to 1 by dividing by 2,3,5. |
| 3   | Important edge cases: n <= 0 → false, n = 1 → true.         |
| 4   | No need to find all factors, just remove 2,3,5.             |

### 💭 Common Mistakes to Avoid

| #   | Mistake                      | Description                                                            | How to Avoid                             | Example |
| --- | ---------------------------- | ---------------------------------------------------------------------- | ---------------------------------------- | ------- |
| 1   | Forget to handle n <= 0      | Leads to incorrect output for negative n or 0                          | Always check `if (n <= 0) return false;` | n = -6  |
| 2   | Do not stop the loop         | Wrong while loop condition, infinite loop                              | Always decrease n in each step           | n = 7   |
| 3   | Confused with Ugly Number II | Question 264 generates Ugly numbers, different from question 263 check | Read the question carefully              | -       |

### 🐛 Implementation Mistakes

| #   | Mistake                            | Description                     | How to Avoid                  | Example |
| --- | ---------------------------------- | ------------------------------- | ----------------------------- | ------- |
| 1   | Use int overflow in precomputation | Multiply by 5 to exceed INT_MAX | Check `if (x*5 <= INT_MAX)`   | -       |
| 2   | Divide but do not update n         | Forget to reassign `n /= 2`     | Check carefully in while      | -       |
| 3   | Return false for n=1               | Some code returns false for n=1 | Especially handle case `n==1` | n=1     |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                        | Description                       | How to Avoid                          | Prevention   |
| --- | ---------------------------------------------- | --------------------------------- | ------------------------------------- | ------------ |
| 1   | Thinking that Ugly Number must have both 2,3,5 | In fact, only need subset {2,3,5} | Understanding “no other prime factor” | Test n=8     |
| 2   | Mistaking 1 for not Ugly                       | By definition, 1 is Ugly          | Always consider 1 as true             | Test n=1     |
| 3   | Compare with Prime Number                      | Ugly number != prime number       | Read definition                       | Test n=2,3,5 |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                            |
| --- | ------------------- | -------------------------------------- |
| 1   | Prime Factorization | Used to prove the Ugly property        |
| 2   | Division Reduction  | Continuously divide by 2,3,5 to reduce |
| 3   | Recursion           | Recursively divide to 1                |

### 🔄 Follow-up Questions

| #   | Question                            | Answer / Approach                                      |
| --- | ----------------------------------- | ------------------------------------------------------ |
| 1   | If we extend to Ugly Number II?     | Use DP or Min-Heap to generate Ugly numbers            |
| 2   | If we replace {2,3,5} with {a,b,c}? | Generalize by dividing by another set of prime factors |

---

<div align="center">

**🎯 Problem 263 Completed!**

_Happy Coding! 🚀_

</div>
