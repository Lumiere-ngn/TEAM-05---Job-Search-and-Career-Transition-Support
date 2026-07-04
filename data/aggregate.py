#!/usr/bin/env python3
"""Aggregate raw Hugging Face job data into skills_by_role.csv and roles.csv."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
OUT = ROOT

# Target roles shown in the UI (mapped from Mindweave role_family + title keywords)
ROLES = [
    "Data Analyst",
    "Software Engineer",
    "Product Manager",
    "Sales",
    "Customer Success",
    "Operations",
]

# Mindweave role_family -> canonical role (fallback when title keywords do not match)
MINDWEAVE_ROLE_FAMILY_HINTS: dict[str, str] = {
    "data": "Data Analyst",
    "engineering": "Software Engineer",
    "product": "Product Manager",
    "sales": "Sales",
    "customer_success": "Customer Success",
    "operations": "Operations",
}

ROLE_PATTERNS: dict[str, list[str]] = {
    "Data Analyst": [
        r"data analyst",
        r"business analyst",
        r"analytics analyst",
        r"reporting analyst",
        r"bi analyst",
        r"business intelligence",
        r"financial analyst",
        r"fp&a analyst",
        r"fp&a\b",
        r"data scientist",
        r"pricing analyst",
        r"compliance analyst",
        r"insights analyst",
    ],
    "Software Engineer": [
        r"software engineer",
        r"software developer",
        r"backend engineer",
        r"frontend engineer",
        r"front[\s-]?end engineer",
        r"full[\s-]?stack",
        r"web developer",
        r"application developer",
        r"devops engineer",
        r"platform engineer",
        r"cloud infrastructure engineer",
        r"ml engineer",
        r"machine learning engineer",
        r"sre\b",
        r"technical support engineer",
    ],
    "Product Manager": [
        r"product manager",
        r"product owner",
        r"technical product manager",
        r"associate product manager",
        r"growth product manager",
        r"growth pm",
        r"\bpm\b",
        r"ux designer",
        r"ui designer",
        r"ui/ux",
        r"product designer",
        r"senior product designer",
        r"interaction designer",
        r"user experience designer",
        r"visual designer",
    ],
    "Sales": [
        r"sales development representative",
        r"\bsdr\b",
        r"\bbdr\b",
        r"business development representative",
        r"business development manager",
        r"regional sales manager",
        r"sales manager",
        r"account executive",
        r"inside sales",
        r"sales representative",
        r"\bsales\b",
    ],
    "Customer Success": [
        r"customer success manager",
        r"customer success specialist",
        r"client success manager",
        r"partner success manager",
        r"customer success\b",
        r"client success\b",
        r"partner success\b",
    ],
    "Operations": [
        r"operations manager",
        r"logistics operations",
        r"supply chain",
        r"talent acquisition",
        r"\brecruiter\b",
        r"recruiting specialist",
        r"project manager",
        r"program manager",
        r"logistics manager",
        r"lifecycle marketing",
        r"solutions consultant",
        r"operations\b",
    ],
}

# Curated skill lexicon per role (matched case-insensitively in title + description)
SKILL_LEXICON: dict[str, list[str]] = {
    "Data Analyst": [
        "SQL",
        "Excel",
        "Python",
        "Tableau",
        "Statistics",
        "Power BI",
        "Data visualization",
        "R",
        "Pandas",
        "ETL",
    ],
    "Software Engineer": [
        "JavaScript",
        "Python",
        "Java",
        "Git",
        "Data structures",
        "REST APIs",
        "SQL",
        "Cloud (AWS)",
        "Testing",
        "React",
        "Docker",
        "Kubernetes",
    ],
    "Product Manager": [
        "Roadmapping",
        "User research",
        "Analytics",
        "SQL",
        "A/B testing",
        "Stakeholder management",
        "Agile",
        "Jira",
        "Product strategy",
        "Wireframing",
        "Figma",
        "Prototyping",
        "Design systems",
    ],
    "Sales": [
        "CRM (Salesforce)",
        "Pipeline management",
        "Prospecting",
        "Negotiation",
        "Lead generation",
        "HubSpot",
        "Cold outreach",
        "Account planning",
        "Quota attainment",
        "Demo skills",
    ],
    "Customer Success": [
        "Onboarding",
        "Retention",
        "Account management",
        "Customer advocacy",
        "Churn reduction",
        "CRM (Salesforce)",
        "Product adoption",
        "Renewals",
        "Upselling",
        "Support escalation",
    ],
    "Operations": [
        "Process improvement",
        "Project management",
        "Logistics",
        "Supply chain",
        "Agile",
        "Excel",
        "Data analysis",
        "Vendor management",
        "KPI tracking",
        "Cross-functional coordination",
    ],
}

# Search terms in posting text (lowercase) -> canonical skill label
SKILL_SEARCH: dict[str, str] = {
    "sql": "SQL",
    "excel": "Excel",
    "python": "Python",
    "tableau": "Tableau",
    "statistics": "Statistics",
    "statistical": "Statistics",
    "power bi": "Power BI",
    "powerbi": "Power BI",
    "data visualization": "Data visualization",
    "data visualisation": "Data visualization",
    "visualization": "Data visualization",
    "visualisation": "Data visualization",
    " pandas": "Pandas",
    " etl": "ETL",
    "javascript": "JavaScript",
    "typescript": "JavaScript",
    " java ": "Java",
    " git": "Git",
    "github": "Git",
    "data structures": "Data structures",
    "data structure": "Data structures",
    "rest api": "REST APIs",
    "restful": "REST APIs",
    " aws": "Cloud (AWS)",
    "amazon web services": "Cloud (AWS)",
    "testing": "Testing",
    "unit test": "Testing",
    " react": "React",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "roadmap": "Roadmapping",
    "road mapping": "Roadmapping",
    "user research": "User research",
    "analytics": "Analytics",
    "a/b test": "A/B testing",
    "ab test": "A/B testing",
    "split test": "A/B testing",
    "stakeholder": "Stakeholder management",
    "agile": "Agile",
    "scrum": "Agile",
    " jira": "Jira",
    "product strategy": "Product strategy",
    "figma": "Figma",
    "wireframe": "Wireframing",
    "wire framing": "Wireframing",
    "prototype": "Prototyping",
    "prototyping": "Prototyping",
    "design system": "Design systems",
    "salesforce": "CRM (Salesforce)",
    " crm": "CRM (Salesforce)",
    "pipeline": "Pipeline management",
    "prospecting": "Prospecting",
    "negotiat": "Negotiation",
    "lead gen": "Lead generation",
    "lead generation": "Lead generation",
    "hubspot": "HubSpot",
    "cold call": "Cold outreach",
    "cold email": "Cold outreach",
    "cold outreach": "Cold outreach",
    "account plan": "Account planning",
    "quota": "Quota attainment",
    "product demo": "Demo skills",
    "demo": "Demo skills",
    "onboarding": "Onboarding",
    "retention": "Retention",
    "account management": "Account management",
    "account manager": "Account management",
    "customer advocacy": "Customer advocacy",
    "churn": "Churn reduction",
    "product adoption": "Product adoption",
    "renewal": "Renewals",
    "upsell": "Upselling",
    "cross-sell": "Upselling",
    "escalation": "Support escalation",
    "process improvement": "Process improvement",
    "continuous improvement": "Process improvement",
    "project management": "Project management",
    "project manager": "Project management",
    "logistics": "Logistics",
    "supply chain": "Supply chain",
    "vendor management": "Vendor management",
    "vendor manag": "Vendor management",
    "kpi": "KPI tracking",
    "key performance": "KPI tracking",
    "cross-functional": "Cross-functional coordination",
    "cross functional": "Cross-functional coordination",
    "data analysis": "Data analysis",
    "accessibility": "Accessibility",
    " a11y": "Accessibility",
    "wcag": "Accessibility",
    "sketch": "Sketch",
    "adobe xd": "Adobe XD",
    "usability test": "Usability testing",
    "information architecture": "Information architecture",
}

LEARN_LINKS: dict[str, str] = {
    "SQL": "SQLBolt + Mode SQL tutorial (free)",
    "Excel": "ExcelJet / Microsoft Learn",
    "Python": "Kaggle 'Python' micro-course (free)",
    "Tableau": "Tableau Public free training videos",
    "Statistics": "Khan Academy Statistics",
    "Power BI": "Microsoft Learn Power BI path",
    "Data visualization": "Storytelling with Data (blog)",
    "Pandas": "Kaggle Pandas micro-course (free)",
    "ETL": "DataCamp ETL fundamentals (free tier)",
    "R": "R for Data Science (free online)",
    "JavaScript": "javascript.info (free)",
    "Java": "Oracle Java Tutorials (free)",
    "Git": "Git 'Learn Branching' interactive",
    "Data structures": "NeetCode roadmap (free)",
    "REST APIs": "MDN HTTP / API docs",
    "Cloud (AWS)": "AWS Skill Builder free tier",
    "Testing": "Testing Library docs",
    "React": "React.dev official tutorial (free)",
    "Docker": "Docker Getting Started guide",
    "Kubernetes": "Kubernetes.io tutorials",
    "Roadmapping": "Reforge / SVPG articles",
    "User research": "NN/g free articles",
    "Analytics": "Amplitude / GA4 free courses",
    "A/B testing": "Optimizely Academy",
    "Stakeholder management": "Lenny's Newsletter (free posts)",
    "Agile": "Scrum.org free learning paths",
    "Jira": "Atlassian University (free)",
    "Product strategy": "Reforge free articles",
    "Figma": "Figma's free interactive courses",
    "Wireframing": "NN/g free articles",
    "Prototyping": "Figma prototyping tutorials",
    "Design systems": "Refactoring UI (concepts)",
    "CRM (Salesforce)": "Trailhead Salesforce Admin (free)",
    "Pipeline management": "Sales Hacker / Gong blog (free)",
    "Prospecting": "LinkedIn Sales Navigator tips (free)",
    "Negotiation": "Chris Voss negotiation summaries (free)",
    "Lead generation": "HubSpot Academy (free)",
    "HubSpot": "HubSpot Academy CRM course (free)",
    "Cold outreach": "Sales Hacker cold email guides",
    "Account planning": "Gartner account planning articles",
    "Quota attainment": "Sales Hacker quota attainment posts",
    "Demo skills": "Demo2Win free resources",
    "Onboarding": "Gainsight Customer Success resources",
    "Retention": "ProfitWell Retain blog (free)",
    "Account management": "Gainsight CS playbook articles",
    "Customer advocacy": "Influitive advocacy guides",
    "Churn reduction": "ChurnZero blog (free)",
    "Product adoption": "Pendo product adoption guides",
    "Renewals": "Gainsight renewal management articles",
    "Upselling": "Gainsight expansion playbook",
    "Support escalation": "ITIL / Zendesk escalation guides",
    "Process improvement": "Lean Six Sigma Yellow Belt (free intro)",
    "Project management": "Google Project Management Certificate (audit free)",
    "Logistics": "Coursera Supply Chain intro (audit free)",
    "Supply chain": "MIT SCM micro-masters preview (free)",
    "Data analysis": "Kaggle Data Analysis micro-course (free)",
    "Vendor management": "CIPS vendor management articles",
    "KPI tracking": "KPI.org free resources",
    "Cross-functional coordination": "Atlassian teamwork guides",
    "Accessibility": "web.dev Accessibility (free)",
    "Sketch": "Sketch Learn (free)",
    "Adobe XD": "Adobe XD tutorials",
    "Usability testing": "NN/g usability testing articles",
    "Information architecture": "NN/g IA basics",
}

EXPERIENCE_MAP = {
    "internship": 0,
    "entry level": 1,
    "entry-level": 1,
    "associate": 2,
    "mid-senior level": 5,
    "mid-senior": 5,
    "director": 10,
    "executive": 12,
}

MAX_LINKEDIN_ROWS = 33246  # full dataset ~33k rows
MAX_INDEED_ROWS = 1000


def normalize_role(title: str, role_family: str | None = None) -> str | None:
    if isinstance(title, str) and title.strip():
        t = title.lower()
        for role, patterns in ROLE_PATTERNS.items():
            for pat in patterns:
                if re.search(pat, t):
                    return role
    if role_family:
        family = str(role_family).strip().lower()
        if family in MINDWEAVE_ROLE_FAMILY_HINTS:
            return MINDWEAVE_ROLE_FAMILY_HINTS[family]
    return None


def text_blob(*parts: str | float | None) -> str:
    return " ".join(str(p).lower() for p in parts if p is not None and str(p) != "nan")


def skills_in_text(text: str, role: str) -> set[str]:
    found: set[str] = set()
    allowed = set(SKILL_LEXICON[role])
    for term, skill in SKILL_SEARCH.items():
        if skill in allowed and term in text:
            found.add(skill)
    return found


def parse_experience_years(value: str | float | None) -> float | None:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return None
    s = str(value).strip().lower()
    for key, years in EXPERIENCE_MAP.items():
        if key in s:
            return float(years)
    m = re.search(r"(\d+)\+?\s*years?", s)
    if m:
        return float(m.group(1))
    return None


def sane_annual_salary(value: float | None) -> float | None:
    if value is None or pd.isna(value):
        return None
    v = float(value)
    if v < 20_000 or v > 1_000_000:
        return None
    return v


def annualize_salary(amount: float | None, period: str | None) -> float | None:
    if amount is None or pd.isna(amount):
        return None
    p = (period or "").upper()
    if p in {"HOURLY", "HOUR"}:
        return float(amount) * 2080
    if p in {"WEEKLY", "WEEK"}:
        return float(amount) * 52
    if p in {"MONTHLY", "MONTH"}:
        return float(amount) * 12
    return float(amount)


def load_linkedin() -> pd.DataFrame:
    path = RAW / "xanderios__linkedin-job-postings" / "job_postings.csv"
    if not path.exists():
        path = None
    if path is None:
        return pd.DataFrame()

    df = pd.read_csv(path, nrows=MAX_LINKEDIN_ROWS, low_memory=False)
    rows = []
    for _, row in df.iterrows():
        title = str(row.get("title", "") or "")
        role = normalize_role(title)
        desc = text_blob(title, row.get("description", ""), row.get("skills_desc", ""))
        if role is None:
            continue
        med = row.get("med_salary")
        salary = annualize_salary(med, row.get("pay_period")) if pd.notna(med) else None
        salary = sane_annual_salary(salary)
        rows.append(
            {
                "source": "linkedin",
                "role": role,
                "title": title,
                "text": desc,
                "experience_years": parse_experience_years(row.get("formatted_experience_level")),
                "salary": salary,
            }
        )
    return pd.DataFrame(rows)


def load_indeed() -> pd.DataFrame:
    path = RAW / "fact-den__indeed-job-postings-2026" / "jobs" / "jobs.csv"
    if not path.exists():
        path = None
    if path is None:
        return pd.DataFrame()

    df = pd.read_csv(path, nrows=MAX_INDEED_ROWS, low_memory=False)
    rows = []
    for _, row in df.iterrows():
        title = str(row.get("title", ""))
        role = normalize_role(title)
        if role is None:
            continue
        desc = text_blob(title, row.get("description", ""), row.get("occupations", ""))
        salary = None
        smin, smax = row.get("salaryMin"), row.get("salaryMax")
        if pd.notna(smin) and pd.notna(smax):
            salary = sane_annual_salary((float(smin) + float(smax)) / 2)
        elif pd.notna(smin):
            salary = sane_annual_salary(float(smin))
        elif pd.notna(smax):
            salary = sane_annual_salary(float(smax))
        smin_val = sane_annual_salary(float(smin)) if pd.notna(smin) else None
        smax_val = sane_annual_salary(float(smax)) if pd.notna(smax) else None
        rows.append(
            {
                "source": "indeed",
                "role": role,
                "title": title,
                "text": desc,
                "experience_years": None,
                "salary": salary,
                "salary_min": smin_val,
                "salary_max": smax_val,
            }
        )
    return pd.DataFrame(rows)


def load_mindweave_applicants() -> dict[str, float]:
    base = RAW / "mindweave__job-postings-applications"
    jobs_path = base / "data" / "jobs.csv"
    apps_path = base / "data" / "applications.csv"
    if not jobs_path.exists() or not apps_path.exists():
        return {}

    jobs = pd.read_csv(jobs_path, low_memory=False)
    apps = pd.read_csv(apps_path, low_memory=False)

    title_col = "job_title" if "job_title" in jobs.columns else "title"
    id_col = "job_id" if "job_id" in jobs.columns else jobs.columns[0]
    app_job_col = "job_id" if "job_id" in apps.columns else apps.columns[0]

    app_counts = apps.groupby(app_job_col).size()
    role_apps: dict[str, list[float]] = defaultdict(list)

    for _, row in jobs.iterrows():
        title = str(row.get(title_col, ""))
        role_family = row.get("role_family")
        family_hint = str(role_family).strip() if pd.notna(role_family) else None
        role = normalize_role(title, role_family=family_hint)
        if role is None:
            continue
        jid = row[id_col]
        count = float(app_counts.get(jid, 0))
        role_apps[role].append(count)

    return {role: float(np.median(vals)) if vals else 0.0 for role, vals in role_apps.items()}


def top_example_titles(subset: pd.DataFrame, limit: int = 6) -> list[str]:
    """Top unique real job titles for a role (LinkedIn/Indeed only)."""
    posting_sources = subset[subset["source"].isin(["linkedin", "indeed"])]
    if posting_sources.empty:
        posting_sources = subset
    titles = posting_sources["title"].dropna().astype(str).str.strip()
    titles = titles[titles != ""]
    # Most frequent titles first, then alphabetical for ties
    counts = titles.value_counts()
    seen: set[str] = set()
    result: list[str] = []
    for title, _ in counts.items():
        key = title.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(title)
        if len(result) >= limit:
            break
    return result


def aggregate_postings(frames: list[pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame, dict, dict[str, list[str]]]:
    combined = pd.concat([f for f in frames if not f.empty], ignore_index=True)
    meta = {
        "total_postings_matched": int(len(combined)),
        "by_source": combined["source"].value_counts().to_dict() if len(combined) else {},
        "by_role": combined["role"].value_counts().to_dict() if len(combined) else {},
    }

    skill_rows = []
    role_rows = []
    example_titles_by_role: dict[str, list[str]] = {}

    for role in ROLES:
        subset = combined[combined["role"] == role]
        total = len(subset)
        if total == 0:
            continue

        example_titles_by_role[role] = top_example_titles(subset)

        skill_hits: Counter[str] = Counter()
        # Salaries of postings that do/don't mention each skill, for a per-skill salary-lift estimate.
        salaries_with: dict[str, list[float]] = defaultdict(list)
        salaries_without: dict[str, list[float]] = defaultdict(list)
        for _, row in subset.iterrows():
            found = skills_in_text(str(row["text"]), role)
            for skill in found:
                skill_hits[skill] += 1
            sal = row.get("salary")
            if sal is None or (isinstance(sal, float) and pd.isna(sal)):
                continue
            for skill in SKILL_LEXICON[role]:
                (salaries_with if skill in found else salaries_without)[skill].append(float(sal))

        # Keep top skills for this role (at least 1 hit), sorted by demand
        ranked = skill_hits.most_common()
        if not ranked:
            # Use lexicon order with zero counts as last resort (shouldn't happen with text)
            ranked = [(s, 0) for s in SKILL_LEXICON[role][:7]]

        for skill, count in ranked[:12]:
            demand_pct = round(100 * count / total, 1) if total else 0
            with_sal, without_sal = salaries_with.get(skill, []), salaries_without.get(skill, [])
            salary_lift = (
                round(float(np.median(with_sal)) - float(np.median(without_sal)), 0)
                if len(with_sal) >= 5 and len(without_sal) >= 5
                else None
            )
            skill_rows.append(
                {
                    "role": role,
                    "skill": skill,
                    "demand_pct": demand_pct,
                    "posting_count": int(count),
                    "role_total_postings": total,
                    "salary_lift": salary_lift,
                }
            )

        exp_vals = [v for v in subset["experience_years"] if v is not None and not pd.isna(v)]
        median_exp = round(float(np.median(exp_vals)), 1) if exp_vals else None

        salaries = [v for v in subset.get("salary", pd.Series(dtype=float)) if v is not None and not pd.isna(v)]
        median_salary = round(float(np.median(salaries)), 0) if salaries else None

        smins = subset["salary_min"].dropna().tolist() if "salary_min" in subset.columns else []
        smaxs = subset["salary_max"].dropna().tolist() if "salary_max" in subset.columns else []
        salary_min = round(float(np.min(smins)), 0) if smins else None
        salary_max = round(float(np.max(smaxs)), 0) if smaxs else None

        role_rows.append(
            {
                "role": role,
                "median_experience_years": median_exp,
                "total_postings": total,
                "median_salary": median_salary,
                "salary_min": salary_min,
                "salary_max": salary_max,
                "sources": ",".join(sorted(subset["source"].unique())),
            }
        )

    skills_df = pd.DataFrame(skill_rows)
    roles_df = pd.DataFrame(role_rows)
    return skills_df, roles_df, meta, example_titles_by_role


def cosine_similarity(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    norm_a = sum(v * v for v in a.values()) ** 0.5
    norm_b = sum(v * v for v in b.values()) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def build_role_transitions(skills_df: pd.DataFrame, roles_df: pd.DataFrame) -> dict:
    """Skill-overlap graph between roles: friction = 1 - cosine similarity of
    each role's skill-demand vector. Used client-side for transition pathfinding."""
    demand_by_role: dict[str, dict[str, float]] = {
        role: dict(zip(g["skill"], g["demand_pct"])) for role, g in skills_df.groupby("role")
    }
    salary_by_role = dict(zip(roles_df["role"], roles_df["median_salary"]))

    transitions: dict[str, dict[str, dict]] = {}
    for role_a in ROLES:
        if role_a not in demand_by_role:
            continue
        transitions[role_a] = {}
        for role_b in ROLES:
            if role_b == role_a or role_b not in demand_by_role:
                continue
            vec_a, vec_b = demand_by_role[role_a], demand_by_role[role_b]
            similarity = cosine_similarity(vec_a, vec_b)
            friction = round((1 - similarity) * 100, 1)
            shared = sorted(
                (
                    {"skill": s, "demandA": vec_a[s], "demandB": vec_b[s]}
                    for s in set(vec_a) & set(vec_b)
                ),
                key=lambda s: min(s["demandA"], s["demandB"]),
                reverse=True,
            )
            sal_a, sal_b = salary_by_role.get(role_a), salary_by_role.get(role_b)
            salary_delta = (
                round(float(sal_b) - float(sal_a), 0)
                if sal_a is not None and sal_b is not None and pd.notna(sal_a) and pd.notna(sal_b)
                else None
            )
            transitions[role_a][role_b] = {
                "friction": friction,
                "sharedSkills": shared,
                "salaryDelta": salary_delta,
            }
    return transitions


def main() -> None:
    linkedin = load_linkedin()
    indeed = load_indeed()
    applicants = load_mindweave_applicants()

    skills_df, roles_df, meta, example_titles = aggregate_postings([linkedin, indeed])

    if not roles_df.empty and applicants:
        roles_df["applicants_per_posting"] = roles_df["role"].map(
            lambda r: round(applicants.get(r, np.nan), 1)
        )
    else:
        roles_df["applicants_per_posting"] = np.nan

    skills_path = OUT / "skills_by_role.csv"
    roles_path = OUT / "roles.csv"
    skills_df.to_csv(skills_path, index=False)
    roles_df.to_csv(roles_path, index=False)

    role_transitions = build_role_transitions(skills_df, roles_df)

    # Also emit JSON for the static app
    payload = build_app_payload(skills_df, roles_df, meta, applicants, example_titles, role_transitions)
    (OUT / "aggregated.json").write_text(json.dumps(payload, indent=2))

    summary = {
        **meta,
        "applicants_per_posting": applicants,
        "outputs": {
            "skills_by_role": str(skills_path),
            "roles": str(roles_path),
            "aggregated_json": str(OUT / "aggregated.json"),
        },
    }
    (OUT / "aggregation_summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


def build_app_payload(
    skills_df: pd.DataFrame,
    roles_df: pd.DataFrame,
    meta: dict,
    applicants: dict[str, float],
    example_titles: dict[str, list[str]],
    role_transitions: dict,
) -> dict:
    data: dict = {}
    for role in ROLES:
        role_info = roles_df[roles_df["role"] == role]
        if role_info.empty:
            continue
        row = role_info.iloc[0].to_dict()
        role_skills = skills_df[skills_df["role"] == role].sort_values(
            "demand_pct", ascending=False
        )
        skills = []
        for _, s in role_skills.iterrows():
            skill_name = s["skill"]
            lift = s.get("salary_lift")
            skills.append(
                {
                    "skill": skill_name,
                    "demand": float(s["demand_pct"]),
                    "postingCount": int(s["posting_count"]),
                    "salaryLift": float(lift) if lift is not None and pd.notna(lift) else None,
                    "learn": LEARN_LINKS.get(skill_name, "Search free courses on Coursera / YouTube"),
                }
            )
        data[role] = {
            "medianExp": row.get("median_experience_years"),
            "applicants": row.get("applicants_per_posting"),
            "totalPostings": int(row.get("total_postings", 0)),
            "medianSalary": row.get("median_salary"),
            "salaryMin": row.get("salary_min"),
            "salaryMax": row.get("salary_max"),
            "sources": row.get("sources", ""),
            "exampleTitles": example_titles.get(role, []),
            "allSkills": SKILL_LEXICON.get(role, []),
            "skills": skills,
        }

    return {
        "meta": {
            **meta,
            "datasets": [
                "xanderios/linkedin-job-postings",
                "fact-den/indeed-job-postings-2026",
                "mindweave/job-postings-applications",
            ],
            "applicantsSource": "mindweave/job-postings-applications",
            "skillExtraction": "keyword lexicon match in title + description",
            "generatedNote": (
                "Demand % = share of role-matched postings mentioning each skill. "
                f"Processed {meta.get('total_postings_matched', 0)} postings total."
            ),
            "skillLexicon": SKILL_LEXICON,
            "skillSearch": SKILL_SEARCH,
        },
        "roles": data,
        "roleTransitions": role_transitions,
    }


if __name__ == "__main__":
    main()
