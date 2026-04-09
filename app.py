import streamlit as st
import os
import shutil

# 1) Paths
RESUMES_DIR   = "resumes"
PASSED_DIR    = "passed_candidates"
FAILED_DIR    = "failed_candidates"

# 2) Skill weights (same as your screener)
SKILL_WEIGHTS = {
    "python":        20,
    "pandas":        20,
    "data analysis": 15,
    "excel":         10,
}

# 3) Function to score one resume
def score_resume(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
    except:
        return 0, []

    total_score = 0
    skills_found = []
    for keyword, weight in SKILL_WEIGHTS.items():
        if keyword in content:
            total_score += weight
            skills_found.append(keyword)

    return total_score, skills_found

# 4) Streamlit app
st.title("Resume Screener UI")

st.write("This page shows all resumes from the `resumes/` folder with scores and status.")

candidates = []

for filename in os.listdir(RESUMES_DIR):
    filepath = os.path.join(RESUMES_DIR, filename)
    if not os.path.isfile(filepath):
        continue

    score, skills = score_resume(filepath)

    if score >= 30:
        status = "passed"
        target_folder = PASSED_DIR
    else:
        status = "failed"
        target_folder = FAILED_DIR

    # Optional: you can still move files if you want
    # target_path = os.path.join(target_folder, filename)
    # if not os.path.exists(target_path):
    #     shutil.copy(filepath, target_path)

    candidates.append({
        "Name": filename,
        "Score": score,
        "Status": status,
        "Skills": ", ".join(skills)
    })

# 5) Sort by score (highest first)
import pandas as pd
df = pd.DataFrame(candidates)
df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)
df.index += 1  # 1‑based ranking

st.write("### Ranked Candidate List")
st.dataframe(df)

st.write("### Score Distribution")
st.bar_chart(df.set_index("Name")["Score"])