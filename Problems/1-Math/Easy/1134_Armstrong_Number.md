<div align="center">

# 🧠 [1134. Armstrong Number](https://leetcode.com/problems/armstrong-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201134-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/armstrong-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                         |
| **Acceptance Rate** | `77.9%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/armstrong-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <code>true</code> <em>if and only if it is an <strong>Armstrong number</strong></em>.</p>

<p>The <code>k</code>-digit number <code>n</code> is an Armstrong number if and only if the <code>k<sup>th</sup></code> power of each digit sums to <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 153
<strong>Output:</strong> true
<strong>Explanation:</strong> 153 is a 3-digit number, and 153 = 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 123
<strong>Output:</strong> false
<strong>Explanation:</strong> 123 is a 3-digit number, and 123 != 1<sup>3</sup> + 2<sup>3</sup> + 3<sup>3</sup> = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `07-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `07-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: String Conversion (Brute Force)

#### 📝 Intuition

> Convert the number to a string, so we can easily extract digits and count how many digits there are (`k`). Then, compute the sum of each digit raised to the power `k`.

#### 🔍 Algorithm

```pseudo
function isArmstrong(num):
    s = to_string(n)
    k = length(s)
    sum = 0
    for each digit d in s:
        sum += d^k
    return sum == n
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    bool isArmstrong(int n) {
        string s = to_string(n);
        int k = s.size();
        long long sum = 0;
        for (char c : s) {
            int digit = c - '0';
            sum += pow(digit, k);
        }
        return sum == n;
    }
};
```

### 🥈 Approach 2: Mathematical Digit Extraction (Optimized Solution)

#### 📝 Intuition

> Instead of converting to string, count digits using division. Then extract digits again and compute the sum of their powers.

#### 🔍 Algorithm

```pseudo
function isArmstrong(num):
    count = number_of_digits(n)
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit^count
        temp = temp / 10
    return sum == n
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    bool isArmstrong(int n) {
        int k = 0, temp = n;
        while (temp > 0) {
            k++;
            temp /= 10;
        }
        long long sum = 0;
        temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            sum += pow(digit, k);
            temp /= 10;
        }
        return sum == n;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Since n ≤ 10^8, k ≤ 9. We can precompute all powers of digits 0–9 up to the 9th power.
> This avoids repeated calls to pow, making it faster.

#### 🔍 Algorithm

```pseudo
function isArmstrong(num):
    precompute power[d][k] for d=0..9, k=1..9
    k = number_of_digits(n)
    sum = 0
    while n > 0:
        digit = n % 10
        sum += power[digit][k]
        n /= 10
    return sum == original

```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    bool isArmstrong(int n) {
        static int power[10][10] = {0};
        static bool initialized = false;
        if (!initialized) {
            for (int d = 0; d < 10; d++) {
                for (int k = 1; k <= 9; k++) {
                    power[d][k] = pow(d, k);
                }
            }
            initialized = true;
        }

        int k = 0, temp = n;
        while (temp > 0) {
            k++;
            temp /= 10;
        }

        long long sum = 0;
        temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            sum += power[digit][k];
            temp /= 10;
        }
        return sum == n;
    }
};
```

### 💡 Approach 5: Recursive Digit Power Sum

#### 📝 Intuition

> We can write a recursive function that processes one digit at a time and sums the digit powers.

#### 🔍 Algorithm

```pseudo
function digitPowerSum(num, k):
    if num == 0: return 0
    return (last_digit^k) + digitPowerSum(num/10, k)

function isArmstrong(n):
    k = number_of_digits(n)
    sum = digitPowerSum(n, k)
    return sum == n
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isArmstrong(int n) {
        int k = 0, temp = n;
        while (temp > 0) {
            k++;
            temp /= 10;
        }
        return n == digitPowerSum(n, k);
    }

    int digitPowerSum(int num, int k) {
        if (num == 0) return 0;
        int digit = num % 10;
        return pow(digit, k) + digitPowerSum(num / 10, k);
    }
};
```

### 💡 Approach 4: Library-Based (Direct pow for Each Digit)

#### 📝 Intuition

> A very concise approach: just use pow directly for each digit extraction without optimization.
> This is shorter but slightly less efficient.

#### 🔍 Algorithm

```pseudo
function isArmstrong(num):
    count = number_of_digits(n)
    sum = Σ (digit^count) for each digit of n
    return sum == n
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isArmstrong(int n) {
        int k = floor(log10(n)) + 1; // quick way to count digits
        long long sum = 0, temp = n;
        while (temp > 0) {
            sum += pow(temp % 10, k);
            temp /= 10;
        }
        return sum == n;
    }
};
```

## 📊 Comparison of Approaches

| Approach             | Time Complexity | Space Complexity        | Pros                               | Cons                   |
| -------------------- | --------------- | ----------------------- | ---------------------------------- | ---------------------- |
| 🥉 String Conversion | O(k)            | O(k)                    | Easy to implement                  | Extra space for string |
| 🥈 Digit Extraction  | O(k)            | O(1)                    | Clean, no extra memory             | Slightly longer code   |
| 🥇 Precompute Powers | O(k)            | O(1) (after precompute) | Very efficient, avoids `pow` calls | Needs setup table      |
| 💡 Library pow       | O(k)            | O(1)                    | Concise, short code                | Less efficient         |
| 💡 Recursive         | O(k)            | O(k)                    | Elegant recursion                  | Less practical         |

## 🎯 Why This is Optimal?

    - The Digit Extraction approach is the best balance:
        - Constant space
        - Clear logic
        - Efficient enough for constraints (n ≤ 10^8).
    - Precomputation is faster but overkill here.

### 🔑 Key Insights

| #   | Insight                                                                 |
| --- | ----------------------------------------------------------------------- |
| 1   | Armstrong number check only requires digit count and power sum.         |
| 2   | Max digit count is 9 for `n ≤ 10^8`.                                    |
| 3   | The `pow` function is fine here but can be avoided with precomputation. |

### 💭 Common Mistakes to Avoid

| #   | Mistake                               | Description                                       | How to Avoid                          | Example                        |
| --- | ------------------------------------- | ------------------------------------------------- | ------------------------------------- | ------------------------------ |
| 1   | Using floating-point `pow` carelessly | `pow` returns `double` → risk of precision issues | Cast to integer after pow             | `(int)pow(digit, k)`           |
| 2   | Forgetting to count digits first      | Using wrong `k` in calculations                   | Always count digits separately        | `153` → must use `k=3`         |
| 3   | Not handling single-digit numbers     | All 1–9 are Armstrong numbers                     | Special case is handled automatically | Input `7` should return `true` |

### 🐛 Implementation Mistakes

| #   | Mistake                                       | Description                                                                                                                  | How to Avoid                                                                                                                                                             | Example                                                                                                                       |
| --- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| 1   | Using floating-point `pow` and casting to int | `pow` returns a `double`; tiny floating errors can lead to incorrect integer results when cast (truncation/rounding issues). | Use an integer power function (fast integer exponent), or precompute powers in an integer table. If you must use `pow`, round the result before casting: `int(r + 0.5)`. | `pow(5,3)` should be `125`. In rare floating cases `pow` might produce `124.9999999` → casting to `int` yields `124` (wrong). |
| 2   | Integer overflow when summing powers          | Sum of digit^k can exceed 32-bit `int` (especially for k up to 9), causing overflow and wrong comparison.                    | Use 64-bit integer types (`long long`) for intermediate power and sum. Validate with worst-case upper bound.                                                             | For n with many 9s: sum ≈ 9 \* 9^9 = 3,486,784,401 > 2,147,483,647 → overflow if using `int`.                                 |
| 3   | Incorrect digit counting using floating math  | Using `floor(log10(n)) + 1` can be fragile due to floating-point precision or edge cases (and fails for `n=0`).              | Count digits by integer division (`while (temp > 0) { k++; temp /= 10; }`) or convert to string and use `.size()`. Handle `n==0` separately if needed.                   | For some floating-edge inputs `log10` may produce `2.9999999` for a 1000-like value leading to wrong k.                       |
| 4   | Recomputing `pow` repeatedly (inefficient)    | Calling `pow` for each digit inside loops causes repeated work and minor performance hit.                                    | Precompute `digit^k` for digits `0..9` (since k ≤ 9 here) and look up values during the sum.                                                                             | For k=9, precompute `power[d][9]` and use `power[digit][k]` instead of `pow(digit, k)` per digit.                             |
| 5   | Wrong type conversion / truncation            | Mixing `double` and `int` without explicit rounding or using incorrect casts leads to subtle bugs.                           | Keep all math in integer domain when possible; if converting from `double`, use `llround()` or add `0.5` before cast.                                                    | `int val = (int)pow(digit, k);` → prefer `long long val = llround(pow(digit,k));` or integer pow.                             |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                               | Description                                         | How to Avoid                        | Prevention            |
| --- | ----------------------------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------- |
| 1   | Assuming Armstrong means divisible                    | Confusing Armstrong with self-dividing numbers      | Carefully read problem statement    | Check with examples   |
| 2   | Mixing up digit powers with sum of squares            | Thinking "Armstrong = sum of squares"               | Re-check definition                 | Use example `153`     |
| 3   | Assuming large Armstrong numbers exist in input range | Very few Armstrong numbers exist, don’t brute force | Only check definition for given `n` | Just validate one `n` |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                              |
| --- | ------------------- | ---------------------------------------- |
| 1   | Modulo and Division | Extract digits without string conversion |
| 2   | Precomputation      | Store digit powers for efficiency        |
| 3   | Recursion           | Compute digit power sum elegantly        |

### 🔄 Follow-up Questions

| #   | Question                                        | Answer / Approach                                                                 |
| --- | ----------------------------------------------- | --------------------------------------------------------------------------------- |
| 1   | What if `n` is larger (e.g., up to 10^18)?      | Approach still works, but `k` increases. Use 64-bit integers.                     |
| 2   | Can we generate all Armstrong numbers in range? | Yes, iterate through range and apply check. There are very few Armstrong numbers. |
| 3   | Why are Armstrong numbers rare?                 | Because sum of digit powers grows much slower than number magnitude.              |

---

<div align="center">

**🎯 Problem 1134 Completed!**

_Happy Coding! 🚀_

</div>
