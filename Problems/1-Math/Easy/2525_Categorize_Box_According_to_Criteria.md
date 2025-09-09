<div align="center">

# 🧠 [2525. Categorize Box According to Criteria](https://leetcode.com/problems/categorize-box-according-to-criteria/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202525-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/categorize-box-according-to-criteria/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                             |
| **Acceptance Rate** | `37.9%`                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/categorize-box-according-to-criteria/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                      |

## Description

<!-- description:start -->

<p>Given four integers <code>length</code>, <code>width</code>, <code>height</code>, and <code>mass</code>, representing the dimensions and mass of a box, respectively, return <em>a string representing the <strong>category</strong> of the box</em>.</p>

<ul>
	<li>The box is <code>&quot;Bulky&quot;</code> if:

  <li><strong>Bulky</strong> if <strong>any</strong> of the following conditions hold:
    <ul>
      <li>Any of the dimensions of the box is greater or equal to <code>10<sup>4</sup></code>.</li>
      <li>Or, the <strong>volume</strong> of the box is greater or equal to <code>10<sup>9</sup></code>.</li>
    </ul>
  </li>
  <li>If the mass of the box is greater or equal to <code>100</code>, it is <code>"Heavy"</code>.</li>
  <li>If the box is both <code>"Bulky"</code> and <code>"Heavy"</code>, then its category is <code>"Both"</code>.</li>
  <li>If the box is neither <code>"Bulky"</code> nor <code>"Heavy"</code>, then its category is <code>"Neither"</code>.</li>
  <li>If the box is <code>"Bulky"</code> but not <code>"Heavy"</code>, then its category is <code>"Bulky"</code>.</li>
  <li>If the box is <code>"Heavy"</code> but not <code>"Bulky"</code>, then its category is <code>"Heavy"</code>.</li>
</ul>

</ul>

<p><strong>Note</strong> that the volume of the box is the product of its length, width and height.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> length = 1000, width = 35, height = 700, mass = 300
<strong>Output:</strong> &quot;Heavy&quot;
<strong>Explanation:</strong> 
None of the dimensions of the box is greater or equal to 10<sup>4</sup>. 
Its volume = 24500000 &lt;= 10<sup>9</sup>. So it cannot be categorized as &quot;Bulky&quot;.
However mass &gt;= 100, so the box is &quot;Heavy&quot;.
Since the box is not &quot;Bulky&quot; but &quot;Heavy&quot;, we return &quot;Heavy&quot;.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> length = 200, width = 50, height = 800, mass = 50
<strong>Output:</strong> &quot;Neither&quot;
<strong>Explanation:</strong> 
None of the dimensions of the box is greater or equal to 10<sup>4</sup>.
Its volume = 8 * 10<sup>6</sup> &lt;= 10<sup>9</sup>. So it cannot be categorized as &quot;Bulky&quot;.
Its mass is also less than 100, so it cannot be categorized as &quot;Heavy&quot; either. 
Since its neither of the two above categories, we return &quot;Neither&quot;.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= length, width, height &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= mass &lt;= 10<sup>3</sup></code></li>
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

| Problem                                                                                               | Difficulty  | Relationship    |
| ----------------------------------------------------------------------------------------------------- | ----------- | --------------- |
| [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)                                                 | 🟢 **Easy** | Similar logic   |
| [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | 🟢 **Easy** | Related concept |
| [Best Poker Hand](https://leetcode.com/problems/best-poker-hand/)                                     | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Zendesk** 🔥 100.0%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: If-Else (Brute Force)

#### 📝 Intuition

> MThe simplest approach:
>
> - Compute the box volume.
> - Use if-else statements to check bulky and heavy conditions.
> - Return the string according to the 4 possible cases.

#### 🔍 Algorithm

```pseudo
function categorizeBox(length, width, height, mass):
    volume = length * width * height

    bulky = (length >= 1e4 OR width >= 1e4 OR height >= 1e4 OR volume >= 1e9)
    heavy = (mass >= 100)

    if bulky AND heavy: return "Both"
    else if bulky: return "Bulky"
    else if heavy: return "Heavy"
    else: return "Neither"
```

#### 💻 Implementation

```cpp
// Brute force approach (if-else)
class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        long long volume = 1LL * length * width * height;

        bool bulky = (length >= 1e4 || width >= 1e4 || height >= 1e4 || volume >= 1e9);
        bool heavy = (mass >= 100);

        if (bulky && heavy) return "Both";
        if (bulky) return "Bulky";
        if (heavy) return "Heavy";
        return "Neither";
    }
};
```

### 🥈 Approach 2: Flag / Bitmask (Optimized Solution)

#### 📝 Intuition

> Instead of multiple if-else, encode the state with numbers:
> bulky = 1
> heavy = 2
> Result = flag sum (0,1,2,3).
> Use switch or a map to return the category.

#### 🔍 Algorithm

```pseudo
function categorizeBox(length, width, height, mass):
    volume = length * width * height
    flag = 0
    if (dimension >= 1e4 OR volume >= 1e9): flag += 1
    if (mass >= 100): flag += 2

    switch(flag):
        case 0: return "Neither"
        case 1: return "Bulky"
        case 2: return "Heavy"
        case 3: return "Both"
```

#### 💻 Implementation

```cpp
// Optimized with flags

class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        long long volume = 1LL * length * width * height;
        int flag = 0;

        if (length >= 1e4 || width >= 1e4 || height >= 1e4 || volume >= 1e9) flag += 1;
        if (mass >= 100) flag += 2;

        switch(flag) {
            case 0: return "Neither";
            case 1: return "Bulky";
            case 2: return "Heavy";
            case 3: return "Both";
        }
        return "";
    }
};

```

### 🥇 Approach 3: Mapping Table (Optimal Solution ⭐)

#### 📝 Intuition

> Represent the result as a mapping (bulky, heavy) → category.
> This makes the code clear, clean, and extendable.

#### 🔍 Algorithm

```pseudo
function categorizeBox(length, width, height, mass):
    volume = length * width * height
    bulky = (dimension >= 1e4 OR volume >= 1e9)
    heavy = (mass >= 100)

    mapping = {
        (0,0): "Neither",
        (1,0): "Bulky",
        (0,1): "Heavy",
        (1,1): "Both"
    }

    return mapping[(bulky, heavy)]
```

#### 💻 Implementation

```cpp
// Most elegant solution with mapping
class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        long long volume = 1LL * length * width * height;
        bool bulky = (length >= 1e4 || width >= 1e4 || height >= 1e4 || volume >= 1e9);
        bool heavy = (mass >= 100);

        if (!bulky && !heavy) return "Neither";
        if (bulky && !heavy) return "Bulky";
        if (!bulky && heavy) return "Heavy";
        return "Both";
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                                    |
| -------------- | --------------- | ---------------- | ------------------------------- | --------------------------------------- |
| 🥉 Brute Force | O(1)            | O(1)             | Very simple, easy to understand | Code is verbose with many `if-else`     |
| 🥈 Optimized   | O(1)            | O(1)             | Cleaner, extensible with flags  | Requires understanding of flag encoding |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, most maintainable     | Essentially same logic as brute force   |

## 🎯 Why This is Optimal?

- All approaches run in O(1) → cannot be improved further.
  = The Optimal approach uses mapping → cleaner, scalable, easier to maintain.
- It avoids deep nesting and multiple redundant if-else.

### 🔑 Key Insights

| #   | Insight                                                   |
| --- | --------------------------------------------------------- |
| 1   | The problem reduces to checking two boolean conditions.   |
| 2   | Only 4 possible outcomes exist.                           |
| 3   | Flags/mapping make the code cleaner and easier to extend. |

### 💭 Common Mistakes to Avoid

| #   | Mistake                  | Description                         | How to Avoid      | Example                |
| --- | ------------------------ | ----------------------------------- | ----------------- | ---------------------- |
| 1   | Using `int` for volume   | Volume may exceed `int`             | Use `long long`   | `1LL * l * w * h`      |
| 2   | Missing bulky condition  | Checked only dimensions, not volume | Always check both | `1000*1000*1000`       |
| 3   | Returning wrong category | Confusing `"Both"` with `"Bulky"`   | Use clear mapping | `(bulky, heavy)` table |

### 🐛 Implementation Mistakes

| #   | Mistake                     | Description                        | How to Avoid               | Example           |     |        |     |           |
| --- | --------------------------- | ---------------------------------- | -------------------------- | ----------------- | --- | ------ | --- | --------- |
| 1   | Overflow in volume          | `int` overflow at large dimensions | Use `long long`            | `1LL * a * b * c` |     |        |     |           |
| 2   | Not checking all dimensions | Only checked length                | Apply OR on all dimensions | \`(l>=1e4         |     | w>=1e4 |     | h>=1e4)\` |
| 3   | Wrong threshold             | Typo: `1000` instead of `10000`    | Double-check constants     | ≥ 1e4, ≥ 1e9      |     |        |     |           |

### 💭 Logical Thinking Mistakes

| #   | Mistake                   | Description                    | How to Avoid        | Prevention      |
| --- | ------------------------- | ------------------------------ | ------------------- | --------------- |
| 1   | Using AND instead of OR   | Problem states "any dimension" | Re-read carefully   | `(a OR b OR c)` |
| 2   | Forgetting "Neither" case | Did not return if both false   | Always handle all 4 | Mapping table   |
| 3   | Boundary errors           | Misinterpreting ≥ vs >         | Test edge cases     | volume = 1e9    |

### 🎯 Patterns & Techniques Used

| #   | Pattern / Technique | Application                       |
| --- | ------------------- | --------------------------------- |
| 1   | Boolean flagging    | Mark bulky/heavy                  |
| 2   | Mapping table       | Map `(bulky, heavy)` to category  |
| 3   | Defensive coding    | Use `long long` to avoid overflow |

### 🔄 Follow-up Questions

| #   | Question                                      | Answer / Approach                 |
| --- | --------------------------------------------- | --------------------------------- |
| 1   | What if we add a new category like "Fragile"? | Extend mapping/flag system easily |
| 2   | What if we need to process millions of boxes? | Still O(1) per box → O(n) overall |
| 3   | Can we remove all `if-else`?                  | Yes, by using dictionary mapping  |

---

<div align="center">

**🎯 Problem 2525 Completed!**

_Happy Coding! 🚀_

</div>
