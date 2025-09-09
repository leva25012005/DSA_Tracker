<div align="center">

# 🧠 [2520. Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202520-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                              |
| **Acceptance Rate** | `85.9%`                                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                       |

## Description

<!-- description:start -->

<p>Given an integer <code>num</code>, return <em>the number of digits in <code>num</code> that divide </em><code>num</code>.</p>

<p>An integer <code>val</code> divides <code>nums</code> if <code>nums % val == 0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 7
<strong>Output:</strong> 1
<strong>Explanation:</strong> 7 divides itself, hence the answer is 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 121
<strong>Output:</strong> 2
<strong>Explanation:</strong> 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 1248
<strong>Output:</strong> 4
<strong>Explanation:</strong> 1248 is divisible by all of its digits, hence the answer is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
	<li><code>num</code> does not contain <code>0</code> as one of its digits.</li>
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

## 🔗 Related Problems

| Problem                                                                       | Difficulty  | Relationship    |
| ----------------------------------------------------------------------------- | ----------- | --------------- |
| [Happy Number](https://leetcode.com/problems/happy-number/)                   | 🟢 **Easy** | Similar logic   |
| [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

- **tcs** 📈 59.9%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> We can iterate through each digit of the number, check if it divides the number, and count such digits.

#### 🔍 Algorithm

```pseudo
function countDigits(num):
    count = 0
    original = num
    while num > 0:
        digit = num % 10
        if original % digit == 0:
            count += 1
        num = num / 10
    return count
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int countDigits(int num) {
        int count = 0, original = num;
        while (num > 0) {
            int digit = num % 10;
            if (original % digit == 0) count++;
            num /= 10;
        }
        return count;
    }
};
```

### 🥈 Approach 2: String Conversion (Optimized Solution)

#### 📝 Intuition

> Convert the number into a string, iterate through each character, convert back to digit, and check divisibility.
> This makes the code cleaner and avoids manual %// digit extraction.

#### 🔍 Algorithm

```pseudo
function countDigits(num):
    strNum = convert num to string
    count = 0
    for ch in strNum:
        digit = int(ch)
        if num % digit == 0:
            count += 1
    return count
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    int countDigits(int num) {
        string s = to_string(num);
        int count = 0;
        for (char c : s) {
            int digit = c - '0';
            if (num % digit == 0) count++;
        }
        return count;
    }
};
```

### 🥇 Approach 3: Mathematical + Early Exit (Optimal Solution ⭐)

#### 📝 Intuition

> Same as Approach 1, but we avoid redundant work:
>
> - If a digit occurs multiple times, each occurrence should be counted.
> - Since the constraint num ≤ 1e9 is small (≤ 10 digits), the brute force is already optimal.
> - Still, we can add early exit: if all digits are 1, result = number of digits.

#### 🔍 Algorithm

```pseudo
function countDigits(num):
    if all digits are 1:
        return number of digits
    count = 0
    original = num
    while num > 0:
        digit = num % 10
        if original % digit == 0:
            count += 1
        num = num // 10
    return count
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    int countDigits(int num) {
        int count = 0, original = num;
        bool allOne = true;
        int temp = num;
        while (temp > 0) {
            if (temp % 10 != 1) allOne = false;
            temp /= 10;
        }
        if (allOne) return to_string(num).size();

        while (num > 0) {
            int digit = num % 10;
            if (original % digit == 0) count++;
            num /= 10;
        }
        return count;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                | Cons                        |
| -------------- | --------------- | ---------------- | ------------------- | --------------------------- |
| 🥉 Brute Force | O(d)            | O(1)             | Straightforward     | Manual digit ops            |
| 🥈 String Conv | O(d)            | O(d)             | Cleaner code        | Extra space for string      |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Small optimizations | Same as brute in worst case |

## 🎯 Why This is Optimal?

    - The number has at most 10 digits, so O(d) is essentially O(1).
    - Extra optimizations don’t reduce complexity but may simplify certain cases.
    - The brute force itself is already optimal for the given constraints.

### 🔑 Key Insights

| #   | Insight                                                                |
| --- | ---------------------------------------------------------------------- |
| 1   | Each digit must be checked separately.                                 |
| 2   | If a digit occurs multiple times, it should be counted multiple times. |
| 3   | Constraints are small → O(d) is acceptable.                            |

### 💭 Common Mistakes to Avoid

| #   | Mistake                | Description                                  | How to Avoid                  | Example                      |
| --- | ---------------------- | -------------------------------------------- | ----------------------------- | ---------------------------- |
| 1   | Forget multiple digits | Not counting repeated digits                 | Always count each occurrence  | `121 → answer = 2, not 1`    |
| 2   | Division by zero       | If 0 digit existed, it would cause crash     | Problem guarantees no 0 digit | N/A                          |
| 3   | Wrong modulus          | Using `digit % num` instead of `num % digit` | Carefully check condition     | Should be `num % digit == 0` |

### 🐛 Implementation Mistakes

| #   | Mistake                                | Description                                                                                               | How to Avoid                                           | Example                                                       |
| --- | -------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------- |
| 1   | Division by zero                       | Using a digit value `0` as a divisor causes runtime error.                                                | Always check `digit != 0` before `num % digit`.        | `num = 101` → skip digit `0` when checking divisibility.      |
| 2   | Using the mutated variable for checks  | Extracting digits by modifying `num` and then using `num` for divisibility instead of the original value. | Store original value in `orig` and use `orig % digit`. | `while(num>0){ digit=num%10; if (num%digit==0)... }` (wrong). |
| 3   | Wrong char-to-int conversion           | When iterating string digits, forgetting to convert `'3'` to `3` results in wrong values.                 | Use `c - '0'` or `std::stoi(string(1,c))`.             | `sum += c;` instead of `sum += c - '0'`.                      |
| 4   | Off-by-one / loop boundary errors      | Miswriting loop condition or index causes skipping first/last digit.                                      | Test small examples and use clear loop invariants.     | Using `for(i=0;i<s.size()-1;i++)` and missing last digit.     |
| 5   | Wrong data type / overflow assumptions | Using too-small integer type for larger constraints (or mixing signed/unsigned).                          | Use `int64_t` / `long long` when constraints may grow. | If `num` could be `1e18`, `int` would overflow.               |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                       | Description                                                                                       | How to Avoid                                                           | Prevention                                                   |
| --- | --------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| 1   | Counting unique digits only                   | Counting each distinct digit once instead of each occurrence.                                     | Remember to count every occurrence separately.                         | `121` has two `1`s → answer `2`.                             |
| 2   | Confusing order of modulus                    | Using `digit % num` instead of `num % digit`.                                                     | Carefully read “val divides num” as `num % val == 0`.                  | Wrong: `digit % num == 0` is meaningless here.               |
| 3   | Overcomplicating with factorization           | Trying to find all divisors of `num` and compare to digits — unnecessary overhead.                | Directly test each digit; complexity ≤ number of digits.               | Avoid factoring `num` for this task.                         |
| 4   | Assuming presence/absence of zero incorrectly | Either assuming zeros will always be present or never present; both can be wrong across variants. | Always handle `0` digit explicitly (skip/divide check).                | If constraint changes (0 allowed), skip zero digits.         |
| 5   | Ignoring input constraints / sign             | Applying logic for negatives or other ranges without confirming constraints.                      | Verify constraints (here `1 <= num <= 1e9`) and handle sign if needed. | If negative allowed, use `abs(num)` for divisibility checks. |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique        | Application                                                                           |
| --- | -------------------------- | ------------------------------------------------------------------------------------- |
| 1   | Digit extraction (mod/div) | Extract each digit via `digit = n % 10; n /= 10` and test divisibility.               |
| 2   | String iteration           | Convert `num` to string and iterate characters when that simplifies code/readability. |
| 3   | Early skip / guard         | Skip digits equal to `0` immediately to avoid divide-by-zero.                         |
| 4   | Count occurrences          | If digit appears multiple times, count each occurrence separately.                    |
| 5   | Type safety                | Use appropriate integer types (`int64_t`) and avoid signed/unsigned mix-ups.          |

### 🔄 Follow-up Questions

| #   | Question                                   | Answer / Approach                               |
| --- | ------------------------------------------ | ----------------------------------------------- |
| 1   | What if `num` could contain 0?             | Need to skip 0 to avoid division by zero error. |
| 2   | What if `num` was very large (e.g., 1e18)? | Use `long long` in C++ to handle safely.        |
| 3   | Can we parallelize digit checks?           | Overkill for ≤10 digits, but possible.          |

---

<div align="center">

**🎯 Problem 2520 Completed!**

_Happy Coding! 🚀_

</div>
