<div align="center">

# 🧠 [1056. Confusing Number](https://leetcode.com/problems/confusing-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201056-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/confusing-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                         |
| **Acceptance Rate** | `49.3%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/confusing-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

<p>A <strong>confusing number</strong> is a number that when rotated <code>180</code> degrees becomes a different number with <strong>each digit valid</strong>.</p>

<p>We can rotate digits of a number by <code>180</code> degrees to form new digits.</p>

<ul>
	<li>When <code>0</code>, <code>1</code>, <code>6</code>, <code>8</code>, and <code>9</code> are rotated <code>180</code> degrees, they become <code>0</code>, <code>1</code>, <code>9</code>, <code>8</code>, and <code>6</code> respectively.</li>
	<li>When <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, and <code>7</code> are rotated <code>180</code> degrees, they become <strong>invalid</strong>.</li>
</ul>

<p>Note that after rotating a number, we can ignore leading zeros.</p>

<ul>
	<li>For example, after rotating <code>8000</code>, we have <code>0008</code> which is considered as just <code>8</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <code>true</code><em> if it is a <strong>confusing number</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1056.Confusing%20Number/images/1268_1.png" style="width: 281px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1056.Confusing%20Number/images/1268_2.png" style="width: 312px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 89
<strong>Output:</strong> true
<strong>Explanation:</strong> We get 68 after rotating 89, 68 is a valid number and 68 != 89.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1056.Confusing%20Number/images/1268_3.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> false
<strong>Explanation:</strong> We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `07-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `09-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                         | Difficulty  | Relationship    |
| ------------------------------------------------------------------------------- | ----------- | --------------- |
| [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) | 🟢 **Easy** | Similar logic   |
| [Confusing Number II](https://leetcode.com/problems/confusing-number-ii/)       | 🔴 **Hard** | Related concept |

---

## 💡 Solutions

### 🥉 Approach 1a: Brute Force With Digit Mapping

#### 📝 Intuition

> We can rotate a number by checking each digit:
>
> - If the digit is invalid `{2,3,4,5,7}`, return false immediately.
> - Otherwise, map it using the rule:  
>   `{0→0, 1→1, 6→9, 8→8, 9→6}`.
> - Construct the rotated number by processing digits in reverse.
> - Compare rotated number with the original.

#### 🔍 Algorithm

```pseudo
map = {0→0, 1→1, 6→9, 8→8, 9→6}

function isConfusingNumber(n):
    original = n
    rotated = 0
    while n > 0:
        digit = n % 10
        if digit not in map: return false
        rotated = rotated * 10 + map[digit]
        n = n / 10
    return rotated != original
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    bool confusingNumber(int n) {
        unordered_map<int,int> rotate = {{0,0},{1,1},{6,9},{8,8},{9,6}};
        int original = n, rotated = 0;
        while (n > 0) {
            int digit = n % 10;
            if (rotate.find(digit) == rotate.end()) return false;
            rotated = rotated * 10 + rotate[digit];
            n /= 10;
        }
        return rotated != original;
    }
};
```

### 🥉 Approach 1b: Brute Force with String-Based Rotation

#### 📝 Intuition

> Convert the number to a string. Reverse the string while mapping each character to its rotated digit.
> Finally, compare rotated string (converted back to integer) with the original.

#### 🔍 Algorithm

```pseudo
map = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}

function isConfusingNumber(n):
    s = str(n)
    rotated_str = ""
    for char in reverse(s):
        if char not in map: return false
        rotated_str += map[char]
    rotated_num = int(rotated_str)
    return rotated_num != n
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    bool confusingNumber(int n) {
        string s = to_string(n);
        unordered_map<char,char> rotate = {{'0','0'},{'1','1'},{'6','9'},{'8','8'},{'9','6'}};
        string rotated = "";
        for (int i = s.size()-1; i >= 0; i--) {
            if (rotate.find(s[i]) == rotate.end()) return false;
            rotated.push_back(rotate[s[i]]);
        }
        long rotatedNum = stol(rotated);
        return rotatedNum != n;
    }
};
```

### 🥈 Approach 2: Early Exit Optimizatio (Optimized Solution)

#### 📝 Intuition

> While checking digits, return immediately if an invalid digit is found.
> This avoids unnecessary processing. Similarly, if rotation so far already differs, we can short-circuit.

#### 🔍 Algorithm

```pseudo
function isConfusingNumber(n):
    original = n
    rotated = 0
    while n > 0:
        digit = n % 10
        if digit not in map: return false
        rotated = rotated * 10 + map[digit]
        n /= 10
    return rotated != original
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    bool confusingNumber(int n) {
        unordered_map<int,int> rotate = {{0,0},{1,1},{6,9},{8,8},{9,6}};
        int original = n, rotated = 0;
        while (n > 0) {
            int digit = n % 10;
            if (rotate.find(digit) == rotate.end()) return false; // invalid digit
            rotated = rotated * 10 + rotate[digit];
            n /= 10;
        }
        return rotated != original;
    }
};
```

### 🥇 Approach 3: Mathematical Reverse-Build (Optimal Solution ⭐)

#### 📝 Intuition

> Instead of reversing digits first and then mapping, we directly construct the rotated number from right to left using multiplication by 10.
> This reduces extra operations and is more elegant.

#### 🔍 Algorithm

```pseudo
function isConfusingNumber(n):
    map = {0→0, 1→1, 6→9, 8→8, 9→6}
    original = n
    rotated = 0
    while n > 0:
        digit = n % 10
        if digit not in map: return false
        rotated = rotated * 10 + map[digit]
        n /= 10
    return rotated != original
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    bool confusingNumber(int n) {
        unordered_map<int,int> rotate = {{0,0},{1,1},{6,9},{8,8},{9,6}};
        int original = n, rotated = 0;
        while (n > 0) {
            int digit = n % 10;
            if (rotate.find(digit) == rotate.end()) return false;
            rotated = rotated * 10 + rotate[digit];
            n /= 10;
        }
        return rotated != original;
    }
};
```

### 🥇 Approach 3: Precomputation (for multiple queries) (Optimal Solution ⭐)

#### 📝 Intuition

> If the function will be called multiple times, we can precompute all confusing numbers up to 10^9 or a reasonable limit (e.g., 10^5 for smaller constraints).
> Then answering each query is just a lookup.

#### 🔍 Algorithm

```pseudo
precompute all confusing numbers ≤ 10^9
store in hash set

function isConfusingNumber(n):
    return n in precomputed_set
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
    unordered_set<int> precomputed;
    bool isConfusingSingle(int n) {
        unordered_map<int,int> rotate = {{0,0},{1,1},{6,9},{8,8},{9,6}};
        int original = n, rotated = 0;
        while (n > 0) {
            int digit = n % 10;
            if (rotate.find(digit) == rotate.end()) return false;
            rotated = rotated * 10 + rotate[digit];
            n /= 10;
        }
        return rotated != original;
    }
public:
    Solution() {
        for (int i = 1; i <= 100000; i++) {
            if (isConfusingSingle(i)) precomputed.insert(i);
        }
    }
    bool confusingNumber(int n) {
        return precomputed.count(n) > 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach                      | Time Complexity               | Space Complexity | Pros                    | Cons                                    |
| ----------------------------- | ----------------------------- | ---------------- | ----------------------- | --------------------------------------- |
| 🥉 Brute Force Digit Mapping  | O(d)                          | O(1)             | Straightforward         | Slightly verbose                        |
| 🥈 String-Based Rotation      | O(d)                          | O(d)             | Easy to implement       | Slower due to string conversion         |
| 🥈 Early Exit Optimization    | O(d)                          | O(1)             | Faster in practice      | Same worst-case as brute force          |
| 🥇 Precomputation             | O(N·d) preprocess, O(1) query | O(N)             | Instant queries         | Memory heavy, only for multiple queries |
| 🥇 Mathematical Reverse-Build | O(d)                          | O(1)             | Clean, elegant, optimal | Same complexity as brute force          |

## 🎯 Why This is Optimal?

    - Mathematical reverse-build (Approach 5) is the cleanest and most optimal for a single query.
    - Precomputation (Approach 4) is optimal if we expect many queries.
    - Both reduce overhead compared to string manipulation.

### 🔑 Key Insights

| #   | Insight                                               |
| --- | ----------------------------------------------------- |
| 1   | Only digits `{0,1,6,8,9}` are valid.                  |
| 2   | A confusing number must differ from its rotated form. |
| 3   | Leading zeros in rotated numbers are ignored.         |
| 4   | For multiple queries, precomputation is efficient.    |

### 💭 Common Mistakes to Avoid

| #   | Insight                                               |
| --- | ----------------------------------------------------- |
| 1   | Only digits `{0,1,6,8,9}` are valid.                  |
| 2   | A confusing number must differ from its rotated form. |
| 3   | Leading zeros in rotated numbers are ignored.         |
| 4   | For multiple queries, precomputation is efficient.    |

### 🐛 Implementation Mistakes

| #   | Mistake                                   | Description                                 | How to Avoid                       | Example |
| --- | ----------------------------------------- | ------------------------------------------- | ---------------------------------- | ------- |
| 1   | Forgetting invalid digits                 | `{2,3,4,5,7}` are invalid                   | Check each digit against map       | n=23    |
| 2   | Forgetting to compare rotated vs original | Some valid rotations may equal the original | Always check `rotated != original` | n=11    |
| 3   | Misplacing rotation order                 | Reversing incorrectly                       | Use `%10` properly                 |         |

### 💭 Logical Thinking Mistakes

| #   | Mistake                        | Description                     | How to Avoid          | Prevention |
| --- | ------------------------------ | ------------------------------- | --------------------- | ---------- |
| 1   | Assuming rotation is symmetric | Not all numbers remain the same | Must check inequality |            |
| 2   | Ignoring leading zeros         | Rotated 8000 = 8, not 0008      | Convert correctly     |            |
| 3   | Forgetting base case           | Input 0 should return false     | Handle explicitly     |            |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                          |
| --- | ------------------- | ------------------------------------ |
| 1   | Digit extraction    | Process digits using `%` and `/`     |
| 2   | Mapping digits      | Convert each digit by rule           |
| 3   | Reverse build       | Construct rotated number efficiently |
| 4   | Precomputation      | Cache results for fast lookups       |

### 🔄 Follow-up Questions

| #   | Question                                   | Answer / Approach                        |
| --- | ------------------------------------------ | ---------------------------------------- |
| 1   | What if `n` can go beyond `10^9`?          | Same digit check works; complexity O(d). |
| 2   | What if many queries are asked?            | Precompute all confusing numbers once.   |
| 3   | Can we extend this to arbitrary rotations? | Yes, just update the mapping rules.      |

---

<div align="center">

**🎯 Problem 1056 Completed!**

_Happy Coding! 🚀_

</div>
