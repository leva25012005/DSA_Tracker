<div align="center">

# 🧠 [507. Perfect Number](https://leetcode.com/problems/perfect-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20507-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/perfect-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `45.7%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/perfect-number/)  |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `06/09/2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `06/09/2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                       | Difficulty  | Relationship  |
| ----------------------------------------------------------------------------- | ----------- | ------------- |
| [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | 🟢 **Easy** | Similar logic |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Grammarly** ⭐ 76.5%

### 📈 Regular Frequency (40-59%)

- **Accenture** 📈 48.3%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> The simplest idea is to iterate through all numbers from 1 to n-1, check if the number is divisible by n, if so add it to the sum. Finally compare the sum with n.

#### 🔍 Algorithm

```pseudo
function isPerfect(n):
    if n <= 1:
        return false
    sum = 0
    for i from 1 to n-1:
        if n % i == 0:
            sum += i
    return sum == n
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;
        int sum = 0;
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                sum += i;
            }
        }
        return sum == num;
    }
};
```

### 🥈 Approach 2: Optimized Solution with √n Divisors

#### 📝 Intuition

> MNo need to check up to n-1. If i is a divisor of n, then n / i is also a divisor. Just iterate i from 1 → √n, adding both i and n/i. Remember to leave n out of the sum.

#### 🔍 Algorithm

```pseudo
function isPerfect(n):
    if n <= 1:
        return false
    sum = 1
    for i from 2 to sqrt(n):
        if n % i == 0:
            sum += i
            if i != n / i:
                sum += n / i
    return sum == n
```

#### 💻 Implementation

```cpp
// Optimized approach using sqrt
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;
        int sum = 1; // 1 is always a divisor
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                sum += i;
                if (i != num / i) {
                    sum += num / i;
                }
            }
        }
        return sum == num;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> According to Euclid–Euler, every even perfect number has the form:
> $$2^{p-1} \times (2^p - 1)$$
> trong đó (2^p - 1) là số nguyên tố Mersenne.
> Trong giới hạn n <= 10^8, chỉ có vài số hoàn hảo: 6, 28, 496, 8128, 33550336.

#### 🔍 Algorithm

```pseudo
function isPerfect(n):
    known_perfect_numbers = {6, 28, 496, 8128, 33550336}
    return n in known_perfect_numbers
```

#### 💻 Implementation

```cpp
// Most optimal approach (using mathematical property)
class Solution {
public:
    bool checkPerfectNumber(int num) {
        static unordered_set<int> perfects = {6, 28, 496, 8128, 33550336};
        return perfects.count(num) > 0;
    }
};

```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                | Cons                             |
| -------------- | --------------- | ---------------- | ------------------- | -------------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Dễ hiểu, dễ cài     | Quá chậm với n lớn               |
| 🥈 Optimized   | O(√n)           | O(1)             | Nhanh hơn nhiều     | Vẫn phải duyệt                   |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Nhanh nhất, elegant | Phụ thuộc vào tính chất toán học |

## 🎯 Why This is Optimal?

    - Brute force is too slow.
    - Optimized (√n) is enough for the constraint.
    - Optimal uses the Euclid–Euler theorem for O(1) speed and very clean code.

### 🔑 Key Insights

| #   | Insight                                                             |
| --- | ------------------------------------------------------------------- |
| 1   | Perfect numbers are closely related to **Mersenne primes**          |
| 2   | Only need to check up to `√n` instead of `n-1`                      |
| 3   | There is a practical limit for even perfect numbers                 |
| 4   | The problem essentially tests membership in a finite set of numbers |

### 💭 Common Mistakes to Avoid

| #   | Mistake                           | Description                             | How to Avoid                         | Example                       |
| --- | --------------------------------- | --------------------------------------- | ------------------------------------ | ----------------------------- |
| 1   | Forget to remove `n` from the sum | Some people add `n` → always wrong      | Remember to only add **divisor < n** | With n=28, the sum will be 56 |
| 2   | Overflow                          | When adding divisors, it can exceed int | Use `long long` if num is large      | num > 10^8                    |
| 3   | Start from `0`                    | Divisor checks from 1, not 0            | Be careful when writing for-loop     | `i=0` causes division by 0    |

### 🐛 Implementation Mistakes

| #   | Mistake               | Description                        | How to Avoid                | Example |
| --- | --------------------- | ---------------------------------- | --------------------------- | ------- |
| 1   | Forget to add `1`     | Every number > 1 has a divisor `1` | Initialize sum=1            |         |
| 2   | Count double divisors | With `i == n/i` add 2 times        | Check `if(i != n/i)`        | n=16    |
| 3   | Do not check num <= 1 | 1 is not a perfect number          | Return false from the start | num=1   |

### 💭 Logical Thinking Mistakes

| #   | Mistake                        | Description                        | How to Avoid                  | Prevention                 |
| --- | ------------------------------ | ---------------------------------- | ----------------------------- | -------------------------- |
| 1   | Think of perfect numbers a lot | In a small range of only 5 numbers | Know the limit in advance     | Use Euclid–Euler           |
| 2   | Confused with prime            | Prime ≠ Perfect                    | Read the definition carefully | 7 is prime but not perfect |
| 3   | Incorrect comparison           | Sum of divisors can be > n         | Just return `sum==n`          | Do not use ≥               |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                    |
| --- | ------------------- | ------------------------------ |
| 1   | Divisor Pairing     | Reduce the loop from n → √n    |
| 2   | Math Theorem        | Euclid–Euler theorem           |
| 3   | Precomputation      | Store a set of perfect numbers |

### 🔄 Follow-up Questions

| #   | Question                            | Answer / Approach                                    |
| --- | ----------------------------------- | ---------------------------------------------------- |
| 1   | Are there odd perfect numbers?      | Unknown, still an open problem in mathematics        |
| 2   | What if n > 10^8?                   | Use optimized √n because hardcoded set is not enough |
| 3   | Are there infinite perfect numbers? | Still unknown, depends on Mersenne primes            |

---

<div align="center">

**🎯 Problem 507 Completed!**

_Happy Coding! 🚀_

</div>
