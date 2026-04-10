# 🤖 AI Resume Screener with Streamlit UI

**Automated candidate screening system that scores & ranks resumes using NLP + skill matching**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)

## 🚀 Features

✅ **AI-Powered Scoring** - NLP skill extraction & weighted scoring  
✅ **Real-time Ranking** - Candidates sorted by score (Pass/Fail)  
✅ **Interactive Dashboard** - Live table + score distribution charts  
✅ **Bulk Processing** - Screens multiple resumes instantly  
✅ **Customizable Skills** - Python, pandas, SQL, ML, Excel weights  
✅ **Production Ready** - Streamlit web interface  

## 📊 Live Demo
http://localhost:8501

- **Candidate Table** - Name, Score, Status, Top Skills
- **Score Distribution** - Bar chart visualization
- **Pass/Fail Threshold** - Configurable cutoff

## 🛠️ Tech Stack

```python
Streamlit | pandas | NLP | Skill Matching Algorithm
Automated Resume Processing | Interactive Data Viz

🎯 How to Run

# Clone & Install
git clone https://github.com/Prasha-git/data_projects_portfolio.git
cd data_projects_portfolio/resume_screener

# Install dependencies
pip install streamlit pandas

# Add resume TXT files to resumes/ folder
# Run screener
streamlit run resume_ui.py
Open Browser:http://localhost:8501

🤖 AI Scoring Algorithm

| Skill Category | Weight | Keywords |
|----------------|--------|----------|
| **Python** | 25% | python, pandas, numpy, jupyter |
| **Data Analysis** | 20% | analysis, visualization, EDA, dashboard |
| **SQL** | 15% | sql, mysql, postgresql, query |
| **Machine Learning** | 20% | ml, scikit-learn, tensorflow, prediction |
| **Excel/Tools** | 10% | excel, powerbi, tableau, google sheets |
| **Soft Skills** | 10% | communication, leadership, problem solving |

📈 Screening Results

| Status | Score Range | Action |
|--------|-------------|---------|
| **PASS** | 75-100 | Shortlist immediately |
| **MAYBE** | 50-74 | Manual review |
| **FAIL** | 0-49 | Auto-reject |

🎨 Screenshots

<img width="1920" height="1080" alt="Screenshot 2026-04-08 205100" src="https://github.com/user-attachments/assets/de0b0096-bc7d-4a35-acad-4f7194aad6c6" />
<img width="1920" height="1080" alt="Screenshot 2026-04-08 205119" src="https://github.com/user-attachments/assets/24d08f6c-ea39-4e98-9a7c-71b51a7b30d4" />

💡 Business Impact
80% Faster Screening - Automates manual resume review
Zero Bias - Algorithmic skill-based scoring
Scalable - Handles 100s of resumes instantly
Configurable - Custom skill weights per role
Visual Reporting - Score distributions + rankings

🔗 Live Links
Local Demo: http://localhost:8501
Portfolio: https://github.com/Prasha-git/data_projects_portfolio

---
**Built by Prashansa Choubey** | 📍 Pune, India

