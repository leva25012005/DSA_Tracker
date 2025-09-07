<div align="center">

# 🧠 [1118. Number of Days in a Month](https://leetcode.com/problems/number-of-days-in-a-month/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201118-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/number-of-days-in-a-month/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                        |
| ------------------- | ---------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                  |
| **Acceptance Rate** | `59.2%`                                                                      |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/number-of-days-in-a-month/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)!          |

## Description

<!-- description:start -->

<p>Given a year <code>year</code> and a month <code>month</code>, return <em>the number of days of that month</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> year = 1992, month = 7
<strong>Output:</strong> 31
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> year = 2000, month = 2
<strong>Output:</strong> 29
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> year = 1900, month = 2
<strong>Output:</strong> 28
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1583 &lt;= year &lt;= 2100</code></li>
	<li><code>1 &lt;= month &lt;= 12</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `07-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `07-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1a: Hardcoded Array + Leap Year Check (Brute Force)

#### 📝 Intuition

> The number of days in each month is mostly fixed except for February.  
> We can store the days in an array and handle leap years separately.

#### 🔍 Algorithm

```pseudo
function numberOfDays(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and isLeap(year):
        return 29
    else:  return days[month - 1]
function isLeap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int numberOfDays(int year, int month) {
        vector<int> days = {31, 28, 31, 30, 31, 30,
                            31, 31, 30, 31, 30, 31};
        if (month == 2 && isLeap(year)) return 29;
        return days[month - 1];
    }

    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
};
```

### 🥉 Approach 1b: If-Else Conditions Only (Brute Force)

#### 📝 Intuition

> Instead of using arrays, directly check the month with conditionals..

#### 🔍 Algorithm

```pseudo
function numberOfDays(year, month):
    if month in {1,3,5,7,8,10,12} → return 31
    if month in {4,6,9,11} → return 30
    if month == 2:
        if isLeap(year) → return 29
        else return 28
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int numberOfDays(int year, int month) {
        if (month == 1 || month == 3 || month == 5 || month == 7 ||
            month == 8 || month == 10 || month == 12)
            return 31;
        if (month == 4 || month == 6 || month == 9 || month == 11)
            return 30;
        return isLeap(year) ? 29 : 28;
    }

    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
};
```

### 🥉 Approach 1c: If-Else Conditions Only (Brute Force)

#### 📝 Intuition

> Use a switch statement to directly map months to day counts.

#### 🔍 Algorithm

```pseudo
function numberOfDays(year, month):
    switch(month):
    case 1,3,5,7,8,10,12 → return 31
    case 4,6,9,11 → return 30
    case 2 → check leap year → return 29 or 28
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    int numberOfDays(int year, int month) {
        switch(month) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                return 31;
            case 4: case 6: case 9: case 11:
                return 30;
            case 2:
                return isLeap(year) ? 29 : 28;
        }
        return -1; // invalid input
    }

    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
};
```

### 🥈 Approach 2: Library Function (Optimized Solution)

#### 📝 Intuition

> Use built-in date handling functions which already know month lengths.

#### 🔍 Algorithm

```pseudo
return calendar.monthrange(year, month)[1]
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
#include <chrono>
using namespace std;

class Solution {
public:
    int numberOfDays(int year, int month) {
        using namespace std::chrono;
        year_month ym = year / month;
        auto first_day = sys_days(ym / 1);
        auto next_month = ym + months(1);
        auto first_next = sys_days(next_month / 1);
        return (first_next - first_day).count();
    }
};
```

### 🥇 Approach 3: Mathematical Formula (Optimal Solution ⭐)

#### 📝 Intuition

> Except February, we can use arithmetic patterns to compute days:
>
> - For months ≤ 7: odd months have 31 days, even months 30.
> - For months ≥ 8: even months have 31, odd months 30.

#### 🔍 Algorithm

```pseudo
if month == 2:
    if isLeap(year): return 29
    else return 28
else:
    return 30 + ((month + (month > 7)) % 2)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    int numberOfDays(int year, int month) {
        if (month == 2) return isLeap(year) ? 29 : 28;
        return 30 + ((month + (month > 7)) % 2);
    }

    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
};
```

## 📊 Comparison of Approaches

| Approach        | Time Complexity | Space Complexity | Pros                        | Cons                        |
| --------------- | --------------- | ---------------- | --------------------------- | --------------------------- |
| 🥉 Array + Leap | O(1)            | O(1)             | Clean, simple, easy to read | Needs extra array           |
| 🥉 Math Formula | O(1)            | O(1)             | Elegant, no array           | Harder to understand        |
| 🥉 Switch-Case  | O(1)            | O(1)             | Clear mapping               | Verbose, repetitive         |
| 🥈 If-Else      | O(1)            | O(1)             | No extra memory             | More verbose                |
| 🥇 Library      | O(1)            | O(1)             | Uses built-in reliability   | Overkill for simple problem |

## 🎯 Why This is Optimal?

> All solutions run in O(1) time and O(1) space.
> The array approach and if-else approach are the cleanest for interviews.
> The math formula is the most elegant but less intuitive.
> Using library functions is not always allowed but good in practice.

### 🔑 Key Insights

| #   | Insight                                        |
| --- | ---------------------------------------------- |
| 1   | Leap year calculation is the only tricky part. |
| 2   | February is the only month with variable days. |
| 3   | All solutions achieve constant time and space. |

### 💭 Common Mistakes to Avoid

| #   | Mistake               | Description                                    | How to Avoid                                      | Example                        |
| --- | --------------------- | ---------------------------------------------- | ------------------------------------------------- | ------------------------------ |
| 1   | Wrong leap year check | Only checking `year % 4 == 0`                  | Remember 100 is exception unless divisible by 400 | 1900 is NOT leap, 2000 IS leap |
| 2   | Off-by-one indexing   | Using `days[month]` instead of `days[month-1]` | Adjust for 0-based index                          | month=1 → index=0              |
| 3   | Ignoring constraints  | Not validating month 1–12                      | Ensure switch/array valid                         | Guard with condition           |

### 🐛 Implementation Mistakes

| #   | Mistake                                                           | Description                                                                                                                      | How to Avoid                                                                                                                | Example                                                                                         |                                                                      |                                                                                                   |
| --- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 1   | Wrong leap-year logic                                             | Implementing leap year as `year % 4 == 0` only (missing the 100/400 rules).                                                      | Implement full rule: \`year % 400 == 0                                                                                      |                                                                                                 | (year % 4 == 0 && year % 100 != 0)\`. Add unit tests for edge years. | `1900` should **not** be leap (1900 % 100 == 0 and 1900 % 400 != 0), but naive rule returns leap. |
| 2   | Off-by-one indexing for month array                               | Using `days[month]` instead of `days[month - 1]`, causing wrong lookup or out-of-bounds.                                         | Use 0-based indexing correctly and validate index range before access.                                                      | `month = 1` accidentally reads `days[1]` (February) instead of `days[0]` (January).             |                                                                      |                                                                                                   |
| 3   | Not handling February separately when using formulas              | Applying a generic formula to all months that also affects February, producing wrong result for February.                        | Branch February first (`if month == 2`) and handle leap-year separately; apply formula only to other months.                | Using `30 + ((month + (month > 7)) % 2)` without checking `month == 2` → wrong for `month = 2`. |                                                                      |                                                                                                   |
| 4   | Misusing date/time library APIs (off-by-one or timezone pitfalls) | Using C/C++ `tm` fields or other APIs that index months 0–11 or that are affected by locale/timezone, causing incorrect results. | Read docs carefully, normalize indices (e.g., `tm_mon + 1`), prefer `std::chrono` or simple lookup for this simple problem. | Passing month directly into `tm_mon` (0–11 expected) causes month mismatch.                     |                                                                      |                                                                                                   |
| 5   | Not validating input/range                                        | Accessing arrays or computing with invalid `month` values (e.g., 0 or 13) leads to UB or wrong returns.                          | Validate `1 <= month <= 12` up front and handle invalid input explicitly (assert/throw/return error).                       | `month = 0` leads to `days[-1]` (out-of-bounds) or undefined behavior.                          |                                                                      |                                                                                                   |

### 💭 Logical Thinking Mistakes

| #   | Mistake                                                        | Description                                                                                                            | How to Avoid                                                                           | Prevention                                                                                     |
| --- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 1   | Oversimplifying leap-year rule                                 | Believing "every year divisible by 4 is leap" and ignoring century rule.                                               | Memorize and apply the full rule: divisible by 400 OR (divisible by 4 AND not by 100). | Test known edge cases: 1900 (not leap), 2000 (leap).                                           |
| 2   | Assuming months strictly alternate 31/30 starting from January | Thinking pattern 31,30,31,30... for all months (ignores August symmetry).                                              | Use a fixed lookup or verified formula; don't rely on assumed alternation.             | Expecting August to follow the simple alternation leads to wrong days for Aug/Sep transitions. |
| 3   | Ignoring problem constraints / calendar system                 | Not noticing that problem uses Gregorian rules and gives `year >= 1583`; applying other calendars may confuse results. | Read constraints and apply the Gregorian rules as required by the problem.             | Applying Julian-calendar assumptions for years before Gregorian adoption.                      |
| 4   | Relying on heavy libraries for trivial problem                 | Using complex date APIs to solve a constant-time lookup increases risk of subtle bugs.                                 | Prefer a simple lookup + leap check for clarity and reliability.                       | Calling complicated time zone or locale functions for a simple day-count leads to surprises.   |
| 5   | Forgetting to test boundary years and months                   | Not verifying boundary inputs like `month=1`, `month=12`, `year=1583`, `year=2100`.                                    | Add unit tests for boundary and edge cases.                                            | Failing to test `year=2100, month=2` (2100 is not leap) and returning 29 erroneously.          |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique   | Application                      |
| --- | --------------------- | -------------------------------- |
| 1   | Leap year rule        | Handle February properly         |
| 2   | Mapping via array     | Fast lookup for fixed data       |
| 3   | Mathematical patterns | Optimize with modular arithmetic |

### 🔄 Follow-up Questions

| #   | Question                                                           | Answer / Approach                                                                            |
| --- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| 1   | How to extend this to support **any year**, not just \[1583–2100]? | The same leap year rules apply, so solutions are valid globally.                             |
| 2   | Can this be solved without conditionals at all?                    | Yes, with a precomputed array including February=28 and separately adjusting for leap years. |
| 3   | How would you solve it in Python in one line?                      | `return calendar.monthrange(year, month)[1]`                                                 |

---

<div align="center">

**🎯 Problem 1118 Completed!**

_Happy Coding! 🚀_

</div>
