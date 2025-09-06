import os

def clean_filename(title):
    """Làm sạch tên file, loại bỏ ký tự không hợp lệ"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    return title.replace(' ', '_')

def get_difficulty_badge(difficulty):
    """Tạo badge màu sắc cho độ khó"""
    colors = {
        'Easy': '🟢',
        'Medium': '🟡', 
        'Hard': '🔴'
    }
    return f"{colors.get(difficulty, '⚪')} **{difficulty}**"

def get_frequency_badge(frequency):
    """Tạo badge cho frequency của company"""
    if frequency >= 80:
        return f"🔥 {frequency}%"
    elif frequency >= 60:
        return f"⭐ {frequency}%"
    elif frequency >= 40:
        return f"📈 {frequency}%"
    else:
        return f"📊 {frequency}%"

def generate_problems_files(data, base_folder, base_name):
    """Tạo các file solution cho từng bài toán"""
    
    # Lặp qua từng bài trong list JSON
    for item in data:
        qid = item["questionFrontendId"]
        title = item["title"]
        clean_title = clean_filename(title)

        difficulty = item.get("difficulty", "Unknown")

        # Xử lý topicTags -> mỗi bài có thể nhiều tag, chọn tag đầu tiên làm folder chính
        topics = item.get("topicTags", [])
        topic_name = topics[0]['name'] if topics else "Misc"

        # Nếu base_folder đã trỏ thẳng vào Problems/, thì thêm topic_name
        topic_folder = base_folder

        # Folder con theo độ khó
        diff_folder = os.path.join(topic_folder, difficulty)
        os.makedirs(diff_folder, exist_ok=True)

        filename = f"{qid}_{clean_title}.md"
        filepath = os.path.join(diff_folder, filename)
        
        # Tạo URL cho LeetCode problem
        title_slug = item.get("titleSlug", title.lower().replace(" ", "-"))
        leetcode_url = f"https://leetcode.com/problems/{title_slug}/"
        
        with open(filepath, "w", encoding="utf-8") as f:
            # Header với styling đẹp
            f.write(f"<div align=\"center\">\n\n")
            f.write(f"# 🧠 [{qid}. {title}]({leetcode_url})\n\n")
            f.write(f"[![LeetCode](<https://img.shields.io/badge/LeetCode-Problem%20{qid}-FFA116?style=for-the-badge&logo=leetcode&logoColor=white>)]({leetcode_url})\n\n")
            f.write(f"</div>\n\n")
            f.write("---\n\n")
            
            # Tags section với styling đẹp
            if item.get("topicTags"):
                f.write("## 🏷️ Topics & Tags\n\n")
                f.write("<div align=\"center\">\n\n")
                for tag in item.get("topicTags", []):
                    f.write(f"![{tag['name']}](https://img.shields.io/badge/-{tag['name'].replace(' ', '%20')}-blue?style=flat-square) ")
                f.write("\n\n</div>\n\n")

            # Problem Overview với styling
            f.write("## 📋 Problem Overview\n\n")
            f.write("| Property | Value |\n")
            f.write("|----------|-------|\n")
            f.write(f"| **Difficulty** | {get_difficulty_badge(item['difficulty'])} |\n")
            f.write(f"| **Acceptance Rate** | `{item['acRate']:.1f}%` |\n")
            f.write(f"| **Problem Link** | [Open in LeetCode]({leetcode_url}) |\n")
            
            # Progress Tracking Section
            f.write("## ⏰ Progress Tracking\n\n")
            f.write("| Status | Date | Notes |\n")
            f.write("|--------|------|-------|\n")
            f.write("| 🎯 **Attempted** | `DD-MM-YYYY` | First attempt, understanding the problem |\n")
            f.write("| ✅ **Solved** | `DD-MM-YYYY` | Successfully implemented solution |\n")
            f.write("| 🔄 **Review 1** | `DD-MM-YYYY` | First review, optimization |\n")
            f.write("| 🔄 **Review 2** | `DD-MM-YYYY` | Second review, different approaches |\n")
            f.write("| 🔄 **Review 3** | `DD-MM-YYYY` | Final review, mastery |\n\n")
            
            # Similar Questions với table đẹp
            similar_questions = item.get("similarQuestions", [])
            if similar_questions:
                f.write("## 🔗 Related Problems\n\n")
                f.write("| Problem | Difficulty | Relationship |\n")
                f.write("|---------|------------|-------------|\n")
                for i, sq in enumerate(similar_questions):
                    sq_url = f"https://leetcode.com/problems/{sq['titleSlug']}/"
                    difficulty_badge = get_difficulty_badge(sq['difficulty'])
                    relationship = "Similar logic" if i == 0 else "Related concept"
                    f.write(f"| [{sq['title']}]({sq_url}) | {difficulty_badge} | {relationship} |\n")
                f.write("\n")
            
            # Companies section với frequency badges
            companies = item.get("companies", [])
            if companies:
                f.write("## 🏢 Companies Asked (Frequency)\n\n")
                
                # Sort companies by frequency
                sorted_companies = sorted(companies, key=lambda x: x['frequency'], reverse=True)
                
                f.write("### 🔥 High Frequency (80%+)\n")
                high_freq = [c for c in sorted_companies if c['frequency'] >= 80]
                if high_freq:
                    for comp in high_freq:
                        f.write(f"- **{comp['name']}** {get_frequency_badge(comp['frequency'])}\n")
                else:
                    f.write("*No high frequency companies*\n")
                f.write("\n")
                
                f.write("### ⭐ Medium Frequency (60-79%)\n")
                med_freq = [c for c in sorted_companies if 60 <= c['frequency'] < 80]
                if med_freq:
                    for comp in med_freq:
                        f.write(f"- **{comp['name']}** {get_frequency_badge(comp['frequency'])}\n")
                else:
                    f.write("*No medium frequency companies*\n")
                f.write("\n")
                
                f.write("### 📈 Regular Frequency (40-59%)\n")
                reg_freq = [c for c in sorted_companies if 40 <= c['frequency'] < 60]
                if reg_freq:
                    for comp in reg_freq:
                        f.write(f"- **{comp['name']}** {get_frequency_badge(comp['frequency'])}\n")
                else:
                    f.write("*No regular frequency companies*\n")
                f.write("\n")
                
                # Show low frequency in collapsed section
                low_freq = [c for c in sorted_companies if c['frequency'] < 40]
                if low_freq:
                    f.write("📊 Low Frequency Companies\n")
                    for comp in low_freq:
                        f.write(f"- **{comp['name']}** {get_frequency_badge(comp['frequency'])}\n")
            
            # Solution template với multiple approaches
            f.write("---\n\n")
            f.write("## 💡 Solutions\n\n")
            
            # Approach 1 - Brute Force
            f.write("### 🥉 Approach 1: Brute Force\n\n")
            f.write("#### 📝 Intuition\n")
            f.write("> Mô tả ý tưởng đơn giản nhất để giải quyết bài toán\n\n")
            
            f.write("#### 🔍 Algorithm\n")
            f.write("```pseudo\n")
            f.write("// Write your pseudocode here\n")
            f.write("```\n\n")

            
            f.write("#### 💻 Implementation\n\n")
            f.write("```cpp\n")
            f.write("// Brute force approach\n")
            f.write("\n")
            f.write("class Solution {\n")
            f.write("public:\n")
            f.write("    int solutionBruteForce(vector<int>& nums) {\n")
            f.write("        // Implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("};\n")
            f.write("```\n\n")
            
            # Approach 2 - Optimized
            f.write("### 🥈 Approach 2: Optimized Solution\n\n")
            f.write("#### 📝 Intuition\n")
            f.write("> Mô tả cách tối ưu hóa từ approach đầu tiên\n\n")
            
            f.write("#### 🔍 Algorithm\n")
            f.write("```pseudo\n")
            f.write("// Write your pseudocode here\n")
            f.write("```\n\n")
            
            f.write("#### 💻 Implementation\n\n")
            f.write("```cpp\n")
            f.write("// Optimized approach with better complexity\n")
            f.write("\n")
            f.write("class Solution {\n")
            f.write("public:\n")
            f.write("    int solutionOptimized(vector<int>& nums) {\n")
            f.write("        // Optimized implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("};\n")
            f.write("```\n\n")

            # Approach 3 - Best Solution
            f.write("### 🥇 Approach 3: Optimal Solution ⭐\n\n")
            f.write("#### 📝 Intuition\n")
            f.write("> Mô tả giải pháp tốt nhất, elegant nhất\n\n")

            f.write("#### 🔍 Algorithm\n")
            f.write("```pseudo\n")
            f.write("// Write your pseudocode here\n")
            f.write("```\n\n")

            f.write("#### 💻 Implementation\n\n")
            f.write("```cpp\n")
            f.write("// Most optimal and elegant solution\n")
            f.write("\n")
            f.write("class Solution {\n")
            f.write("public:\n")
            f.write("    int solutionOptimal(vector<int>& nums) {\n")
            f.write("        // Optimal implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("};\n")
            f.write("```\n\n")

            # So sánh các approaches
            f.write("## 📊 Comparison of Approaches\n\n")

            f.write("| Approach | Time Complexity | Space Complexity | Pros | Cons |\n")
            f.write("|----------|-----------------|------------------|------|------|\n")
            f.write("| 🥉 Brute Force | O(?) | O(?) | ... | ... |\n")
            f.write("| 🥈 Optimized   | O(?) | O(?) | ... | ... |\n")
            f.write("| 🥇 Optimal ⭐  | O(?) | O(?) | ... | ... |\n")
            f.write("|  ...            | .... | ... | ... | ... |\n\n")

            # Kết luận vì sao Optimal
            f.write("## 🎯 Why This is Optimal?\n")
            f.write("- So sánh nhanh với brute force và optimized\n")
            f.write("- Nêu rõ cách tối ưu được cả time/space\n")
            f.write("- Giải thích tại sao đây là giải pháp clean và scalable nhất\n\n")

            
            # Learning Notes            
            f.write("### 🔑 Key Insights\n")
            f.write("| # | Insight |\n")
            f.write("|---|---------|\n")
            f.write("| 1 |Điểm quan trọng số 1|\n")
            f.write("| 2 |Điểm quan trọng số 2|\n")
            f.write("| 3 |Điểm quan trọng số 3|\n")
            f.write("| ... | Thêm nếu cần | \n\n")

            f.write("### 💭 Common Mistakes to Avoid\n")
            f.write("| # | Mistake | Description | How to Avoid | Example |\n")
            f.write("|---|---------|-------------|--------------|----------|\n")
            f.write("| 1 |         |             |              |          |\n")
            f.write("| 2 |         |             |              |          |\n")
            f.write("| 3 |         |             |              |          |\n")
            f.write(" ... |   .... |   ....      |  .....       |   ...    |\n\n")

            f.write("### 🐛 Implementation Mistakes\n\n")
            f.write("| # | Mistake | Description | How to Avoid | Example |\n")
            f.write("|---|---------|-------------|--------------|----------|\n")
            f.write("| 1 |         |             |              |          |\n")
            f.write("| 2 |         |             |              |          |\n")
            f.write("| 3 |         |             |              |          |\n")
            f.write(" ... |   .... |   ....      |  .....       |   ...    |\n\n")

            f.write("### 💭 Logical Thinking Mistakes\n\n")
            f.write("| # | Mistake | Description | How to Avoid | Prevention |\n")
            f.write("|---|---------|-------------|--------------|------------|\n")
            f.write("| 1 |         |             |              |          |\n")
            f.write("| 2 |         |             |              |          |\n")
            f.write("| 3 |         |             |              |          |\n")
            f.write(" ... |   .... |   ....      |  .....       |   ...    |\n\n")

            f.write("### 🎯 Patterns & Techniques Used\n")
            f.write("| # | Pattern / Technique | Application |\n")
            f.write("|---|---------------------|-------------|\n")
            f.write("| 1 |                     |             |\n")
            f.write("| 2 |                     |             |\n")
            f.write("| 3 |                     |             |\n")
            f.write(" ... |   ....             | ...         |\n\n")

            f.write("### 🔄 Follow-up Questions\n")
            f.write("| # | Question | Answer / Approach |\n")
            f.write("|---|----------|-------------------|\n")
            f.write("| 1 |          |                   |\n")
            f.write("| 2 |          |                   |\n")
            f.write(" ... |   .... |   ....             |\n\n")

            # Footer
            f.write("---\n\n")
            f.write("<div align=\"center\">\n\n")
            f.write(f"**🎯 Problem {qid} Completed!**\n\n")
            f.write("*Happy Coding! 🚀*\n\n")
            f.write("</div>\n")
    
    print(f"✅ Generated {len(data)} solution files in: {base_folder}")