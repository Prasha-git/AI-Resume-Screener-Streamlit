import os
import shutil

# 1) Folders
RESUMES_DIR   = "resumes"
PASSED_DIR    = "passed_candidates"
FAILED_DIR    = "failed_candidates"

# 2) Skill keywords with weights (you can change these)
SKILL_WEIGHTS = {
    "python":        20,
    "pandas":        20,
    "data analysis": 15,
    "excel":         10,
    # add more skills later
}

# 3) Create output folders
os.makedirs(PASSED_DIR, exist_ok=True)
os.makedirs(FAILED_DIR, exist_ok=True)

# 4) For each resume
candidates = []  # store name, score, status, skills

for filename in os.listdir(RESUMES_DIR):
    filepath = os.path.join(RESUMES_DIR, filename)

    if not os.path.isfile(filepath):
        continue

    # Read file
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        continue

    # 5) Count score and found skills
    total_score = 0
    skills_found = []
    for keyword, weight in SKILL_WEIGHTS.items():
        if keyword in content:
            total_score += weight
            skills_found.append(keyword)

    # 6) Decide status
    if total_score >= 20:  # 20+ points → passed
        status = "passed"
        target_folder = PASSED_DIR
    else:
        status = "failed"
        target_folder = FAILED_DIR

    # 7) Move file
    target_path = os.path.join(target_folder, filename)
    shutil.copy(filepath, target_path)

    # 8) Save candidate info
    candidates.append({
        "name": filename,
        "score": total_score,
        "status": status,
        "skills": skills_found
    })


# 9) Print score for each resume before ranking
print("DEBUG: Each resume score")
print("-" * 40)

for c in candidates:
    print(f"{c['name']:<20} | Score: {c['score']:3d} | Status: {c['status']:<8}")

print("" + "="*60)
print("RANKED CANDIDATE LIST")
print("="*60)

# 10) Sort by score (highest first → rank 1, 2, 3...)
candidates.sort(key=lambda x: x["score"], reverse=True)

for i, c in enumerate(candidates, start=1):
    print(f"{i:2d}. {c['name']:<20} | Score: {c['score']:3d} | Status: {c['status']:<8} | Skills: {c['skills']}")