# LinkedIn Job Postings (2023–2024): Skills Demand & Salary Trends

## Dataset
- Source: LinkedIn Job Postings (2023–2024), Kaggle (arshkon/linkedin-job-postings)
- Raw size: 123,849 postings, 31 columns
- After cleaning: 120,503 postings, 26 columns (dropped 5 columns >80% null: `med_salary`, `applies`, `remote_allowed`, `closed_time`, `skills_desc`; dropped rows missing `company_name`/`company_id`/`views`; mode-filled `formatted_experience_level`)
- 0 duplicate rows found

## Data Quality Notes
- ~76% of postings have no disclosed salary — treated as missing, not imputed (fabricating pay data would distort analysis)
- Found and removed corrupted `normalized_salary` values: some rows exceeded $500M due to a `BIWEEKLY` pay-period conversion bug in the source data (only 7 rows, dropped)
- Applied a $2M domain cap on salary to remove remaining data-entry errors (32 rows dropped) — chose a domain cap over IQR since salary is naturally right-skewed and IQR would have cut legitimate high earners
- Location-based salary rankings required a minimum sample size filter (≥20 postings) — single-posting locations produced misleading medians (e.g., a 2-posting town outranking Chicago)

## Finding 1: Salary by Experience Level
Clear, expected gradient — validates data integrity:

| Level | Median Salary |
|---|---|
| Executive | $193,750 |
| Director | $167,206 |
| Mid-Senior | $107,500 |
| Associate | $72,800 |
| Entry level | $52,213 |
| Internship | $48,880 |

## Finding 2: Top-Paying Locations (filtered, ≥20 postings)
Bay Area dominance, consistent with known tech-salary geography:
San Mateo, Mountain View, Foster City, Sunnyvale, San Francisco Bay Area, Palo Alto, Santa Clara — all in top 15.

## Finding 3: Skills in Demand (by posting volume)
Broad job-function categories, not granular tool-level skills (data limitation — `skills.csv` tags are functional categories like "Information Technology," not specific tools like "Python"):

1. Information Technology — 26,137 postings
2. Sales — 22,475
3. Management — 20,861
4. Manufacturing — 18,185
5. Health Care Provider — 17,369

## Finding 4: Highest-Paying Skill Categories (≥500 postings, salary-cleaned)
1. Product Management — $150,400 median
2. Engineering — $132,080
3. Strategy/Planning — $125,900
4. Legal — $125,000
5. Information Technology — $120,000

## Takeaway
Demand and pay don't fully align: IT and Sales dominate volume, but Product Management, Engineering, and Strategy/Planning command the highest pay despite lower posting counts — suggesting a supply/demand premium for specialized functional roles over high-volume categories.

## Limitations
- Skill tags are broad functional categories, not specific technical skills
- Salary data self-reported by posters; ~76% of postings omit it entirely, so findings reflect only the disclosed subset
- Dataset is a single 2023–2024 snapshot, not longitudinal (no true trend-over-time yet — planned as next step)