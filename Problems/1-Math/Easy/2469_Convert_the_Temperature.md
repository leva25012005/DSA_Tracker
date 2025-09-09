<div align="center">

# 🧠 [2469. Convert the Temperature](https://leetcode.com/problems/convert-the-temperature/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202469-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/convert-the-temperature/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                |
| **Acceptance Rate** | `90.2%`                                                                    |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/convert-the-temperature/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)         |

## Description

<!-- description:start -->

<p>You are given a non-negative floating point number rounded to two decimal places <code>celsius</code>, that denotes the <strong>temperature in Celsius</strong>.</p>

<p>You should convert Celsius into <strong>Kelvin</strong> and <strong>Fahrenheit</strong> and return it as an array <code>ans = [kelvin, fahrenheit]</code>.</p>

<p>Return <em>the array <code>ans</code>. </em>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p><strong>Note that:</strong></p>

<ul>
	<li><code>Kelvin = Celsius + 273.15</code></li>
	<li><code>Fahrenheit = Celsius * 1.80 + 32.00</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> celsius = 36.50
<strong>Output:</strong> [309.65000,97.70000]
<strong>Explanation:</strong> Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> celsius = 122.11
<strong>Output:</strong> [395.26000,251.79800]
<strong>Explanation:</strong> Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= celsius &lt;= 1000</code></li>
</ul>

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

| Problem                                                                         | Difficulty  | Relationship  |
| ------------------------------------------------------------------------------- | ----------- | ------------- |
| [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Direct Formula (Brute Force)

#### 📝 Intuition

> Since the conversion formulas are given, we can directly apply them without any apply them without any additional logic.

#### 🔍 Algorithm

```pseudo
function convertTemperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
```

#### 💻 Implementation

```cpp
// Brute force approach
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double fahrenheit = celsius * 1.80 + 32.00;
        return {kelvin, fahrenheit};
    }
};
```

### 🥇 Approach 3: Using Constants (Clean & Maintainable)(Optimal Solution ⭐)

#### 📝 Intuition

> Instead of hardcoding formulas inside the function, define constants for better readability and maintainability.
> This makes it easier to adjust if formulas change in other contexts.

#### 🔍 Algorithm

```pseudo
function convertTemperature(celsius):
    const K_OFFSET = 273.15
    const F_MULTIPLIER = 1.80
    const F_OFFSET = 32.00

    kelvin = celsius + K_OFFSET
    fahrenheit = celsius * F_MULTIPLIER + F_OFFSET
    return [kelvin, fahrenheit]
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        const double K_OFFSET = 273.15;
        const double F_MULTIPLIER = 1.80;
        const double F_OFFSET = 32.00;

        double kelvin = celsius + K_OFFSET;
        double fahrenheit = celsius * F_MULTIPLIER + F_OFFSET;

        return {kelvin, fahrenheit};
    }
};
```

## 📊 Comparison of Approaches

| Approach          | Time Complexity | Space Complexity | Pros                       | Cons                 |
| ----------------- | --------------- | ---------------- | -------------------------- | -------------------- |
| 🥉 Direct Formula | O(1)            | O(1)             | Simple, straightforward    | Hardcoded constants  |
| 🥇 Constants ⭐   | O(1)            | O(1)             | Clean, maintainable, clear | Slightly longer code |

## 🎯 Why This is Optimal?

- So sánh nhanh với brute force và optimized
- Nêu rõ cách tối ưu được cả time/space
- Giải thích tại sao đây là giải pháp clean và scalable nhất

### 🔑 Key Insights

| #   | Insight                                                                 |
| --- | ----------------------------------------------------------------------- |
| 1   | Both conversions are **linear transformations**.                        |
| 2   | Floating point precision is required but `double` in C++ is sufficient. |
| 3   | Return type is a vector since we need both Kelvin and Fahrenheit.       |

### 💭 Common Mistakes to Avoid

| #   | Mistake         | Description                                                        | How to Avoid              | Example                                      |
| --- | --------------- | ------------------------------------------------------------------ | ------------------------- | -------------------------------------------- |
| 1   | Wrong formula   | Mixing Fahrenheit and Kelvin formulas                              | Memorize correctly        | Fahrenheit needs `×1.8 + 32`, not `+ 273.15` |
| 2   | Precision loss  | Using `float` instead of `double`                                  | Use `double` for accuracy | `float` may cause tiny rounding errors       |
| 3   | Order of return | Returning `[fahrenheit, kelvin]` instead of `[kelvin, fahrenheit]` | Follow problem statement  | Must match `[Kelvin, Fahrenheit]`            |

### 🔄 Follow-up Questions

| #   | Question                                                   | Answer / Approach                                                         |
| --- | ---------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1   | What if we also need to convert to **Rankine**?            | Add another formula: Rankine = Celsius × 1.8 + 491.67                     |
| 2   | What if precision needs to be controlled?                  | Use `setprecision` in C++ when outputting.                                |
| 3   | Can this be extended to support bi-directional conversion? | Yes, create a utility class with methods `toKelvin`, `toFahrenheit`, etc. |

---

<div align="center">

**🎯 Problem 2469 Completed!**

_Happy Coding! 🚀_

</div>
