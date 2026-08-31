"""
Exports the `jobs` table from scout.db into jobs.json,
so the HTML/CSS/JS UI can load it with fetch().

Run this any time you scrape new jobs and want the UI to reflect them:
    python export_jobs.py
"""

import sqlite3
import json

conn = sqlite3.connect("scout.db")
cursor = conn.cursor()

cursor.execute("SELECT id, title, company, location, job_type, salary, requirements, url FROM jobs")
rows = cursor.fetchall()

jobs = []
for row in rows:
    id_, title, company, location, job_type, salary, requirements, url = row
    jobs.append({
        "id": id_,
        "title": title,
        "company": company,
        "location": location,
        "job_type": job_type,
        "salary": salary.replace("\n", " ").strip() if salary else salary,
        "requirements": json.loads(requirements) if requirements else {},
        "url": url,
    })

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=2, ensure_ascii=False)

print(f"Exported {len(jobs)} jobs to jobs.json")
conn.close()
