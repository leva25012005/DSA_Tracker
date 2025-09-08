<div align="center">

# 🧠 [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201281-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                             |
| **Acceptance Rate** | `86.6%`                                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                      |

## Description

<!-- description:start -->

Given an integer number <code>n</code>, return the difference between the product of its digits and the sum of its digits.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 234
<strong>Output:</strong> 15 
<b>Explanation:</b> 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4421
<strong>Output:</strong> 21
<b>Explanation: 
</b>Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
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

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Quora** 🔥 87.2%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Convert to String (Brute Force)

#### 📝 Intuition

> The simplest way is to convert the number into a string, then iterate over each character, convert it back to integer, and compute product and sum separately.

#### 🔍 Algorithm

```pseudo
function subtractProductAndSum(n):
    convert n to string s
    product = 1
    sum = 0
    for each character c in s:
        digit = int(c)
        product = product * digit
        sum = sum + digit
    return product - sum
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int subtractProductAndSum(int n) {
        string s = to_string(n);
        int product = 1, sum = 0;
        for (char c : s) {
            int digit = c - '0';
            product *= digit;
            sum += digit;
        }
        return product - sum;
    }
};
```

### 🥈 Approach 2: Modulo / Division (Optimized Solution)

#### 📝 Intuition

> Instead of converting to string, directly extract digits using modulo (% 10) and integer division (/ 10). This avoids extra space and is more efficient.

#### 🔍 Algorithm

```pseudo
function subtractProductAndSum(n):
    product = 1
    sum = 0
    while n > 0:
        digit = n % 10
        product = product * digit
        sum = sum + digit
        n = n // 10
    return product - sum
```

#### 💻 Implementation

```cpp
// Optimized mathematical approach
class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1, sum = 0;
        while (n > 0) {
            int digit = n % 10;
            product *= digit;
            sum += digit;
            n /= 10;
        }
        return product - sum;
    }
};
```

### 🥇 Approach 3: : Functional Style with STL (accumulate / lambda) (Optimal Solution ⭐)

#### 📝 Intuition

> We can take advantage of STL algorithms such as accumulate and lambda functions. First, extract digits into a vector, then apply functional operations for sum and product.

#### 🔍 Algorithm

```pseudo
function subtractProductAndSum(n):
    extract digits into vector
    product = accumulate with multiplication lambda
    sum = accumulate with addition lambda
    return product - sum
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
// Functional style using STL accumulate
#include <numeric>

class Solution {
public:
    int subtractProductAndSum(int n) {
        vector<int> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        int product = accumulate(digits.begin(), digits.end(), 1, multiplies<int>());
        int sum = accumulate(digits.begin(), digits.end(), 0, plus<int>());
        return product - sum;
    }
};
```

### 🏆 Approach 4: Precomputation / Lookup Table

#### 📝 Intuition

> If the input range is small (e.g., only a few digits), we can precompute results for all possible numbers and use a lookup table for O(1) query.
> (This is not practical for large n, but good for theoretical completeness.)

#### 🔍 Algorithm

```pseudo
precompute table[0..9999] where each entry = product(digits) - sum(digits)
function subtractProductAndSum(n):
    return table[n]
```

#### 💻 Implementation

```cpp
// Precomputation approach (for small ranges)

class Solution {
    vector<int> table;
public:
    Solution() {
        table.resize(10000);
        for (int i = 0; i < 10000; i++) {
            int x = i, product = 1, sum = 0;
            if (x == 0) { table[i] = 0; continue; }
            while (x > 0) {
                int d = x % 10;
                product *= d;
                sum += d;
                x /= 10;
            }
            table[i] = product - sum;
        }
    }

    int subtractProductAndSum(int n) {
        return (n < 10000) ? table[n] : -1; // valid only for precomputed range
    }
};
```

## 📊 Comparison of Approaches

| Approach                         | Time Complexity | Space Complexity | Pros                                | Cons                                  |
| -------------------------------- | --------------- | ---------------- | ----------------------------------- | ------------------------------------- |
| 🥉 Brute Force (String)          | O(d)            | O(d)             | Very simple, easy to implement      | Extra space, slower due to conversion |
| 🥈 Optimized (Modulo / Division) | O(d)            | O(1)             | Fast, minimal space, clean          | Slightly more code than brute force   |
| 🥇 Functional (STL / accumulate) | O(d)            | O(d)             | Elegant, concise with STL utilities | Requires storing digits in vector     |
| 🏆 Precomputation / Lookup Table | O(1) query      | O(maxN)          | Instant query after precompute      | Not scalable for large `n` (memory)   |

## 🎯 Why This is Optimal?

    - The Modulo/Division approach is the cleanest and most efficient in terms of time + space.
    - The Functional STL approach is elegant but has extra space overhead.
    - Precomputation only makes sense for bounded inputs.
    - Overall, Approach 2 is optimal for competitive programming, while Approach 3 is best for readability/elegance.

### 🔑 Key Insights

| #   | Insight                                             |
| --- | --------------------------------------------------- |
| 1   | Always consider both product and sum simultaneously |
| 2   | String conversion is intuitive but not efficient    |
| 3   | STL accumulate makes code elegant and concise       |

### 💭 Common Mistakes to Avoid

| #   | Mistake             | Description                                  | How to Avoid                                    | Example                |
| --- | ------------------- | -------------------------------------------- | ----------------------------------------------- | ---------------------- |
| 1   | Overflow            | Product can grow large                       | Use `int` carefully (but here `n ≤ 10^5`, safe) | n = 99999              |
| 2   | Forget leading zero | String conversion may add unnecessary checks | Handle correctly                                | "0123" invalid         |
| 3   | Empty digits        | Not handling n=0 properly                    | Add base case                                   | n=0 → product=0, sum=0 |

### 🐛 Implementation Mistakes

| #   | Mistake              | Description              | How to Avoid       | Example               |
| --- | -------------------- | ------------------------ | ------------------ | --------------------- |
| 1   | Wrong initialization | product initialized as 0 | Start product = 1  | product=0 → always 0  |
| 2   | Forget n/=10         | Infinite loop            | Always reduce n    | while loop never ends |
| 3   | Wrong modulo         | Using `/` instead of `%` | Correctly separate | digit = n % 10        |

### 💭 Logical Thinking Mistakes

| #   | Mistake                     | Description               | How to Avoid                  | Prevention              |
| --- | --------------------------- | ------------------------- | ----------------------------- | ----------------------- |
| 1   | Confusing subtraction order | Using sum - product       | Always compute product - sum  | Check with examples     |
| 2   | Assuming negative digits    | Digits always ≥ 0         | Don’t overcomplicate          | Constraints             |
| 3   | Over-optimizing             | Precomputation for huge n | Only use where range is small | Think about constraints |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                          |
| --- | ------------------- | ------------------------------------ |
| 1   | Digit Extraction    | Getting digits via % and //          |
| 2   | Functional Reduce   | Using STL accumulate for sum/product |
| 3   | Precomputation      | Speed-up queries with lookup tables  |

### 🔄 Follow-up Questions

| #   | Question                                     | Answer / Approach                                          |
| --- | -------------------------------------------- | ---------------------------------------------------------- |
| 1   | Can we handle very large `n` (e.g., 10^18)?  | Yes, still works with modulo approach but use `long long`. |
| 2   | Can we extend to "sum of squares of digits"? | Yes, just adjust computation inside loop.                  |

---

<div align="center">

**🎯 Problem 1281 Completed!**

_Happy Coding! 🚀_

</div>
