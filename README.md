# Job-Fit Gap Analyzer

Static HTML tool that compares your skills against **real job-posting aggregates** from Hugging Face datasets. Upload your CV to auto-detect skills and suggested roles — all parsing runs **client-side** in the browser. No server required.

## Three analysis modes

The app supports three ways to evaluate your fit — all run entirely in the browser.

### Mode A: Benchmark against market data (default)

1. Parse your CV to auto-detect skills, experience, and a suggested role.
2. Pick a target role and toggle skills you have.
3. Click **Analyze my fit** to see gaps ranked by how often real postings require each skill, plus salary and applicant benchmarks from aggregated Hugging Face data.

### Mode B: Analyze a specific job

1. Parse your CV first (same as above).
2. Switch to **Analyze a specific job**.
3. Paste a real job posting (title + description).
4. Click **Analyze fit for this job**.

Results include:

- **Fit score** — % of skills detected in the posting that also appear in your CV (keyword lexicon match).
- **You have / Missing** — skills from this posting found vs not found in your CV.
- **Experience alignment** — your years vs requirements parsed from the posting (e.g. "3+ years", "senior").
- **Top 3 improvements** — missing skills prioritized by how often they appear in the posting text.
- **Market context** — for the detected role category, how competitive the field is and how often missing skills show up in similar aggregated postings.

A requirements preview appears when you leave the posting textarea (or when you run the analysis).

### Mode C: Career Pathfinder

1. Parse your CV first (same as above).
2. Switch to **Career Pathfinder**.
3. **Transition path** tab — pick a starting role and a target role. Instead of just scoring one role, this treats the six roles as a graph: edge weight ("friction") is `1 − cosine similarity` between each pair of roles' skill-demand vectors, computed from real posting data. It runs a shortest-path search and will surface a **stepping-stone role** when a two-hop route (e.g. Sales → Customer Success → Product Manager) has lower total friction than jumping directly — something a single-role gap calculator can't show.
4. **Skill ROI** tab — for a target role, ranks your missing skills by a **priority score** = market demand % + salary lift (the difference in median salary between postings that mention the skill and postings that don't, expressed as % of the role's median salary). This tells you which skill to learn *first*, not just which is most common.

### Limitations (all three modes)

- Keyword matching only — misses synonyms, abbreviations, and skills not in the lexicon.
- Posting experience parsing is heuristic ("3+ years", "senior", etc.) and may miss unusual wording.
- Fit score reflects lexicon overlap, **not** a prediction of hiring outcome.
- PDF text extraction can scramble layout; `.docx` is not supported — paste text instead.
- Salary lift and friction scores are only as reliable as sample size — roles with few postings (e.g. Customer Success, ~71) or skills with sparse salary data can produce noisy or counterintuitive numbers. Salary lift is omitted (shown as "insufficient samples") when fewer than 5 postings exist on either side of the comparison.

## Quick start (demo)

1. Open `index.html` in any modern browser (double-click or drag into Chrome/Firefox).
2. Upload a `.txt` or `.pdf` resume (or paste text) and click **Parse my CV**.
3. Choose a mode:
   - **Benchmark against market data** — pick role, toggle skills, click **Analyze my fit**.
   - **Analyze a specific job** — paste a job posting, click **Analyze fit for this job**.

Data is baked into `data/data.js`, generated from real postings.

## Regenerate data from Hugging Face

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Download raw datasets

```bash
python data/fetch_data.py
```

Downloads into `data/raw/` (repo folders use `owner__repo-name` naming):

| Dataset | Repo | Used for |
|---------|------|----------|
| LinkedIn job postings | `xanderios/linkedin-job-postings` | Titles, descriptions, experience labels, salaries (~33k rows) |
| Indeed 2026 sample | `fact-den/indeed-job-postings-2026` | Titles, descriptions, parsed salaries (~1k rows; files at `jobs/jobs.csv`) |
| Mindweave applications | `mindweave/job-postings-applications` | Applicants-per-posting (applications ÷ jobs by role) |

Download status is recorded in `data/download_manifest.json`.

### 3. Aggregate into CSV + JSON

```bash
python data/aggregate.py
```

Outputs:

- `data/skills_by_role.csv` — role, skill, demand_pct, posting_count, role_total_postings, salary_lift (median salary of postings mentioning the skill minus those that don't; blank if <5 postings on either side)
- `data/roles.csv` — role, median_experience_years, total_postings, median_salary, salary_min/max, applicants_per_posting, sources
- `data/aggregated.json` — combined payload for the UI (includes `exampleTitles`, skill lexicon for CV matching, and `roleTransitions`: a role×role friction/shared-skills/salary-delta graph used by the Career Pathfinder)
- `data/aggregation_summary.json` — run stats

### 4. Bake into the static app

```bash
python data/build_data_js.py
```

Writes `data/data.js` (`window.JOB_FIT_DATA = …`) and ensures `index.html` loads it.

Or run both in one step:

```bash
python data/aggregate.py && python data/build_data_js.py
```

## Data sources & columns used

| Dataset | HF repo | Columns used |
|---------|---------|--------------|
| LinkedIn | [xanderios/linkedin-job-postings](https://huggingface.co/datasets/xanderios/linkedin-job-postings) | `title`, `description`, `formatted_experience_level`, `med_salary`, `skills_desc`, `applies` |
| Indeed | [fact-den/indeed-job-postings-2026](https://huggingface.co/datasets/fact-den/indeed-job-postings-2026) | `title`, `description`, `salaryMin`, `salaryMax` |
| Mindweave | [mindweave/job-postings-applications](https://huggingface.co/datasets/mindweave/job-postings-applications) | `jobs.title`, `jobs.role_family`, `applications` (count per job) |

## Data strategy & limitations

### Role matching (6 canonical roles)

Job titles from LinkedIn/Indeed are mapped to **six normalized roles** via keyword regex, with a Mindweave `role_family` fallback for applicant stats. The UI shows these six roles — not all 55+ raw Mindweave title variants — with **example real titles** under each (e.g. "Data Analyst — matches titles like: Senior Data Scientist, FP&A Analyst, BI Analyst"). This keeps the picker practical for candidates while reflecting real posting diversity.

| Canonical role | Mindweave `role_family` | Example title keywords |
|----------------|-------------------------|-------------------------|
| **Data Analyst** | `data` | data analyst, BI analyst, FP&A analyst, data scientist, … |
| **Software Engineer** | `engineering` | software engineer, ML engineer, backend/frontend, DevOps, SRE, … |
| **Product Manager** | `product` | product manager/owner, growth PM, UX/product designer, … |
| **Sales** | `sales` | SDR/BDR, account executive, regional sales manager, … |
| **Customer Success** | `customer_success` | customer success manager, partner success, … |
| **Operations** | `operations` | operations manager, logistics, talent acquisition, project manager, … |

### CV parsing (client-side)

- **Supported formats:** `.txt` (read directly), `.pdf` (via pdf.js CDN). `.docx` is not supported — paste text instead.
- **Experience:** regex heuristics (`X years experience`) and employment date-range counting.
- **Skills:** keyword lexicon match against CV text (same terms as job-posting aggregation).
- **Role suggestion:** scores each canonical role by % of that role's skill lexicon found in the CV; pre-selects top match.

### Specific job posting analysis (client-side)

- **Role detection:** title keywords in first lines + skill overlap against canonical roles.
- **Skill extraction:** same `skillSearch` lexicon scanned in full posting text; ranked by mention frequency.
- **Experience parsing:** regex for ranges (`5–7 years`), minimums (`3+ years`), and level keywords (entry, senior, mid-level).
- **Requirements section:** heuristic extraction from lines after "Requirements", "Qualifications", "What you'll need", etc.
- **Fit score:** `(posting skills found in CV) / (total posting skills detected) × 100`.
- **Market context:** links missing skills to aggregated demand % for the detected role category.

**Limitations:** Heuristic only — misses synonyms, abbreviations, and skills not in the lexicon. PDF layout can scramble text extraction. Not a hiring prediction.

### Skill extraction (postings)

Skills are detected with a **curated keyword lexicon** scanned in job title + description text (LinkedIn `description`, `skills_desc`; Indeed `description`, `occupations`). Demand % = `(postings mentioning skill) / (total role postings) × 100`.

### Experience & salary

- **Median experience** — parsed from LinkedIn `formatted_experience_level` (Entry → 1 yr, Mid-Senior → 5 yr, etc.).
- **Salaries** — Indeed `salaryMin`/`salaryMax` (annual USD); LinkedIn medians annualized by pay period. Values outside $20k–$1M are filtered as outliers.
- **Applicants per posting** — median application count per matched job title in Mindweave (synthetic but structurally realistic).

## Project layout

```
├── index.html              # Static analyzer UI (CV upload + two analysis modes)
├── requirements.txt
├── README.md
└── data/
    ├── fetch_data.py       # Download from Hugging Face
    ├── aggregate.py        # Build skills_by_role.csv, roles.csv, aggregated.json
    ├── build_data_js.py    # Emit data.js for static HTML
    ├── data.js             # Baked aggregates (generated)
    ├── aggregated.json     # JSON payload (generated)
    ├── skills_by_role.csv  # Per-role skill demand (generated)
    ├── roles.csv           # Per-role summary stats (generated)
    ├── aggregation_summary.json
    └── raw/                # Downloaded source CSVs (gitignored)
```

## License & attribution

Job posting data belongs to the respective Hugging Face dataset authors. This demo aggregates public samples for educational use only.
