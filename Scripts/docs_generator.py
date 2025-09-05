import os
from datetime import datetime

def get_difficulty_badge(difficulty):
    """Tạo badge màu sắc cho độ khó"""
    colors = {
        'Easy': '🟢',
        'Medium': '🟡', 
        'Hard': '🔴'
    }
    return f"{colors.get(difficulty, '⚪')} **{difficulty}**"

def clean_filename(title):
    """Làm sạch tên file, loại bỏ ký tự không hợp lệ"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    return title.replace(' ', '_')

def generate_docs_file(data, docs_file, base_name, json_file):
    """Tạo file documentation tổng hợp"""
    
    current_date = datetime.now().strftime("%d-%m-%Y")
    format_date = current_date.replace("-", "--")
    
    with open(docs_file, "w", encoding="utf-8") as f:
        f.write("<div align=\"center\">\n\n")
        f.write(f"# 📊 {base_name} - LeetCode Progress Tracker\n\n")
        f.write(f"![Problems](https://img.shields.io/badge/Total%20Problems-{len(data)}-blueviolet?style=for-the-badge&logo=leetcode)\n")
        f.write(f"![Progress](https://img.shields.io/badge/Completed-0%2F{len(data)}-critical?style=for-the-badge&logo=github)\n")
        f.write(f"![Last Updated](https://img.shields.io/badge/Last%20Updated-{format_date}-success?style=for-the-badge&logo=git)\n\n")
        f.write("</div>\n\n")
        f.write("---\n\n")
        
        # Table of Contents
        f.write("## 📑 Table of Contents\n\n")
        f.write("1. [📈 Progress Statistics](#-progress-statistics)\n")
        f.write("2. [🏢 Top Companies by Question Frequency](#-top-companies-by-question-frequency)\n")
        f.write("3. [📋 Problems Progress Tracker](#-problems-progress-tracker)\n")
        f.write("4. [📖 How to Use This Tracker](#-how-to-use-this-tracker)\n\n")
        
        # Statistics
        difficulty_stats = {}
        for item in data:
            diff = item['difficulty']
            difficulty_stats[diff] = difficulty_stats.get(diff, 0) + 1
        
        f.write("## 📈 Progress Statistics\n\n")
        f.write("| Difficulty | Total | Solved | Remaining | Progress |\n")
        f.write("|------------|-------|--------|-----------|----------|\n")
        for diff in ['Easy', 'Medium', 'Hard']:
            if diff in difficulty_stats:
                count = difficulty_stats[diff]
                badge = get_difficulty_badge(diff)
                f.write(f"| {badge} | `{count}` | `0` | `{count}` | ![Progress Bar](https://progress-bar.xyz/0/?title=Progress&width=150&color=green) |\n")
        f.write("\n")
        
        # Company frequency analysis
        f.write("## 🏢 Top Companies by Question Frequency\n\n")
        company_freq = {}
        for item in data:
            for comp in item.get("companies", []):
                if comp['name'] not in company_freq:
                    company_freq[comp['name']] = []
                company_freq[comp['name']].append(comp['frequency'])
        
        # Calculate average frequency per company
        company_avg = {}
        for company, freqs in company_freq.items():
            company_avg[company] = sum(freqs) / len(freqs)
        
        sorted_companies = sorted(company_avg.items(), key=lambda x: (len(company_freq[x[0]]), x[1]), reverse=True)[:10]
        
        f.write("| Rank | Company | Questions | Avg Frequency | Total Score |\n")
        f.write("|------|---------|-----------|---------------|-------------|\n")
        for i, (company, avg_freq) in enumerate(sorted_companies, 1):
            question_count = len(company_freq[company])
            total_score = question_count * avg_freq
            f.write(f"| {i} | **{company}** | `{question_count}` | `{avg_freq:.1f}%` | `{total_score:.1f}` |\n")
        f.write("\n")
        
        # Problems tracking table
        f.write("## 📋 Problems Progress Tracker\n\n")
        f.write("| # | Problem | Difficulty | Status | Completed | Review 1 | Review 2 | Review 3 | Notes |\n")
        f.write("|---|---------|------------|--------|-----------|----------|----------|----------|-------|\n")
        
        for item in data:
            qid = item["questionFrontendId"]
            title = item["title"]
            title_slug = item.get("titleSlug", title.lower().replace(" ", "-"))
            leetcode_url = f"https://leetcode.com/problems/{title_slug}/"
            difficulty_badge = get_difficulty_badge(item['difficulty'])
            
            # Create link to solution file
            clean_title = clean_filename(title)
            solution_file = f"{qid}_{clean_title}.md"
            solution_link = f"Solutions/{base_name}/{solution_file}"
            
            f.write(f"| {qid} | [{title}]({solution_link}) | {difficulty_badge} | ⏳ | `____-__-__` | `____-__-__` | `____-__-__` | `____-__-__` |  |  |\n")
        
        f.write("\n")
        
        # Legend and Instructions
        f.write("## 📖 How to Use This Tracker\n\n")
        f.write("### Status Icons\n")
        f.write("- ⏳ **Pending** - Not started\n")
        f.write("- 🔄 **In Progress** - Currently working on\n")
        f.write("- ✅ **Completed** - Successfully solved\n")
        f.write("- 🎯 **Mastered** - Fully understood and optimized\n")
        f.write("- 🔴 **Stuck** - Need help or hints\n")
        f.write("- ⚠️ **Review Needed** - Solution works but needs optimization\n\n")
        
        f.write("### Date Format\n")
        f.write("- Use format: ``DD-MM-YYYY``\n")
        f.write("- **Completed:** Date when you first solved the problem\n")
        f.write("- **Review 1:** First review (1-2 weeks after completion)\n")
        f.write("- **Review 2:** Second review (1 month after completion)\n")
        f.write("- **Review 3:** Final review (3 months after completion)\n\n")
        
        f.write("---\n\n")
        f.write("<div align=\"center\">\n\n")
        f.write(f"*Generated on {format_date} from `{os.path.basename(json_file)}`*\n\n")
        f.write("**Happy Coding! 🚀 Learn from Mistakes! 📈 Keep Going! 💪**\n\n")
        f.write("</div>\n")
    
    print(f"✅ Generated documentation file: {docs_file}")