<div align="center">

# 🧠 [1185. Day of the Week](https://leetcode.com/problems/day-of-the-week/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201185-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/day-of-the-week/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `58.7%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/day-of-the-week/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `08-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `08-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `09-09-2025` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## Description

<!-- description:start -->

<p>Given a date, return the corresponding day of the week for that date.</p>

<p>The input is given as three integers representing the <code>day</code>, <code>month</code> and <code>year</code> respectively.</p>

<p>Return the answer as one of the following values&nbsp;<code>{&quot;Sunday&quot;, &quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Wednesday&quot;, &quot;Thursday&quot;, &quot;Friday&quot;, &quot;Saturday&quot;}</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> day = 31, month = 8, year = 2019
<strong>Output:</strong> &quot;Saturday&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> day = 18, month = 7, year = 1999
<strong>Output:</strong> &quot;Sunday&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> day = 15, month = 8, year = 1993
<strong>Output:</strong> &quot;Sunday&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given dates are valid dates between the years <code>1971</code> and <code>2100</code>.</li>
</ul>

<!-- description:end -->

## 💡 Solutions

### 🥉 Approach 1: Day Counting (Brute Force)

#### 📝 Intuition

> We know a reference date: 1971-01-01 was Friday.
> The idea is to count the number of days from the base date to the target date, then take modulo 7 to get the weekday.

#### 🔍 Algorithm

```pseudo
function dayOfTheWeek(day, month, year):
    baseYear = 1971
    baseWeekday = Friday
    totalDays = 0

    for y from baseYear to year-1:
        if isLeap(y):
            totalDays += 366
        else:
            totalDays += 365

    for m from 1 to month-1:
        if m == 2 and isLeap(year):
            totalDays += 29
        else:
            totalDays += daysInMonth[m]

    totalDays += (day - 1)

    index = (baseWeekdayIndex + totalDays) mod 7
    return week[index]
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    vector<string> week = {"Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"};
    vector<int> daysInMonth = {31,28,31,30,31,30,31,31,30,31,30,31};

    bool isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }

    string dayOfTheWeek(int day, int month, int year) {
        int days = 0;
        for (int y = 1971; y < year; y++)
            days += isLeap(y) ? 366 : 365;

        for (int m = 1; m < month; m++) {
            if (m == 2 && isLeap(year)) days += 29;
            else days += daysInMonth[m-1];
        }
        days += day - 1;
        return week[days % 7];
    }
};
```

### 🥈 Approach 2: Precomputed Offsets (Optimized Solution)

#### 📝 Intuition

> Instead of looping through months, we can use a prefixSum array to store days before each month → faster.

#### 🔍 Algorithm

```pseudo
function dayOfTheWeek(day, month, year):
    baseYear = 1971
    baseWeekday = Friday
    prefix = [0,31,59,90,120,151,181,212,243,273,304,334]
    totalDays = 0

    for y from baseYear to year-1:
        if isLeap(y):
            totalDays += 366
        else:
            totalDays += 365

    totalDays += prefix[month-1] + (day - 1)
    if month > 2 and isLeap(year):
        totalDays += 1

    index = (baseWeekdayIndex + totalDays) mod 7
    return week[index]
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    vector<string> week = {"Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"};
    vector<int> prefix = {0,31,59,90,120,151,181,212,243,273,304,334};

    bool isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }

    string dayOfTheWeek(int day, int month, int year) {
        int days = 0;
        for (int y = 1971; y < year; y++)
            days += isLeap(y) ? 366 : 365;
        days += prefix[month-1] + day - 1;
        if (month > 2 && isLeap(year)) days++;
        return week[days % 7];
    }
};
```

### 🥇 Approach 3: Zeller’s Congruence (Optimal Solution ⭐)

#### 📝 Intuition

> Zeller’s formula computes weekday directly without iteration.

#### 🔍 Algorithm

```pseudo
function dayOfTheWeek(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    K = year mod 100
    J = floor(year / 100)

    h = (q + floor((13*(m+1))/5) + K + floor(K/4) + floor(J/4) + 5*J) mod 7

    return week[h]   // Mapping: 0=Saturday, 1=Sunday, ...
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution
class Solution {
public:
    vector<string> week = {"Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"};

    string dayOfTheWeek(int day, int month, int year) {
        if (month < 3) {
            month += 12;
            year--;
        }
        int q = day, m = month, K = year % 100, J = year / 100;
        int h = (q + (13*(m+1))/5 + K + K/4 + J/4 + 5*J) % 7;
        return week[h];
    }
};;
```

### 🏅 Approach 4: Doomsday Algorithm

#### 📝 Intuition

> Use Conway’s “Doomsday” rule: each year has a fixed weekday for specific dates (e.g., 4/4, 6/6, 8/8).
> Use that pivot to deduce the weekday for the given date.

#### 🔍 Algorithm

```pseudo
function dayOfTheWeek(day, month, year):
    anchorDay = getCenturyAnchor(year)
    y = year mod 100
    doomsday = (y + floor(y/4) + anchorDay) mod 7

    doomsdayDate = nearestDoomsday(month, year)

    offset = (day - doomsdayDate) mod 7
    weekday = (doomsday + offset) mod 7

    return week[weekday]
```

#### 💻 Implementation

```cpp
// Doomsday Algorithm approach

class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        vector<string> week = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

        // Days for each month where doomsday is known
        vector<int> doomsdayMonth = {0, 3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12};

        // Get century anchor
        int century = year / 100;
        int anchor;
        if (century % 4 == 0) anchor = 2;     // Tuesday
        else if (century % 4 == 1) anchor = 0; // Sunday
        else if (century % 4 == 2) anchor = 5; // Friday
        else anchor = 3;                      // Wednesday

        // Year within century
        int y = year % 100;
        int doomsday = (y + y/4 + anchor) % 7;

        // Adjust for leap year in Jan/Feb
        int refDay = doomsdayMonth[month];
        if (month == 1 || month == 2) {
            if (isLeap(year)) refDay += 1;
        }

        // Calculate difference
        int diff = (day - refDay) % 7;
        if (diff < 0) diff += 7;

        int weekday = (doomsday + diff) % 7;
        return week[weekday];
    }

private:
    bool isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }
};
```

### 🏅 Approach 5: Library-based (Built-in Functions)

#### 📝 Intuition

> Use the standard library (<chrono> in C++ or datetime in Python).

#### 💻 Implementation

```cpp
#include <chrono>
#include <string>
using namespace std;

class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        static vector<string> week = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
        std::tm time_in = {0,0,0,day,month-1,year-1900};
        std::time_t time_temp = std::mktime(&time_in);
        const std::tm * time_out = std::localtime(&time_temp);
        return week[time_out->tm_wday];
    }
};
```

## 📊 Comparison of Approaches

| Approach               | Time Complexity | Space Complexity | Pros                             | Cons                      |
| ---------------------- | --------------- | ---------------- | -------------------------------- | ------------------------- |
| 🥉 Brute Force         | O(Y+M)          | O(1)             | Easy to understand, low risk     | Slower, requires loops    |
| 🥈 Precomputed Offsets | O(Y)            | O(1)             | Faster, concise                  | Still loops by year       |
| 🥇 Zeller’s Formula ⭐ | O(1)            | O(1)             | Elegant, mathematical, very fast | Prone to formula mistakes |
| 🏅 Doomsday            | O(1)            | O(1)             | Interesting, efficient           | Harder to implement       |
| 🏅 Library-based       | O(1)            | O(1)             | Short, safe, reliable            | Dependent on language/lib |

## 🎯 Why This is Optimal?

    - Zeller’s Congruence and Doomsday Algorithm both run in O(1) → fastest.
    - No iteration over years/months → more efficient.
    - Clean, mathematically elegant, and scalable.

### 🔑 Key Insights

| #   | Insight                                                                     |
| --- | --------------------------------------------------------------------------- |
| 1   | Every solution boils down to computing an offset from a reference day.      |
| 2   | Leap year handling is the most common pitfall.                              |
| 3   | Mathematical formulas (Zeller/Doomsday) reduce complexity from O(Y) → O(1). |
| 4   | Standard libraries save implementation time and prevent bugs.               |

### 💭 Common Mistakes to Avoid

| #   | Mistake                | Description                                                 | How to Avoid           | Example                  |
| --- | ---------------------- | ----------------------------------------------------------- | ---------------------- | ------------------------ |
| 1   | Wrong leap year rule   | Forgot that divisible by 100 ≠ leap unless divisible by 400 | Use standard formula   | 1900 ≠ leap, 2000 = leap |
| 2   | Wrong weekday indexing | Confused `Sunday=0` vs `Monday=0` mappings                  | Define mapping upfront | Zeller h=0 → Saturday    |
| 3   | Forget `day-1` offset  | Adding current day instead of day-1                         | Always subtract 1      |                          |

### 🐛 Implementation Mistakes

| #   | Mistake                       | Description                     | How to Avoid            | Example                        |
| --- | ----------------------------- | ------------------------------- | ----------------------- | ------------------------------ |
| 1   | Off-by-one error              | Added wrong day offset          | Use `day-1` carefully   |                                |
| 2   | Wrong Feb days                | Forgot leap year check          | Write `isLeap()` helper |                                |
| 3   | Wrong year decrement (Zeller) | For Jan/Feb must decrement year | Apply rule strictly     | Jan 2000 → month=13, year=1999 |

### 💭 Logical Thinking Mistakes

| #   | Mistake               | Description                         | How to Avoid                   | Prevention              |
| --- | --------------------- | ----------------------------------- | ------------------------------ | ----------------------- |
| 1   | Wrong base date       | Used 1970 instead of 1971           | Double-check problem statement | Compare with test cases |
| 2   | Wrong base weekday    | Confused Friday with Sunday         | Debug with known inputs        | Use base test cases     |
| 3   | Not normalizing input | Forgot Jan/Feb conversion in Zeller | Convert before computing       | Apply m=13/14 rule      |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                  |
| --- | ------------------- | ---------------------------- |
| 1   | Prefix sum array    | Precompute days before month |
| 2   | Modular arithmetic  | Compute weekday using % 7    |
| 3   | Math formula        | Zeller’s Congruence          |
| 4   | Anchor day          | Doomsday Algorithm           |

### 🔄 Follow-up Questions

| #   | Question                                  | Answer / Approach                           |
| --- | ----------------------------------------- | ------------------------------------------- |
| 1   | What if input date goes far beyond 2100?  | Zeller/Doomsday still works, no range limit |
| 2   | What if no standard library is available? | Implement Zeller formula manually (O(1))    |
| 3   | Can this extend to Julian calendar?       | Yes, just adjust the formula accordingly    |

---

<div align="center">

**🎯 Problem 1185 Completed!**

_Happy Coding! 🚀_

</div>
