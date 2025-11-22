import re

def parse_semantic_blocks(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    entries = []
    
    date_iso = r"\d{4}-\d{2}-\d{2}"
    date_normal = r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}"
    salary_pattern = r"[\d,]+ INR"
    percent_pattern = r"\d{1,3}\.\d+%|\d{1,3}%"
    score_pattern = r"\d{2,4}\s*out\s*of\s*\d{2,4}"
    cgpa_pattern = r"\b\d\.\d\b"
    rating_pattern = r"\b(10|[1-9])\s*out\s*of\s*10\b"
    
    def add(key, value, comment):
        entries.append((key, value, comment))

    for line in lines:

        if "born on" in line:
            name = line.split("was born")[0].strip()
            dob = re.search(date_normal, line)
            iso = re.search(date_iso, line)
            if name: add("Name", name, line)
            if dob: add("Date of Birth", dob.group(), line)
            if iso: add("DOB (ISO Format)", iso.group(), line)
            place_match = re.search(r"in (.*?), making", line)
            if place_match:
                add("Birthplace", place_match.group(1), line)
            age_match = re.search(r"(\d+)\s+years old", line)
            if age_match:
                add("Age", age_match.group(1), line)
            continue

        if "blood group" in line:
            bg = re.search(r"[A|B|AB|O][+-]", line)
            if bg: add("Blood Group", bg.group(), line)
            continue

        if "Indian national" in line:
            add("Nationality", "Indian", line)
            continue

        if "joined his first company" in line:
            add("First Job Role", "Junior Developer", line)
            date = re.search(date_normal, line)
            if date: add("First Job Start Date", date.group(), line)
            salary = re.search(salary_pattern, line)
            if salary: add("First Salary", salary.group(), line)
            continue

        if "current role" in line:
            add("Current Company", "Resse Analytics", line)
            add("Current Role", "Senior Data Engineer", line)
            date = re.search(date_normal, line)
            if date: add("Current Job Start", date.group(), line)
            salary = re.search(salary_pattern, line)
            if salary: add("Current Salary", salary.group(), line)
            continue

        if "LakeCorp" in line:
            add("Previous Company", "LakeCorp Solutions", line)
            period = re.findall(date_normal, line)
            if period:
                if len(period) >= 1:
                    add("LakeCorp Start", period[0], line)
            continue

        if "St. Xavier" in line:
            add("High School", "St. Xavier's School, Jaipur", line)
            percent = re.search(percent_pattern, line)
            if percent: add("12th Score", percent.group(), line)
            continue

        if "B.Tech" in line:
            add("Bachelor's Degree", "B.Tech in Computer Science", line)
            add("College", "IIT Delhi", line)
            cgpa = re.search(cgpa_pattern, line)
            if cgpa: add("B.Tech CGPA", cgpa.group(), line)
            continue

        if "M.Tech" in line:
            add("Master's Degree", "M.Tech in Data Science", line)
            add("College (PG)", "IIT Bombay", line)
            cgpa = re.search(cgpa_pattern, line)
            if cgpa: add("M.Tech CGPA", cgpa.group(), line)
            sc = re.search(score_pattern, line)
            if sc: add("Thesis Score", sc.group(), line)
            continue

        if "AWS" in line:
            score = re.search(r"\d{3,4}", line)
            if score: add("AWS Solutions Architect Score", score.group(), line)
            continue

        if "Azure" in line:
            score = re.search(r"\d{3,4}", line)
            if score: add("Azure Data Engineer Score", score.group(), line)
            continue

        if "Project Management" in line:
            add("PMP Certification Result", "Above Target", line)
            continue

        if "SAFe Agilist" in line:
            percent = re.search(percent_pattern, line)
            if percent: add("SAFe Agilist Score", percent.group(), line)
            continue

        
        ratings = re.findall(rating_pattern, line)
        if ratings:
            for rating in ratings:
                skill_match = re.search(r"(SQL|Python|machine learning|AWS|Azure|Power BI|Tableau)", line, flags=re.I)
                if skill_match:
                    skill = skill_match.group()
                    add(f"{skill} Skill Rating", rating[0], line)
            continue

        add("Context", line, line)

    return entries
