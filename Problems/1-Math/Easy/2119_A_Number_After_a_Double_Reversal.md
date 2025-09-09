<div align="center">

# 🧠 [2119. A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202119-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/a-number-after-a-double-reversal/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                               |
| ------------------- | ----------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                         |
| **Acceptance Rate** | `81.4%`                                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/a-number-after-a-double-reversal/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                  |

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `08-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `08-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## Description

<!-- description:start -->

<p><strong>Reversing</strong> an integer means to reverse all its digits.</p>

<ul>
	<li>For example, reversing <code>2021</code> gives <code>1202</code>. Reversing <code>12300</code> gives <code>321</code> as the <strong>leading zeros are not retained</strong>.</li>
</ul>

<p>Given an integer <code>num</code>, <strong>reverse</strong> <code>num</code> to get <code>reversed1</code>, <strong>then reverse</strong> <code>reversed1</code> to get <code>reversed2</code>. Return <code>true</code> <em>if</em> <code>reversed2</code> <em>equals</em> <code>num</code>. Otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 526
<strong>Output:</strong> true
<strong>Explanation:</strong> Reverse num to get 625, then reverse 625 to get 526, which equals num.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 1800
<strong>Output:</strong> false
<strong>Explanation:</strong> Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> Reverse num to get 0, then reverse 0 to get 0, which equals num.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## 🔗 Related Problems

| Problem                                                           | Difficulty    | Relationship    |
| ----------------------------------------------------------------- | ------------- | --------------- |
| [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | 🟡 **Medium** | Similar logic   |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/)       | 🟢 **Easy**   | Related concept |

---

## 💡 Solutions

### 🥉 Approach 1: String Conversion + Reverse Twice (Brute Force)

#### 📝 Intuition

> The simplest way is to convert the number into a string, reverse it twice, and compare the result with the original number.

#### 🔍 Algorithm

```pseudo
function isSameAfterReversals(num):
    str_num = convert num to string
    reversed1 = reverse(str_num)
    reversed2 = reverse(reversed1)
    return (reversed2 == str_num)
```

#### 💻 Implementation

```cpp
// Brute force using string reversal
class Solution {
public:
    bool isSameAfterReversals(int num) {
        string s = to_string(num);
        string rev1 = s;
        reverse(rev1.begin(), rev1.end());
        string rev2 = rev1;
        reverse(rev2.begin(), rev2.end());
        return rev2 == s;
    }
};
```

### 🥈 Approach 2: Math Digit Extraction (Reverse Twice) (Optimized) Solution

#### 📝 Intuition

> Instead of converting to a string, we can extract digits mathematically and reverse the number twice.

#### 🔍 Algorithm

```pseudo
function reverseNumber(x):
    rev = 0
    while x > 0:
        rev = rev * 10 + (x % 10)
        x = x / 10
    return rev

function isSameAfterReversals(num):
    rev1 = reverseNumber(num)
    rev2 = reverseNumber(rev1)
    return (rev2 == num)
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
// Mathematical digit extraction

class Solution {
    int reverseNum(int x) {
        int rev = 0;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x /= 10;
        }
        return rev;
    }
public:
    bool isSameAfterReversals(int num) {
        int rev1 = reverseNum(num);
        int rev2 = reverseNum(rev1);
        return rev2 == num;
    }
};
```

### 🥈 Approach 3: Hybrid (String + Trim Zeros)

#### 📝 Intuition

> We can simulate the behavior by reversing the string and removing leading zeros manually before reversing again.

#### 🔍 Algorithm

```pseudo
function isSameAfterReversals(num):
    s = convert num to string
    rev1 = reverse(s)
    rev1_trimmed = remove leading zeros from rev1
    rev2 = reverse(rev1_trimmed)
    return (rev2 == s)
```

#### 💻 Implementation

```cpp
// Hybrid string-based with trimming

class Solution {
public:
    bool isSameAfterReversals(int num) {
        string s = to_string(num);
        string rev1 = s;
        reverse(rev1.begin(), rev1.end());
        // trim leading zeros
        int i = 0;
        while (i < rev1.size() && rev1[i] == '0') i++;
        string trimmed = rev1.substr(i);
        if (trimmed.empty()) trimmed = "0";
        string rev2 = trimmed;
        reverse(rev2.begin(), rev2.end());
        return rev2 == s;
    }
};
```

### 🥈 Approach 4: Reverse Once + Reuse

#### 📝 Intuition

> Instead of coding the whole process inline, create a reusable reverse function and simply call it twice for clarity.

#### 🔍 Algorithm

```pseudo
function isSameAfterReversals(num):
    rev1 = reverse(num)
    rev2 = reverse(rev1)
    return rev2 == num
```

#### 💻 Implementation

```cpp
// Cleaner mathematical approach with reusable function

class Solution {
    int reverseNum(int x) {
        int rev = 0;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x /= 10;
        }
        return rev;
    }
public:
    bool isSameAfterReversals(int num) {
        return reverseNum(reverseNum(num)) == num;
    }
};
```

### 🥇 Approach 3: Trailing Zero Check (Optimal Solution ⭐)

#### 📝 Intuition

> Observation:
> If num == 0 → it always stays the same.
> If num % 10 == 0 → reversing removes trailing zeros → cannot restore.
> Otherwise, reversing twice will always return the original.
> This gives us a direct O(1) solution.

#### 🔍 Algorithm

```pseudo
function isSameAfterReversals(num):
    if num == 0:
        return true
    if num % 10 == 0:
        return false
    return true
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    bool isSameAfterReversals(int num) {
        if (num == 0) return true;
        return num % 10 != 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                          | Cons                     |
| -------------- | --------------- | ---------------- | ----------------------------- | ------------------------ |
| 🥉 Brute Force | O(d)            | O(d)             | Simple, easy to implement     | Slow, uses string ops    |
| 🥈 Optimized   | O(d)            | O(1)             | Faster, math only             | Still does two reversals |
| 🥈 Hybrid      | O(d)            | O(d)             | Shows trimming clearly        | More complex than needed |
| 🥈 ReverseOnce | O(d)            | O(1)             | Clean code, reusable function | Still two reversals      |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fastest, cleanest, elegant    | Requires key insight     |

## 🎯 Why This is Optimal?

    - Unlike brute force and digit-based methods (which take O(d)), the trailing zero check runs in O(1).
    - Clean, scalable, no string conversion, no loops.
    - Directly leverages problem insight.

### 🔑 Key Insights

| #   | Insight                                                           |
| --- | ----------------------------------------------------------------- |
| 1   | Reversing twice restores the number if no trailing zeros are lost |
| 2   | Any number ending with `0` (except 0 itself) will lose digits     |
| 3   | Problem reduces to a **modulo check** rather than simulation      |

### 💭 Common Mistakes to Avoid

| #   | Mistake                | Description                       | How to Avoid        | Example |
| --- | ---------------------- | --------------------------------- | ------------------- | ------- |
| 1   | Forget `num == 0` case | Zero is always valid              | Add special case    | `num=0` |
| 2   | Ignoring leading zeros | After reverse, they disappear     | Handle trimming     | `1800`  |
| 3   | Overflow in reversing  | If not careful with large numbers | Use `int` carefully | `10^6`  |

### 🐛 Implementation Mistakes

| #   | Mistake               | Description               | How to Avoid             | Example |
| --- | --------------------- | ------------------------- | ------------------------ | ------- |
| 1   | Using `stoi` blindly  | May throw exception       | Check validity           | `"000"` |
| 2   | Wrong reverse logic   | Not updating rev properly | Test with small examples | `123`   |
| 3   | Forget trimming zeros | Causes wrong comparison   | Trim before comparing    | `1800`  |

### 💭 Logical Thinking Mistakes

| #   | Mistake                   | Description                     | How to Avoid           | Prevention          |
| --- | ------------------------- | ------------------------------- | ---------------------- | ------------------- |
| 1   | Overcomplicating solution | Writing loops instead of O(1)   | Look for math insights | Think about zeros   |
| 2   | Assuming all numbers fail | Not realizing `0` is valid      | Check base cases       | Test edge cases     |
| 3   | Misunderstanding reverse  | Forgetting leading zeros vanish | Work through examples  | Try `1800, 1200, 0` |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique         | Application                      |
| --- | --------------------------- | -------------------------------- |
| 1   | String manipulation         | Basic brute force reversal       |
| 2   | Math digit extraction       | Reverse without string           |
| 3   | Modulo / Arithmetic insight | Optimal O(1) trailing zero check |

### 🔄 Follow-up Questions

| #   | Question                                | Answer / Approach                                     |
| --- | --------------------------------------- | ----------------------------------------------------- |
| 1   | What if `num` is negative?              | Define reverse behavior for negatives, extend logic   |
| 2   | What if `num` is very large (10^18)?    | Use `long long` or `BigInt` handling in C++           |
| 3   | Can we generalize to "reverse k times"? | Analyze behavior: after even k, same if no zeros lost |

---

<div align="center">

**🎯 Problem 2119 Completed!**

_Happy Coding! 🚀_

</div>
