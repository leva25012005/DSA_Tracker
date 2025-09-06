<div align="center">

# 🧠 [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%209-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/palindrome-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                |
| ------------------- | -------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                          |
| **Acceptance Rate** | `59.5%`                                                              |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/palindrome-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)   |

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `06-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `06-09-2025  | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                 | Difficulty    | Relationship    |
| ----------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                                         | 🟢 **Easy**   | Similar logic   |
| [Find Palindrome With Fixed Length](https://leetcode.com/problems/find-palindrome-with-fixed-length/)                   | 🟡 **Medium** | Related concept |
| [Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/)                               | 🟡 **Medium** | Related concept |
| [ Count Symmetric Integers](https://leetcode.com/problems/count-symmetric-integers/)                                    | 🟢 **Easy**   | Related concept |
| [Find the Count of Good Integers](https://leetcode.com/problems/find-the-count-of-good-integers/)                       | 🔴 **Hard**   | Related concept |
| [Find the Largest Palindrome Divisible by K](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/) | 🔴 **Hard**   | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Cognizant** 🔥 100.0%
- **Roche** 🔥 100.0%
- **Garmin** 🔥 89.2%
- **Accenture** 🔥 85.8%

### ⭐ Medium Frequency (60-79%)

- **Deloitte** ⭐ 76.9%
- **Infosys** ⭐ 76.7%
- **tcs** ⭐ 76.6%
- **HCL** ⭐ 75.5%
- **Bloomberg** ⭐ 74.5%
- **persistent systems** ⭐ 73.2%
- **Wipro** ⭐ 70.1%
- **Adobe** ⭐ 68.6%
- **Apple** ⭐ 68.0%
- **Microsoft** ⭐ 67.5%
- **Capgemini** ⭐ 67.1%
- **Amazon** ⭐ 66.9%
- **Qualcomm** ⭐ 66.9%
- **EPAM Systems** ⭐ 66.8%
- **FPT** ⭐ 66.6%
- **Yahoo** ⭐ 62.9%
- **Samsung** ⭐ 61.0%

### 📈 Regular Frequency (40-59%)

- **Intel** 📈 59.5%
- **Meta** 📈 57.0%
- **Capital One** 📈 54.8%
- **Zoho** 📈 52.5%
- **Uber** 📈 47.3%
- **IBM** 📈 44.1%
- **Visa** 📈 42.9%

### 📊 Low Frequency Companies (0-39%)

- **Oracle** 📊 39.7%
- **Walmart Labs** 📊 36.8%
- **J.P. Morgan** 📊 36.3%
- **Yandex** 📊 35.9%

---

## 💡 Solutions

### 🥉 Approach 1: String Conversion (Brute Force)

#### 📝 Intuition

> Converting strig to number and then compare that string with reversed string.

#### 🔍 Algorithm

```pseudo
function isPalindrome(x):
    if x < 0:
        return false;
    s = to_string(x)
    return s == reverse(s)
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        string rev = s;
        reverse(rev.begin(), rev.end());
        return s == rev;
    }
};

```

### 🥈 Approach 2a: Reverse Full Number (Optimized Solution)

#### 📝 Intuition

> Reversing the whole number ussing division and modulo and then compare with origin number.

#### 🔍 Algorithm

```pseudo
function isPalindrome(x)
    if x < 0:
        return false
    original = x
    rev = 0
    while x > 0
        rev = rev * 10 + (x % 10)
        x = x / 10
    reutnr original == rev
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity

class Solution {
public:
    bool Palindrome Number(int x)
    long long rev = 0, original = x;
    while(x > 10) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    return original == rev;
};
```

### 🥇 Approach 2b: Reverse Half Number (Optimal Solution ⭐)

#### 📝 Intuition

> To avoid overflow, just invert the last half of the number and compare it with the remaining half.f the number has odd digits, discard the middle digit (rev/10).

#### 🔍 Algorithm

```pseudo
function isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return false
    rev = 0
    while x > rev:
        rev = rev * 10 + (x % 10)
        x = x / 10
    return x == rev or x == rev / 10
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return (x == rev) || (x == rev / 10);
    }
};
```

### 🥈 Approach 3: Compare First & Last Digits

#### 📝 Intuition

> Take the first digit by dividing by 10^k, the last digit is equal to % 10, compare gradually. After each round, remove the 2 compared digits.

#### 🔍 Algorithm

```pseudo
function isPalindrome(x):
    if x < 0:
        return false
    div = 1
    while x / div >= 10:
        div *= 10
    while x != 0:
        left = x / div
        right = x % 10
        if left != right: return false
        x = (x % div) / 10
        div /= 100
    return true
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int div = 1;
        while (x / div >= 10) div *= 10;
        while (x != 0) {
            int left = x / div;
            int right = x % 10;
            if (left != right) return false;
            x = (x % div) / 10;
            div /= 100;
        }
        return true;
    }
};
```

### 🥈 Approach 4: Recursive (String)

#### 📝 Intuition

> TConvert to string and recursively compare first and last character, then continue to check the rest.

#### 🔍 Algorithm

```pseudo
function helper(s, l, r):
    if l >= r: return true
    if s[l] != s[r]: return false
    return check(l+1, r-1)
function isPalindrome(x):
    if x < 0
        return false
    s = to_string(x)
    return helper(s, 0, s.size() - 1)
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool helper(const string& s, int l, int r) {
        if (l >= r) return true;
        if (s[l] != s[r]) return false;
        return helper(s, l + 1, r - 1);
    }

    bool isPalindrome(int x) {
        if (x < 0) return false;
        string s = to_string(x);
        return helper(s, 0, s.size() - 1);
    }
};
```

### 🥈 Approach 5: Two Pointers (String)

#### 📝 Intuition

> Switch to string, use 2 pointers to point at the beginning and end, move gradually to the middle to compare.

#### 🔍 Algorithm

```pseudo
function isPalindrome(x):
    if x < 0: return false
    s = to_string(x)
    l = 0, r = len(s)-1
    while l < r:
        if s[l] != s[r]: return false
        l++, r--
    return true
```

#### 💻 Implementation

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        string s = to_string(x);
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++; r--;
        }
        return true;
    }
};
```

## 📊 Comparison of Approaches

| Approach                     | Time Complexity | Space Complexity | Pros                                          | Cons                                             |
| ---------------------------- | --------------- | ---------------- | --------------------------------------------- | ------------------------------------------------ |
| 🥉 Approach 1: String Method | O(n)            | O(n)             | Easy to understand, concise code              | Not “purely mathematical”, memory consuming      |
| Approach 2a: Full Reverse    | O(log n)        | O(1)             | No need for strings, easy to code             | Can overflow if not using `long long`            |
| 🥇 Approach 2b: Half Reverse | O(log n)        | O(1)             | Optimized, avoid overflow, interview-standard | Code is a bit tricky, hard to read for beginners |
| Approach 3: Compare Digits   | O(log n)        | O(1)             | Direct, no inversion                          | Be careful when calculating `div`                |
| Approach 4: Recursion        | O(n)            | O(n) (stack)     | Clear idea, easy to present                   | Stack consuming, not optimal                     |
| Approach 5: Two Pointers     | O(n)            | O(1)             | Basic, easy to understand                     | Still have to convert to string                  |

## 🎯 Why This is Optimal?

    - No additional memory required (O(1)).
    - O(log n) time since only half of the number is scanned.
    - Completely avoids overflow.
    - Clean, elegant, often expected in interviews.

### 🔑 Key Insights

| #   | Insight                                                                  |
| --- | ------------------------------------------------------------------------ |
| 1   | No need to invert the whole number, just invert half.                    |
| 2   | Negative numbers and numbers ending in 0 (except 0) are not palindromes. |
| 3   | String approach is simple but not optimal.                               |

### 💭 Common Mistakes to Avoid

| #   | Mistake                              | Description                                  | How to Avoid                      | Example    |
| --- | ------------------------------------ | -------------------------------------------- | --------------------------------- | ---------- |
| 1   | Forgot to check for negative numbers | Considered -121 as a palindrome              | Checked `x < 0`                   | -121       |
| 2   | Forgot to handle numbers ending in 0 | 10 is not a palindrome                       | Checked `(x % 10 == 0 && x != 0)` | 10         |
| 3   | Only compares full reverse           | Wrong when large numbers can easily overflow | Used half reverse                 | 2147483647 |

### 🐛 Implementation Mistakes

| #   | Mistake                             | Description           | How to Avoid                       | Example           |
| --- | ----------------------------------- | --------------------- | ---------------------------------- | ----------------- |
| 1   | Use int for reverse                 | Large number overflow | Use long long                      | 2147483647        |
| 2   | Wrong divisor in Approach 3         | Deviated comparison   | Debug carefully, test many numbers | 1001              |
| 3   | Recursion has no standard base case | Causes stack overflow | Always check l ≥ r                 | 12345678987654321 |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                                  | Description                  | How to Avoid                         | Prevention              |
| --- | -------------------------------------------------------- | ---------------------------- | ------------------------------------ | ----------------------- |
| 1   | Thinking that you always have to invert the whole number | Actually, you only need half | Understand the nature of palindromes | Look at odd-digit cases |
| 2   | Ignore X=0                                               | Forget boundary cases        | Test edge cases                      | X=0                     |
| 3   | Only test even-digit numbers                             | Fails with odd numbers       | Add condition `rev/10`               | 12321                   |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique   | Application                                |
| --- | --------------------- | ------------------------------------------ |
| 1   | Two Pointers          | Compare first and last characters          |
| 2   | Math Digit Extraction | Reverse numbers using division and mod     |
| 3   | Edge Case Handling    | Check for negative numbers, trailing zeros |

### 🔄 Follow-up Questions

| #   | Question                                   | Answer / Approach                       |
| --- | ------------------------------------------ | --------------------------------------- |
| 1   | Can it be solved without strings?          | Yes, Approach 2a/2b/3.                  |
| 2   | If the problem extends to strings?         | Two pointers are similar.               |
| 3   | If the number is very large (big integer)? | Use strings, mathematically impossible. |

---

<div align="center">

**🎯 Problem 9 Completed!**

_Happy Coding! 🚀_

</div>
