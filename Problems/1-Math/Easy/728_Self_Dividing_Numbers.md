<div align="center">

# 🧠 [728. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20728-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/self-dividing-numbers/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                              |
| **Acceptance Rate** | `79.8%`                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/self-dividing-numbers/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)       |

## Description

<!-- description:start -->

<p>A <strong>self-dividing number</strong> is a number that is divisible by every digit it contains.</p>

<ul>
	<li>For example, <code>128</code> is <strong>a self-dividing number</strong> because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.</li>
</ul>

<p>A <strong>self-dividing number</strong> is not allowed to contain the digit zero.</p>

<p>Given two integers <code>left</code> and <code>right</code>, return <em>a list of all the <strong>self-dividing numbers</strong> in the range</em> <code>[left, right]</code> (both <strong>inclusive</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> left = 1, right = 22
<strong>Output:</strong> [1,2,3,4,5,6,7,8,9,11,12,15,22]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> left = 47, right = 85
<strong>Output:</strong> [48,55,66,77]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `07-09-2026` | First attempt, understanding the problem |
| ✅ **Solved**    | `07-09-2026` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                       | Difficulty  | Relationship    |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------- |
| [Perfect Number](https://leetcode.com/problems/perfect-number/)                                                                               | 🟢 **Easy** | Similar logic   |
| [Check if Number Has Equal Digit Count and Digit Value](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/) | 🟢 **Easy** | Related concept |
| [Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)                                 | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Epic Systems** 🔥 89.3%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1a: Digit Extraction(rute Force)

#### 📝 Intuition

> Check every number in the range `[left, right]`. For each number, extract its digits using `% 10` and `/ 10`.  
> If the number is divisible by all its digits and contains no zero, then it is a self-dividing number.

#### 🔍 Algorithm

```pseudo
function selfDividingNumbers(left, right):
    for num in [left..right]:
        temp = num
        valid = true
        while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                valid = false
                break
            temp = temp / 10
        if valid:
            add num to result
    return result
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result;
        for (int num = left; num <= right; num++) {
            int temp = num;
            bool valid = true;
            while (temp > 0) {
                int digit = temp % 10;
                if (digit == 0 || num % digit != 0) {
                    valid = false;
                    break;
                }
                temp /= 10;
            }
            if (valid) result.push_back(num);
        }
        return result;
    }
};
```

### 🥉 Approach 1b: String Conversion(rute Force)

#### 📝 Intuition

> Instead of extracting digits mathematically, convert the number to a string and check each digit.
> This makes the implementation shorter but slightly slower.

#### 🔍 Algorithm

```pseudo
function selfDividingNumbers(left, right):
    for num in [left..right]:
    str_num = to_string(num)
    valid = true
    for digit_char in str_num:
        digit = int(digit_char)
        if digit == 0 or num % digit != 0:
            valid = false
            break
    if valid:
        add num to result

    return result
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result;
        for (int num = left; num <= right; num++) {
            string s = to_string(num);
            bool valid = true;
            for (char c : s) {
                int digit = c - '0';
                if (digit == 0 || num % digit != 0) {
                    valid = false;
                    break;
                }
            }
            if (valid) result.push_back(num);
        }
        return result;
    }
};
```

### 🥈 Approach 2: Optimized Solution with Digit Checking

#### 📝 Intuition

> Same as Approach 1, but directly return from a helper function isSelfDividing(num) for clarity and reusability.

#### 🔍 Algorithm

```pseudo
function isSelfDividing(num):
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            return false
        temp /= 10
    return true
function selfDividingNumbers(left, right):
    for num in [left..right]:
        if isSelfDividing(num):
            add num to result
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
private:
    bool isSelfDividing(int num) {
        int temp = num;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit == 0 || num % digit != 0) return false;
            temp /= 10;
        }
        return true;
    }
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result;
        for (int num = left; num <= right; num++) {
            if (isSelfDividing(num)) result.push_back(num);
        }
        return result;
    }
};
```

### 🥇 Approach 3: Precomputation (Caching All Valid Numbers) (Optimal Solution ⭐)

#### 📝 Intuition

> Since the constraint is right ≤ 10^4, we can precompute all self-dividing numbers once (from 1 → 10000) and store them.
> For any query [left, right], simply filter from this list.

#### 🔍 Algorithm

```pseudo
function selfDividingNumbers(left, right):
    precompute all self-dividing numbers up to 10000
    for num in precomputed_list:
        if left <= num <= right:
            add to result
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        static vector<int> all;
        if (all.empty()) {
            for (int num = 1; num <= 10000; num++) {
                int temp = num;
                bool valid = true;
                while (temp > 0) {
                    int digit = temp % 10;
                    if (digit == 0 || num % digit != 0) {
                        valid = false;
                        break;
                    }
                    temp /= 10;
                }
                if (valid) all.push_back(num);
            }
        }
        vector<int> result;
        for (int x : all) {
            if (x >= left && x <= right) result.push_back(x);
        }
        return result;
    }
};
```

### 🥇 Approach a: Mathematical Pruning

#### 📝 Intuition

> Skip unnecessary checks:
>
> - Immediately discard numbers containing digit 0.
> - Early break if any digit doesn’t divide the number.
>   ==> This reduces runtime slightly in practice.

#### 🔍 Algorithm

```pseudo
function selfDividingNumbers(left, right):
    for num in [left..right]:
        if num contains '0': continue
        if isSelfDividing(num): add to result
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        static vector<int> all;
        if (all.empty()) {
            for (int num = 1; num <= 10000; num++) {
                int temp = num;
                bool valid = true;
                while (temp > 0) {
                    int digit = temp % 10;
                    if (digit == 0 || num % digit != 0) {
                        valid = false;
                        break;
                    }
                    temp /= 10;
                }
                if (valid) all.push_back(num);
            }
        }
        vector<int> result;
        for (int x : all) {
            if (x >= left && x <= right) result.push_back(x);
        }
        return result;
    }
};
```

## 📊 Comparison of Approaches

| Approach                           | Time Complexity                  | Space Complexity | Pros                       | Cons                           |
| ---------------------------------- | -------------------------------- | ---------------- | -------------------------- | ------------------------------ |
| 🥉 Brute Force (Digit Extraction)  | O(n·d)                           | O(1)             | Straightforward, efficient | Slightly verbose               |
| 🥈 Brute Force (String Conversion) | O(n·d)                           | O(d)             | Simple, easy to read       | Slower due to string ops       |
| 🥈 Optimized Digit Check           | O(n·d)                           | O(1)             | Clean reusable helper      | Same complexity as brute force |
| 🥇 Precomputation                  | O(10⁴·d) preprocess + O(k) query | O(10⁴)           | Extremely fast queries     | Needs extra memory             |
| 🥇 Mathematical Pruning            | O(n·d) (but faster in practice)  | O(1)             | Efficient pruning          | Still same big-O               |

## 🎯 Why This is Optimal?

    - Precomputation (Approach 4) is optimal for multiple queries.
    - Mathematical pruning (Approach 5) is optimal for single query but with faster runtime.
    - Both improve clarity and scalability while keeping complexity minimal.

### 🔑 Key Insights

| #   | Insight                                                               |
| --- | --------------------------------------------------------------------- |
| 1   | Self-dividing numbers cannot contain digit `0`.                       |
| 2   | Constraint `10^4` allows precomputation.                              |
| 3   | Checking digits with `% 10` is more efficient than string conversion. |
| 4   | Helper functions improve readability.                                 |

### 💭 Common Mistakes to Avoid

| #   | Mistake                    | Description                                   | How to Avoid                            | Example                |
| --- | -------------------------- | --------------------------------------------- | --------------------------------------- | ---------------------- |
| 1   | Forgetting digit = 0 check | Division by zero error                        | Always check `digit == 0` first         | `128 → 0` digit check  |
| 2   | Mixing up `num` and `temp` | Using temp for modulo instead of original num | Keep `num` constant, only reduce `temp` | Correct: `num % digit` |
| 3   | Not resetting temp         | Using wrong value in loop                     | Always set `temp = num` per iteration   |                        |

### 🐛 Implementation Mistakes

| #   | Mistake              | Description                      | How to Avoid                | Example |
| --- | -------------------- | -------------------------------- | --------------------------- | ------- |
| 1   | Returning too early  | Breaking outer loop incorrectly  | Use flag or helper function |         |
| 2   | Using floating point | Converting chars incorrectly     | Stick with int operations   |         |
| 3   | Off-by-one errors    | Range boundaries `[left, right]` | Ensure inclusive check      |         |

### 💭 Logical Thinking Mistakes

| #   | Mistake                       | Description                                | How to Avoid                | Prevention |
| --- | ----------------------------- | ------------------------------------------ | --------------------------- | ---------- |
| 1   | Assuming 0 can be valid       | Wrong assumption about digits              | Re-read problem statement   |            |
| 2   | Misunderstanding divisibility | Confusing `digit % num` with `num % digit` | Think carefully about roles |            |
| 3   | Forgetting upper bound        | Not considering `10^4`                     | Apply constraint properly   |            |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                           |
| --- | ------------------- | ------------------------------------- |
| 1   | Digit extraction    | Extract digits using `%` and `/`      |
| 2   | String conversion   | Alternative approach for digit access |
| 3   | Precomputation      | Cache results for fast queries        |
| 4   | Early pruning       | Skip numbers containing `0`           |

### 🔄 Follow-up Questions

| #   | Question                                | Answer / Approach                                                |
| --- | --------------------------------------- | ---------------------------------------------------------------- |
| 1   | What if `right` was up to `10^9`?       | Precomputation not feasible → stick to digit check with pruning. |
| 2   | Can this be extended to base-k numbers? | Yes, but digit extraction logic changes accordingly.             |
| 3   | Can we parallelize?                     | Yes, divide range into subranges and merge results.              |

---

<div align="center">

**🎯 Problem 728 Completed!**

_Happy Coding! 🚀_

</div>
