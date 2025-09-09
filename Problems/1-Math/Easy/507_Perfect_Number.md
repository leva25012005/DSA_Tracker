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

## Description

<!-- description:start -->

<p>A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank"><strong>perfect number</strong></a> is a <strong>positive integer</strong> that is equal to the sum of its <strong>positive divisors</strong>, excluding the number itself. A <strong>divisor</strong> of an integer <code>x</code> is an integer that can divide <code>x</code> evenly.</p>

<p>Given an integer <code>n</code>, return <code>true</code><em> if </em><code>n</code><em> is a perfect number, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 28
<strong>Output:</strong> true
<strong>Explanation:</strong> 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 7
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `06/09/2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `06/09/2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
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

> The simplest idea is to iterate over all numbers from `1 → num-1`, check if they are divisors of `num`. Then sum all divisors and compare with `num`.

#### 🔍 Algorithm

```pseudo
function checkPerfectNumber(num):
    if num <= 1:
        return False
    total = 0
    for i from 1 to num-1:
        if num % i == 0:
            total += i
    return total == num
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
            if (num % i == 0) sum += i;
        }
        return sum == num;
    }
};
```

### 🥈 Approach 2: Optimized Solution with Square Root

#### 📝 Intuition

> Instead of going through the entire 1 → num-1, we only need to go through √num.
> Each divisor i found will have a divisor num / i.
> This reduces the time significantly.

#### 🔍 Algorithm

```pseudo
function checkPerfectNumber(num):
    if num <= 1:
        return False
    total = 1
    for i from 2 to sqrt(num):
        if num % i == 0:
            total += i
            if i != num / i:
                total += num / i
    return total == num
```

#### 💻 Implementation

```cpp
// Optimized approach with sqrt(num)
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;
        int sum = 1;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                sum += i;
                if (i != num / i) sum += num / i;
            }
        }
        return sum == num;
    }
};
```

### 🥇 Approach 3: Euler’s Formula (Mersenne Primes)

#### 📝 Intuition

> Euler proved that even perfect numbers have the form:
>
> $$
> 2^{p-1}\bigl(2^{p}-1\bigr)
> $$
>
> where \(2^{p}-1\) is a Mersenne prime.
> We only need to generate perfect numbers from the small list \(p\): \(2, 3, 5, 7, 13, 17, 19, 31\)

#### 🔍 Algorithm

```pseudo
function checkPerfectNumber(num):
    mersenne_primes = [2,3,5,7,13,17,19,31]
    for p in mersenne_primes:
        perfect = (2^(p-1)) * (2^p - 1)
        if perfect == num:
            return True
    return False
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
// Euler formula using Mersenne primes
class Solution {
public:
    bool checkPerfectNumber(int num) {
        vector<int> primes = {2,3,5,7,13,17,19,31};
        for (int p : primes) {
            long long perfect = ((1LL << (p - 1)) * ((1LL << p) - 1));
            if (perfect == num) return true;
        }
        return false;
    }
};
```

### ⭐ Approach 4: Lookup Known Perfect Numbers

#### 📝 Intuition

> In the limit num ≤ 1e8, there are only 5 perfect numbers: {6, 28, 496, 8128, 33550336}.
> We only need to check membership.

#### 🔍 Algorithm

```pseudo
function checkPerfectNumber(num):
    return num in {6,28,496,8128,33550336}
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool checkPerfectNumber(int num) {
        static unordered_set<int> perfects = {6, 28, 496, 8128, 33550336};
        return perfects.count(num) > 0;
    }
};
```

## ⭐ Approach 4: Lookup Known Perfect Numbers

#### 📝 Intuition

> Using the sieve-like method:
> Create an array div_sum[] to store the sum of divisors for each number.
> For each i, add i to all multiples j.
> Finally check that div_sum[num] == num..

#### 🔍 Algorithm

```pseudo
function checkPerfectNumber(num):
    if num <= 1: return False
    div_sum = array of size num+1, initialized with 1
    div_sum[0] = 0
    for i from 2 to num/2:
        for j from 2*i to num step i:
            div_sum[j] += i
    return div_sum[num] == num
```

#### 💻 Implementation

```cpp
// Sieve approach (not optimal for single query but useful if many queries)
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;
        vector<int> div_sum(num + 1, 1);
        div_sum[0] = 0;
        for (int i = 2; i <= num / 2; i++) {
            for (int j = 2 * i; j <= num; j += i) {
                div_sum[j] += i;
            }
        }
        return div_sum[num] == num;
    }
};
```

## 📊 Comparison of Approaches

| Approach             | Time Complexity | Space Complexity | Pros                                                     | Cons                                     |
| -------------------- | --------------- | ---------------- | -------------------------------------------------------- | ---------------------------------------- |
| 🥉 Brute Force       | O(n)            | O(1)             | Easy to understand                                       | Too slow for `num ~ 1e8`                 |
| 🥈 Square Root       | O(√n)           | O(1)             | Optimal, fast enough for `1e8`                           | Be careful to avoid double count         |
| 🥇 Euler Formula     | O(log n)        | O(1)             | Based on mathematics, generates all even perfect numbers | Need to know the list of Mersenne primes |
| ⭐ Lookup Known      | O(1)            | O(1)             | Fastest, clean                                           | Only applies to `num ≤ 1e8`              |
| 🔧 Sieve Divisor Sum | O(n log n)      | O(n)             | Can check multiple numbers at once                       | Not optimized for 1 number               |

## 🎯 Why This is Optimal?

    - Euler Formula and Lookup allow to transform the perfect number checking problem from O(n) → O(1).
    - This is a clean solution, taking advantage of mathematical knowledge and suitable for the problem's constraints.

### 🔑 Key Insights

| #   | Insight                                                               |
| --- | --------------------------------------------------------------------- |
| 1   | Every divisor smaller than √n has a larger divisor associated with it |
| 2   | Perfect numbers are extremely rare                                    |
| 3   | All even perfect numbers have the form Euler formula                  |
| 4   | With constraint, there are only 5 numbers to check                    |

### 💭 Common Mistakes to Avoid

| #   | Mistake                                 | Description                 | How to Avoid           | Example                  |
| --- | --------------------------------------- | --------------------------- | ---------------------- | ------------------------ |
| 1   | Add `num` to total                      | Must remove itself          | Add only if `i != num` | num=28                   |
| 2   | Do not check `num <= 1`                 | 0,1 is not a perfect number | Add condition          | if (num<=1) return false |
| 3   | Double count divisors when `i*i == num` | Add only once               | if (i != num/i)        | num=16                   |

### 🐛 Implementation Mistakes

| #   | Mistake                         | Description           | How to Avoid  | Example  |
| --- | ------------------------------- | --------------------- | ------------- | -------- |
| 1   | Initial sum = 0                 | 1 is always a divisor | Start sum=1   | num=28   |
| 2   | Overflow when using bit shift   | With Euler formula    | Use long long | num=2^31 |
| 3   | Browse i\*i < num instead of <= | Missing divisors      | Use `<=`      | num=16   |

### 💭 Logical Thinking Mistakes

| #   | Mistake                             | Description        | How to Avoid           | Prevention            |
| --- | ----------------------------------- | ------------------ | ---------------------- | --------------------- |
| 1   | Thinking perfect numbers are common | Actually very rare | Lookup list            | Focus on constraint   |
| 2   | Forgetting Euler formula            | Not using math     | Learning Euler formula | Fast and clean code   |
| 3   | Using brute force with large num    | Too slow           | Sqrt/Euler/Lookup      | Always optimize first |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique      | Application                       |
| --- | ------------------------ | --------------------------------- |
| 1   | Brute Force              | Scanning all divisors             |
| 2   | Square Root Optimization | Pairs of divisors                 |
| 3   | Mathematical Formula     | Euler’s theorem                   |
| 4   | Precomputation           | Lookup table                      |
| 5   | Sieve Technique          | Sum divisors for multiple numbers |

### 🔄 Follow-up Questions

| #   | Question                                   | Answer / Approach                                            |
| --- | ------------------------------------------ | ------------------------------------------------------------ |
| 1   | Are there odd perfect numbers?             | Not found yet, still open problem                            |
| 2   | Are there infinitely many perfect numbers? | Depends on whether there are infinitely many Mersenne primes |
| 3   | What if num > 1e8?                         | Use Euler formula or sqrt optimization                       |

---

<div align="center">

**🎯 Problem 507 Completed!**

_Happy Coding! 🚀_

</div>
```
