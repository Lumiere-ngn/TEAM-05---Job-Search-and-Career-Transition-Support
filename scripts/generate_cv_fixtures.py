from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CvName",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#1F2937"),
            spaceAfter=4,
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvRole",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#374151"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvSection",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=13.5,
            textColor=colors.HexColor("#0F766E"),
            spaceBefore=7,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.9,
            leading=11.3,
            textColor=colors.HexColor("#111827"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvSmall",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#4B5563"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvBullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.7,
            leading=11.3,
            leftIndent=10,
            firstLineIndent=-6,
            bulletIndent=0,
            textColor=colors.HexColor("#111827"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvJobTitle",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=11.8,
            textColor=colors.HexColor("#111827"),
            spaceBefore=4,
            spaceAfter=1,
        )
    )
    return styles


STYLES = build_styles()


def p(text, style="CvBody"):
    return Paragraph(text, STYLES[style])


def section(title):
    return Paragraph(title.upper(), STYLES["CvSection"])


def bullets(items):
    return [Paragraph("- " + item, STYLES["CvBullet"]) for item in items]


def skill_table(groups):
    rows = [[p(f"<b>{label}</b>", "CvSmall"), p(skills, "CvSmall")] for label, skills in groups]
    table = Table(rows, colWidths=[1.25 * inch, 5.65 * inch])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("LINEBELOW", (0, 0), (-1, -2), 0.25, colors.HexColor("#E5E7EB")),
            ]
        )
    )
    return table


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#6B7280"))
    text = f"Synthetic CV fixture for resume parsing and job matching tests - Page {doc.page}"
    canvas.drawString(0.72 * inch, 0.42 * inch, text)
    canvas.restoreState()


def build_cv(filename, name, headline, contact, summary, skills, experience, projects, education, certs):
    path = OUT / filename
    doc = SimpleDocTemplate(
        str(path),
        pagesize=LETTER,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.56 * inch,
        bottomMargin=0.58 * inch,
    )
    story = [
        p(name, "CvName"),
        p(headline, "CvRole"),
        p(contact, "CvSmall"),
        Spacer(1, 4),
        section("Professional Summary"),
        p(summary),
        section("Core Skills"),
        skill_table(skills),
        section("Professional Experience"),
    ]

    for job in experience:
        block = [p(job["title"], "CvJobTitle"), p(job["meta"], "CvSmall")]
        block.extend(bullets(job["bullets"]))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 3))

    project_block = [section("Selected Projects")]
    for proj in projects:
        project_block.append(p(f"<b>{proj['name']}</b> - {proj['description']}"))
    story.append(KeepTogether(project_block))

    story.append(section("Education"))
    for item in education:
        story.append(p(item))

    story.append(section("Certifications And Learning"))
    for item in certs:
        story.append(p(item))

    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
    return path


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    mid_path = build_cv(
        "mid_software_engineer_cv.pdf",
        "Taylor Morgan",
        "Mid-Level Software Engineer | Full-Stack TypeScript, React, Node.js",
        "Toronto, ON | taylor.morgan@example.com | 555-0147 | linkedin.com/in/taylormorgan | github.com/taylormorgan",
        "Full-stack software engineer with 5 years of experience building customer-facing SaaS products, internal operations tools, and data-backed workflows. Strong in TypeScript, React, Node.js, PostgreSQL, REST APIs, and cloud deployment. Known for improving product reliability, collaborating closely with designers and product managers, and translating ambiguous requirements into maintainable features.",
        [
            ("Languages", "TypeScript, JavaScript, Python, SQL, HTML, CSS"),
            ("Frontend", "React, Next.js, Tailwind CSS, accessibility, component testing"),
            ("Backend", "Node.js, Express, REST APIs, authentication, background jobs"),
            ("Data", "PostgreSQL, Prisma, Redis, analytics events, data validation with Zod"),
            ("Cloud And DevOps", "AWS, Docker, GitHub Actions, CI/CD, observability, Sentry"),
            ("Collaboration", "Agile delivery, code review, technical documentation, mentoring interns"),
        ],
        [
            {
                "title": "Software Engineer - Northstar Analytics",
                "meta": "Toronto, ON | March 2022 - Present",
                "bullets": [
                    "Built React and Next.js dashboards used by 1,200 weekly active operations users, reducing manual report preparation by 8 hours per team each week.",
                    "Designed Node.js API endpoints with PostgreSQL and Prisma, improving median page load time from 2.4 seconds to 1.1 seconds.",
                    "Added role-based access controls, audit logs, and Zod request validation for customer account workflows.",
                    "Created reusable form and table components with accessible keyboard behavior and unit tests in Vitest.",
                    "Partnered with product and design to ship a self-serve workflow builder from discovery through production launch.",
                ],
            },
            {
                "title": "Junior Software Developer - BrightCart Commerce",
                "meta": "Remote | June 2019 - February 2022",
                "bullets": [
                    "Implemented checkout improvements in React and Express that increased successful payment completion by 6 percent.",
                    "Maintained REST integrations with Stripe, Shopify, and internal inventory services.",
                    "Wrote automated tests for cart pricing, promotions, and tax calculation edge cases.",
                    "Improved deployment confidence by adding GitHub Actions checks for linting, tests, and database migrations.",
                ],
            },
        ],
        [
            {
                "name": "Resume Matching Prototype",
                "description": "Built a TypeScript prototype that compares extracted resume skills against normalized job requirements and explains matched and missing skills.",
            },
            {
                "name": "Support Triage Automation",
                "description": "Created a Python script and dashboard that grouped support tickets by product area and surfaced weekly defect trends.",
            },
        ],
        ["Bachelor of Computer Science - University of Waterloo, 2019"],
        ["AWS Cloud Practitioner, 2023", "Frontend Masters: TypeScript and React Performance, 2024"],
    )

    senior_path = build_cv(
        "senior_software_engineer_cv.pdf",
        "Jordan Lee",
        "Senior Software Engineer | Distributed Systems, Platform Architecture, Technical Leadership",
        "New York, NY | jordan.lee@example.com | 555-0198 | linkedin.com/in/jordanlee | github.com/jordanlee",
        "Senior software engineer with 11 years of experience designing distributed systems, cloud platforms, and high-scale product infrastructure. Deep background in TypeScript, Go, Java, Kubernetes, AWS, event-driven architecture, observability, and reliability engineering. Leads cross-functional technical strategy, mentors engineers, and turns business goals into resilient systems that teams can operate safely.",
        [
            ("Languages", "TypeScript, Go, Java, Python, SQL"),
            ("Architecture", "Distributed systems, event-driven design, microservices, API design, system design"),
            ("Cloud Platform", "AWS, Kubernetes, Docker, Terraform, service mesh, CI/CD"),
            ("Data Systems", "PostgreSQL, DynamoDB, Kafka, Redis, Elasticsearch, data modeling"),
            ("Reliability", "Observability, OpenTelemetry, SLOs, incident response, performance tuning"),
            ("Leadership", "Technical strategy, mentoring, architecture reviews, stakeholder communication"),
        ],
        [
            {
                "title": "Senior Software Engineer - AtlasCloud Systems",
                "meta": "New York, NY | January 2021 - Present",
                "bullets": [
                    "Led architecture for a multi-tenant workflow platform processing 45 million events per day with Kafka, Go services, and Kubernetes.",
                    "Reduced critical incident frequency by 38 percent by introducing SLOs, OpenTelemetry tracing, runbooks, and production readiness reviews.",
                    "Designed a permission and policy service adopted by 14 product teams, standardizing authorization across web and API surfaces.",
                    "Mentored 7 engineers through design reviews, pairing, promotion planning, and incident follow-up practices.",
                    "Partnered with security and compliance teams to implement audit trails, data retention controls, and customer-facing export workflows.",
                ],
            },
            {
                "title": "Staff-Track Backend Engineer - FinGrid Payments",
                "meta": "Remote | April 2017 - December 2020",
                "bullets": [
                    "Built Java and Spring Boot payment orchestration services with idempotency, retry controls, and automated reconciliation.",
                    "Migrated monolithic billing jobs into event-driven services, cutting monthly close processing time from 9 hours to 90 minutes.",
                    "Introduced Terraform modules and GitHub Actions pipelines that reduced environment setup time from days to under 1 hour.",
                    "Improved PostgreSQL query performance for ledger views by adding indexes, materialized aggregates, and service-level caching.",
                ],
            },
            {
                "title": "Software Engineer - CivicApps Lab",
                "meta": "Boston, MA | July 2013 - March 2017",
                "bullets": [
                    "Delivered public sector web applications using React, Node.js, PostgreSQL, and AWS for transportation and permitting teams.",
                    "Created API documentation and onboarding guides that helped new developers contribute production changes in their first sprint.",
                ],
            },
        ],
        [
            {
                "name": "Skill Gap Recommendation Engine",
                "description": "Designed a ranking service that compares candidate profiles to job requirements and returns transparent weighted score factors.",
            },
            {
                "name": "Platform Reliability Scorecards",
                "description": "Built service scorecards combining deployment frequency, incident volume, latency, error budgets, and ownership metadata.",
            },
        ],
        [
            "Master of Science in Computer Science - Northeastern University, 2013",
            "Bachelor of Science in Software Engineering - Rochester Institute of Technology, 2011",
        ],
        ["AWS Certified Solutions Architect - Associate, 2022", "Kubernetes Application Developer training, 2023"],
    )

    print(mid_path)
    print(senior_path)


if __name__ == "__main__":
    main()
