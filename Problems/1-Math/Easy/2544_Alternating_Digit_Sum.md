<div align="center">

# 🧠 [2544. Alternating Digit Sum](https://leetcode.com/problems/alternating-digit-sum/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202544-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/alternating-digit-sum/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                              |
| **Acceptance Rate** | `68.5%`                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/alternating-digit-sum/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)       |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>n</code>. Each digit of <code>n</code> has a sign according to the following rules:</p>

<ul>
	<li>The <strong>most significant digit</strong> is assigned a <strong>positive</strong> sign.</li>
	<li>Each other digit has an opposite sign to its adjacent digits.</li>
</ul>

<p>Return <em>the sum of all digits with their corresponding sign</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 521
<strong>Output:</strong> 4
<strong>Explanation:</strong> (+5) + (-2) + (+1) = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 111
<strong>Output:</strong> 1
<strong>Explanation:</strong> (+1) + (-1) + (+1) = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 886996
<strong>Output:</strong> 0
<strong>Explanation:</strong> (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<style type="text/css">.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; 
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
</style>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `08-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `08-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                           | Difficulty  | Relationship    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------- |
| [Add Digits](https://leetcode.com/problems/add-digits/)                                                                                           | 🟢 **Easy** | Similar logic   |
| [Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) | 🟢 **Easy** | Related concept |
| [Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array/)                                                 | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **eBay** 🔥 95.1%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: String Conversion + Alternating Index (Brute Force)

#### 📝 Intuition

> The simplest way is to convert the number `n` into a string, iterate through each digit from left to right, and apply `+` for even indices and `-` for odd indices.

#### 🔍 Algorithm

```pseudo
function alternateDigitSum(n):
    convert n to string s
    initialize result = 0
    for each index i and digit d in s:
        if i is even:
            result += d
        else:
            result -= d
    return result
```

#### 💻 Implementation

```cpp
// Brute force approach: String conversion
class Solution {
public:
    int alternateDigitSum(int n) {
        string s = to_string(n);
        int result = 0;
        for (int i = 0; i < s.size(); i++) {
            int digit = s[i] - '0';
            if (i % 2 == 0) result += digit;
            else result -= digit;
        }
        return result;
    }
};

```

### 🥈 Approach 2: Math Simulation (Extract Digits Right-to-Left) (Optimized Solution)

#### 📝 Intuition

> Instead of converting to string, extract digits using % 10 and / 10.
> We need to know the total number of digits to start with the correct sign (+ for the most significant digit).

#### 🔍 Algorithm

```pseudo
function alternateDigitSum(n):
    count digits of n -> len
    result = 0
    sign = +1 if len is odd else -1
    while n > 0:
        digit = n % 10
        result += sign * digit
        sign *= -1
        n = n / 10
    return result

```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
// Optimized: Pure math digit extraction

class Solution {
public:
    int alternateDigitSum(int n) {
        int len = to_string(n).size();
        int result = 0;
        int sign = (len % 2 == 0 ? -1 : 1);
        while (n > 0) {
            int digit = n % 10;
            result += sign * digit;
            sign *= -1;
            n /= 10;
        }
        return result;
    }
};

```

### 🥇 Approach 3: Toggle Sign Variable (Optimal Solution ⭐)

#### 📝 Intuition

> We can avoid checking indices. Just maintain a sign variable that toggles (sign \*= -1) after each digit. This reduces condition checks and makes code cleaner.

#### 🔍 Algorithm

```pseudo
function alternateDigitSum(n):
    convert n to string s
    initialize result = 0, sign = +1
    for each digit d in s:
        result += sign * d
        sign *= -1
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution: sign toggling
class Solution {
public:
    int alternateDigitSum(int n) {
        string s = to_string(n);
        int result = 0, sign = 1;
        for (char c : s) {
            int digit = c - '0';
            result += sign * digit;
            sign *= -1;
        }
        return result;
    }
};
```

### ⚡ Approach 4: One-Liner Trick (Functional Style)

#### 📝 Intuition

> Using high-level constructs (like enumerate in Python), we can compress the solution into a one-liner.
> In C++, we can mimic this with simple loop logic but the concept is for readability.

#### 🔍 Algorithm

```pseudo
function alternateDigitSum(n):
    sum over all digits: (1 if index even else -1) * digit
```

#### 💻 Implementation

```cpp
// One-liner inspired approach
class Solution {
public:
    int alternateDigitSum(int n) {
        string s = to_string(n);
        int result = 0;
        for (int i = 0; i < s.size(); i++) {
            result += (i % 2 == 0 ? 1 : -1) * (s[i] - '0');
        }
        return result;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                           | Cons                           |
| -------------- | --------------- | ---------------- | ------------------------------ | ------------------------------ |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple, intuitive         | Extra string conversion        |
| 🥈 Optimized   | O(d)            | O(1)             | Pure math, no string overhead  | Slightly tricky with sign init |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Clean, elegant, easy to follow | Requires toggle variable       |
| ⚡ One-Liner   | O(d)            | O(d)             | Very concise, Pythonic style   | Less readable in C++           |

## 🎯 Why This is Optimal?

    - Brute force is simple but less efficient in space.
    - Pure math avoids string but needs digit count handling.
    - Sign toggle is both clean and efficient.
    - One-liner is concise but more stylistic.
    - Optimal = Toggle Sign, since it balances readability and efficiency.

### 🔑 Key Insights

| #   | Insight                                                            |
| --- | ------------------------------------------------------------------ |
| 1   | Alternating signs can be tracked with a toggle variable            |
| 2   | Pure math avoids extra storage but requires digit length awareness |
| 3   | String-based approach is easiest to implement                      |

### 💭 Common Mistakes to Avoid

| #   | Mistake             | Description                                            | How to Avoid                                      | Example                                       |
| --- | ------------------- | ------------------------------------------------------ | ------------------------------------------------- | --------------------------------------------- |
| 1   | Wrong starting sign | Forget that the **most significant digit is always +** | Always initialize sign = +1 at the leftmost digit | Input `521` → if start with -1 → result wrong |
| 2   | Indexing error      | Using 0-based index incorrectly for sign               | Test with small cases                             | Input `11` → should return 0                  |
| 3   | Overflow worries    | Not relevant here since n ≤ 1e9                        | Understand constraints                            | Not needed in this problem                    |

### 🐛 Implementation Mistakes

| #   | Mistake                         | Description                                | How to Avoid               | Example                                 |
| --- | ------------------------------- | ------------------------------------------ | -------------------------- | --------------------------------------- |
| 1   | Forget to convert char to digit | Using `char` directly instead of `c - '0'` | Always subtract `'0'`      | `'5'` → 53 ASCII instead of 5           |
| 2   | Forget to toggle sign           | Sign remains same → wrong output           | Always do `sign *= -1`     | Input `521` → would give 8 instead of 4 |
| 3   | Using wrong variable scope      | Resetting `sign` inside loop               | Declare `sign` before loop | Code compiles but gives wrong answer    |

### 💭 Logical Thinking Mistakes

| #   | Mistake                            | Description                                | How to Avoid            | Prevention                   |
| --- | ---------------------------------- | ------------------------------------------ | ----------------------- | ---------------------------- |
| 1   | Assuming left-to-right with `% 10` | `% 10` gives rightmost digit, not leftmost | Count digits first      | Use string or pre-count      |
| 2   | Misinterpreting constraints        | Thinking n can be negative                 | Check input constraints | Ensure `1 <= n <= 1e9`       |
| 3   | Confusing toggle vs index          | Using both together redundantly            | Choose one approach     | Either use `i % 2` or `sign` |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique           | Application              |
| --- | ----------------------------- | ------------------------ |
| 1   | Alternating sign toggle       | To apply + / - on digits |
| 2   | Digit extraction with % and / | Pure math approach       |
| 3   | String conversion             | Easier digit handling    |

### 🔄 Follow-up Questions

| #   | Question                                                    | Answer / Approach                                  |
| --- | ----------------------------------------------------------- | -------------------------------------------------- |
| 1   | How to handle very large numbers beyond 32-bit?             | Use string-based approach to avoid overflow        |
| 2   | Can we do it without counting digits?                       | Yes → use toggle sign starting from leftmost digit |
| 3   | How to generalize to alternating by groups (e.g., + + - -)? | Extend toggle pattern with modulo cycle            |

---

<div align="center">

**🎯 Problem 2544 Completed!**

_Happy Coding! 🚀_

</div>
