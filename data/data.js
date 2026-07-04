window.JOB_FIT_DATA = {
  "meta": {
    "total_postings_matched": 6382,
    "by_source": {
      "linkedin": 5869,
      "indeed": 513
    },
    "by_role": {
      "Sales": 2443,
      "Operations": 1697,
      "Software Engineer": 945,
      "Data Analyst": 745,
      "Product Manager": 481,
      "Customer Success": 71
    },
    "datasets": [
      "xanderios/linkedin-job-postings",
      "fact-den/indeed-job-postings-2026",
      "mindweave/job-postings-applications"
    ],
    "applicantsSource": "mindweave/job-postings-applications",
    "skillExtraction": "keyword lexicon match in title + description",
    "generatedNote": "Demand % = share of role-matched postings mentioning each skill. Processed 6382 postings total.",
    "skillLexicon": {
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
        "ETL"
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
        "Kubernetes"
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
        "Design systems"
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
        "Demo skills"
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
        "Support escalation"
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
        "Cross-functional coordination"
      ]
    },
    "skillSearch": {
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
      "information architecture": "Information architecture"
    }
  },
  "roles": {
    "Data Analyst": {
      "medianExp": 5.0,
      "applicants": 7.0,
      "totalPostings": 745,
      "medianSalary": 152250.0,
      "salaryMin": 60000.0,
      "salaryMax": 470000.0,
      "sources": "indeed,linkedin",
      "exampleTitles": [
        "Data Scientist",
        "Business Analyst",
        "Financial Analyst",
        "Data Analyst",
        "Senior Data Scientist",
        "Senior Financial Analyst"
      ],
      "allSkills": [
        "SQL",
        "Excel",
        "Python",
        "Tableau",
        "Statistics",
        "Power BI",
        "Data visualization",
        "R",
        "Pandas",
        "ETL"
      ],
      "skills": [
        {
          "skill": "Excel",
          "demand": 60.8,
          "postingCount": 453,
          "salaryLift": -26125.0,
          "learn": "ExcelJet / Microsoft Learn"
        },
        {
          "skill": "SQL",
          "demand": 39.5,
          "postingCount": 294,
          "salaryLift": 27900.0,
          "learn": "SQLBolt + Mode SQL tutorial (free)"
        },
        {
          "skill": "Python",
          "demand": 28.6,
          "postingCount": 213,
          "salaryLift": 22624.0,
          "learn": "Kaggle 'Python' micro-course (free)"
        },
        {
          "skill": "Statistics",
          "demand": 27.9,
          "postingCount": 208,
          "salaryLift": 12824.0,
          "learn": "Khan Academy Statistics"
        },
        {
          "skill": "Tableau",
          "demand": 17.9,
          "postingCount": 133,
          "salaryLift": -37250.0,
          "learn": "Tableau Public free training videos"
        },
        {
          "skill": "Data visualization",
          "demand": 17.0,
          "postingCount": 127,
          "salaryLift": -10500.0,
          "learn": "Storytelling with Data (blog)"
        },
        {
          "skill": "Power BI",
          "demand": 17.0,
          "postingCount": 127,
          "salaryLift": -24088.0,
          "learn": "Microsoft Learn Power BI path"
        },
        {
          "skill": "ETL",
          "demand": 5.6,
          "postingCount": 42,
          "salaryLift": 12000.0,
          "learn": "DataCamp ETL fundamentals (free tier)"
        },
        {
          "skill": "Pandas",
          "demand": 1.9,
          "postingCount": 14,
          "salaryLift": 22500.0,
          "learn": "Kaggle Pandas micro-course (free)"
        }
      ]
    },
    "Software Engineer": {
      "medianExp": 5.0,
      "applicants": 7.0,
      "totalPostings": 945,
      "medianSalary": 190888.0,
      "salaryMin": 70000.0,
      "salaryMax": 1000000.0,
      "sources": "indeed,linkedin",
      "exampleTitles": [
        "Software Engineer",
        "Senior Software Engineer",
        "Machine Learning Engineer",
        "Full Stack Engineer",
        "Backend Engineer",
        "DevOps Engineer"
      ],
      "allSkills": [
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
        "Kubernetes"
      ],
      "skills": [
        {
          "skill": "Python",
          "demand": 38.8,
          "postingCount": 367,
          "salaryLift": -6500.0,
          "learn": "Kaggle 'Python' micro-course (free)"
        },
        {
          "skill": "Testing",
          "demand": 37.5,
          "postingCount": 354,
          "salaryLift": -20000.0,
          "learn": "Testing Library docs"
        },
        {
          "skill": "JavaScript",
          "demand": 37.1,
          "postingCount": 351,
          "salaryLift": -5000.0,
          "learn": "javascript.info (free)"
        },
        {
          "skill": "SQL",
          "demand": 36.3,
          "postingCount": 343,
          "salaryLift": -5000.0,
          "learn": "SQLBolt + Mode SQL tutorial (free)"
        },
        {
          "skill": "Cloud (AWS)",
          "demand": 28.7,
          "postingCount": 271,
          "salaryLift": -6250.0,
          "learn": "AWS Skill Builder free tier"
        },
        {
          "skill": "React",
          "demand": 27.7,
          "postingCount": 262,
          "salaryLift": -1500.0,
          "learn": "React.dev official tutorial (free)"
        },
        {
          "skill": "Git",
          "demand": 23.5,
          "postingCount": 222,
          "salaryLift": -15000.0,
          "learn": "Git 'Learn Branching' interactive"
        },
        {
          "skill": "Kubernetes",
          "demand": 21.3,
          "postingCount": 201,
          "salaryLift": -5000.0,
          "learn": "Kubernetes.io tutorials"
        },
        {
          "skill": "Docker",
          "demand": 19.2,
          "postingCount": 181,
          "salaryLift": -30756.0,
          "learn": "Docker Getting Started guide"
        },
        {
          "skill": "REST APIs",
          "demand": 15.6,
          "postingCount": 147,
          "salaryLift": -23500.0,
          "learn": "MDN HTTP / API docs"
        },
        {
          "skill": "Java",
          "demand": 13.5,
          "postingCount": 128,
          "salaryLift": null,
          "learn": "Oracle Java Tutorials (free)"
        },
        {
          "skill": "Data structures",
          "demand": 8.1,
          "postingCount": 77,
          "salaryLift": -21579.0,
          "learn": "NeetCode roadmap (free)"
        }
      ]
    },
    "Product Manager": {
      "medianExp": 5.0,
      "applicants": 8.0,
      "totalPostings": 481,
      "medianSalary": 165000.0,
      "salaryMin": 74250.0,
      "salaryMax": 338300.0,
      "sources": "indeed,linkedin",
      "exampleTitles": [
        "Product Manager",
        "Senior Product Manager",
        "Product Owner",
        "Product Designer",
        "Product Manager II, Developer Experience",
        "Technical Product Manager"
      ],
      "allSkills": [
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
        "Design systems"
      ],
      "skills": [
        {
          "skill": "Stakeholder management",
          "demand": 50.7,
          "postingCount": 244,
          "salaryLift": 15250.0,
          "learn": "Lenny's Newsletter (free posts)"
        },
        {
          "skill": "Roadmapping",
          "demand": 50.1,
          "postingCount": 241,
          "salaryLift": 41262.0,
          "learn": "Reforge / SVPG articles"
        },
        {
          "skill": "Agile",
          "demand": 29.1,
          "postingCount": 140,
          "salaryLift": -29575.0,
          "learn": "Scrum.org free learning paths"
        },
        {
          "skill": "Analytics",
          "demand": 23.1,
          "postingCount": 111,
          "salaryLift": 6200.0,
          "learn": "Amplitude / GA4 free courses"
        },
        {
          "skill": "Product strategy",
          "demand": 21.6,
          "postingCount": 104,
          "salaryLift": 26325.0,
          "learn": "Reforge free articles"
        },
        {
          "skill": "Prototyping",
          "demand": 20.4,
          "postingCount": 98,
          "salaryLift": 20420.0,
          "learn": "Figma prototyping tutorials"
        },
        {
          "skill": "Figma",
          "demand": 10.2,
          "postingCount": 49,
          "salaryLift": null,
          "learn": "Figma's free interactive courses"
        },
        {
          "skill": "User research",
          "demand": 9.6,
          "postingCount": 46,
          "salaryLift": -25700.0,
          "learn": "NN/g free articles"
        },
        {
          "skill": "Wireframing",
          "demand": 8.9,
          "postingCount": 43,
          "salaryLift": null,
          "learn": "NN/g free articles"
        },
        {
          "skill": "Design systems",
          "demand": 7.9,
          "postingCount": 38,
          "salaryLift": null,
          "learn": "Refactoring UI (concepts)"
        },
        {
          "skill": "Jira",
          "demand": 6.9,
          "postingCount": 33,
          "salaryLift": -21275.0,
          "learn": "Atlassian University (free)"
        },
        {
          "skill": "SQL",
          "demand": 5.2,
          "postingCount": 25,
          "salaryLift": -20525.0,
          "learn": "SQLBolt + Mode SQL tutorial (free)"
        }
      ]
    },
    "Sales": {
      "medianExp": 5.0,
      "applicants": 7.0,
      "totalPostings": 2443,
      "medianSalary": 74880.0,
      "salaryMin": 100000.0,
      "salaryMax": 200100.0,
      "sources": "indeed,linkedin",
      "exampleTitles": [
        "Sales Director [Owner/Operator]",
        "Sales Manager",
        "Retail Sales Associate",
        "Sales Associate",
        "Sales Director {Owner/Operator}",
        "Account Executive"
      ],
      "allSkills": [
        "CRM (Salesforce)",
        "Pipeline management",
        "Prospecting",
        "Negotiation",
        "Lead generation",
        "HubSpot",
        "Cold outreach",
        "Account planning",
        "Quota attainment",
        "Demo skills"
      ],
      "skills": [
        {
          "skill": "Demo skills",
          "demand": 36.1,
          "postingCount": 883,
          "salaryLift": -20000.0,
          "learn": "Demo2Win free resources"
        },
        {
          "skill": "CRM (Salesforce)",
          "demand": 25.6,
          "postingCount": 626,
          "salaryLift": -2380.0,
          "learn": "Trailhead Salesforce Admin (free)"
        },
        {
          "skill": "Negotiation",
          "demand": 18.8,
          "postingCount": 459,
          "salaryLift": -13320.0,
          "learn": "Chris Voss negotiation summaries (free)"
        },
        {
          "skill": "Pipeline management",
          "demand": 16.7,
          "postingCount": 408,
          "salaryLift": 154182.0,
          "learn": "Sales Hacker / Gong blog (free)"
        },
        {
          "skill": "Quota attainment",
          "demand": 15.2,
          "postingCount": 372,
          "salaryLift": 26520.0,
          "learn": "Sales Hacker quota attainment posts"
        },
        {
          "skill": "Prospecting",
          "demand": 15.0,
          "postingCount": 366,
          "salaryLift": -11440.0,
          "learn": "LinkedIn Sales Navigator tips (free)"
        },
        {
          "skill": "Cold outreach",
          "demand": 9.7,
          "postingCount": 236,
          "salaryLift": -27500.0,
          "learn": "Sales Hacker cold email guides"
        },
        {
          "skill": "Lead generation",
          "demand": 5.9,
          "postingCount": 144,
          "salaryLift": -32430.0,
          "learn": "HubSpot Academy (free)"
        },
        {
          "skill": "Account planning",
          "demand": 2.5,
          "postingCount": 62,
          "salaryLift": 21520.0,
          "learn": "Gartner account planning articles"
        },
        {
          "skill": "HubSpot",
          "demand": 1.4,
          "postingCount": 34,
          "salaryLift": null,
          "learn": "HubSpot Academy CRM course (free)"
        }
      ]
    },
    "Customer Success": {
      "medianExp": 5.0,
      "applicants": 7.0,
      "totalPostings": 71,
      "medianSalary": 200000.0,
      "salaryMin": NaN,
      "salaryMax": NaN,
      "sources": "indeed,linkedin",
      "exampleTitles": [
        "Customer Success & Services Marketing Manager",
        "Customer Success Manager",
        "Senior Customer Success Manager",
        "Enterprise Customer Success Manager",
        "Client Success Manager",
        "Analytics Manager - Partner Success Team"
      ],
      "allSkills": [
        "Onboarding",
        "Retention",
        "Account management",
        "Customer advocacy",
        "Churn reduction",
        "CRM (Salesforce)",
        "Product adoption",
        "Renewals",
        "Upselling",
        "Support escalation"
      ],
      "skills": [
        {
          "skill": "Renewals",
          "demand": 57.7,
          "postingCount": 41,
          "salaryLift": null,
          "learn": "Gainsight renewal management articles"
        },
        {
          "skill": "CRM (Salesforce)",
          "demand": 54.9,
          "postingCount": 39,
          "salaryLift": null,
          "learn": "Trailhead Salesforce Admin (free)"
        },
        {
          "skill": "Account management",
          "demand": 35.2,
          "postingCount": 25,
          "salaryLift": null,
          "learn": "Gainsight CS playbook articles"
        },
        {
          "skill": "Onboarding",
          "demand": 31.0,
          "postingCount": 22,
          "salaryLift": null,
          "learn": "Gainsight Customer Success resources"
        },
        {
          "skill": "Retention",
          "demand": 29.6,
          "postingCount": 21,
          "salaryLift": null,
          "learn": "ProfitWell Retain blog (free)"
        },
        {
          "skill": "Upselling",
          "demand": 23.9,
          "postingCount": 17,
          "salaryLift": null,
          "learn": "Gainsight expansion playbook"
        },
        {
          "skill": "Churn reduction",
          "demand": 9.9,
          "postingCount": 7,
          "salaryLift": null,
          "learn": "ChurnZero blog (free)"
        },
        {
          "skill": "Support escalation",
          "demand": 8.5,
          "postingCount": 6,
          "salaryLift": null,
          "learn": "ITIL / Zendesk escalation guides"
        },
        {
          "skill": "Customer advocacy",
          "demand": 4.2,
          "postingCount": 3,
          "salaryLift": null,
          "learn": "Influitive advocacy guides"
        },
        {
          "skill": "Product adoption",
          "demand": 2.8,
          "postingCount": 2,
          "salaryLift": null,
          "learn": "Pendo product adoption guides"
        }
      ]
    },
    "Operations": {
      "medianExp": 5.0,
      "applicants": 7.0,
      "totalPostings": 1697,
      "medianSalary": 76917.0,
      "salaryMin": 60000.0,
      "salaryMax": 231000.0,
      "sources": "indeed,linkedin",
      "exampleTitles": [
        "Project Manager",
        "Operations Manager",
        "Program Manager",
        "Senior Project Manager",
        "Construction Project Manager",
        "Recruiter"
      ],
      "allSkills": [
        "Process improvement",
        "Project management",
        "Logistics",
        "Supply chain",
        "Agile",
        "Excel",
        "Data analysis",
        "Vendor management",
        "KPI tracking",
        "Cross-functional coordination"
      ],
      "skills": [
        {
          "skill": "Excel",
          "demand": 60.8,
          "postingCount": 1031,
          "salaryLift": -14544.0,
          "learn": "ExcelJet / Microsoft Learn"
        },
        {
          "skill": "Project management",
          "demand": 50.5,
          "postingCount": 857,
          "salaryLift": 52080.0,
          "learn": "Google Project Management Certificate (audit free)"
        },
        {
          "skill": "Cross-functional coordination",
          "demand": 21.3,
          "postingCount": 362,
          "salaryLift": 54496.0,
          "learn": "Atlassian teamwork guides"
        },
        {
          "skill": "Process improvement",
          "demand": 17.3,
          "postingCount": 294,
          "salaryLift": 33440.0,
          "learn": "Lean Six Sigma Yellow Belt (free intro)"
        },
        {
          "skill": "Supply chain",
          "demand": 12.8,
          "postingCount": 218,
          "salaryLift": 23044.0,
          "learn": "MIT SCM micro-masters preview (free)"
        },
        {
          "skill": "Agile",
          "demand": 12.0,
          "postingCount": 203,
          "salaryLift": -24000.0,
          "learn": "Scrum.org free learning paths"
        },
        {
          "skill": "Logistics",
          "demand": 10.3,
          "postingCount": 174,
          "salaryLift": 35574.0,
          "learn": "Coursera Supply Chain intro (audit free)"
        },
        {
          "skill": "KPI tracking",
          "demand": 9.4,
          "postingCount": 159,
          "salaryLift": null,
          "learn": "KPI.org free resources"
        },
        {
          "skill": "Data analysis",
          "demand": 3.5,
          "postingCount": 60,
          "salaryLift": null,
          "learn": "Kaggle Data Analysis micro-course (free)"
        },
        {
          "skill": "Vendor management",
          "demand": 2.8,
          "postingCount": 48,
          "salaryLift": null,
          "learn": "CIPS vendor management articles"
        }
      ]
    }
  },
  "roleTransitions": {
    "Data Analyst": {
      "Software Engineer": {
        "friction": 69.7,
        "sharedSkills": [
          {
            "skill": "SQL",
            "demandA": 39.5,
            "demandB": 36.3
          },
          {
            "skill": "Python",
            "demandA": 28.6,
            "demandB": 38.8
          }
        ],
        "salaryDelta": 38638.0
      },
      "Product Manager": {
        "friction": 97.4,
        "sharedSkills": [
          {
            "skill": "SQL",
            "demandA": 39.5,
            "demandB": 5.2
          }
        ],
        "salaryDelta": 12750.0
      },
      "Sales": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -77370.0
      },
      "Customer Success": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 47750.0
      },
      "Operations": {
        "friction": 51.7,
        "sharedSkills": [
          {
            "skill": "Excel",
            "demandA": 60.8,
            "demandB": 60.8
          }
        ],
        "salaryDelta": -75333.0
      }
    },
    "Software Engineer": {
      "Data Analyst": {
        "friction": 69.7,
        "sharedSkills": [
          {
            "skill": "SQL",
            "demandA": 36.3,
            "demandB": 39.5
          },
          {
            "skill": "Python",
            "demandA": 38.8,
            "demandB": 28.6
          }
        ],
        "salaryDelta": -38638.0
      },
      "Product Manager": {
        "friction": 97.7,
        "sharedSkills": [
          {
            "skill": "SQL",
            "demandA": 36.3,
            "demandB": 5.2
          }
        ],
        "salaryDelta": -25888.0
      },
      "Sales": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -116008.0
      },
      "Customer Success": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 9112.0
      },
      "Operations": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -113971.0
      }
    },
    "Product Manager": {
      "Data Analyst": {
        "friction": 97.4,
        "sharedSkills": [
          {
            "skill": "SQL",
            "demandA": 5.2,
            "demandB": 39.5
          }
        ],
        "salaryDelta": -12750.0
      },
      "Software Engineer": {
        "friction": 97.7,
        "sharedSkills": [
          {
            "skill": "SQL",
            "demandA": 5.2,
            "demandB": 36.3
          }
        ],
        "salaryDelta": 25888.0
      },
      "Sales": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -90120.0
      },
      "Customer Success": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 35000.0
      },
      "Operations": {
        "friction": 95.4,
        "sharedSkills": [
          {
            "skill": "Agile",
            "demandA": 29.1,
            "demandB": 12.0
          }
        ],
        "salaryDelta": -88083.0
      }
    },
    "Sales": {
      "Data Analyst": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 77370.0
      },
      "Software Engineer": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 116008.0
      },
      "Product Manager": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 90120.0
      },
      "Customer Success": {
        "friction": 75.3,
        "sharedSkills": [
          {
            "skill": "CRM (Salesforce)",
            "demandA": 25.6,
            "demandB": 54.9
          }
        ],
        "salaryDelta": 125120.0
      },
      "Operations": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 2037.0
      }
    },
    "Customer Success": {
      "Data Analyst": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -47750.0
      },
      "Software Engineer": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -9112.0
      },
      "Product Manager": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -35000.0
      },
      "Sales": {
        "friction": 75.3,
        "sharedSkills": [
          {
            "skill": "CRM (Salesforce)",
            "demandA": 54.9,
            "demandB": 25.6
          }
        ],
        "salaryDelta": -125120.0
      },
      "Operations": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -123083.0
      }
    },
    "Operations": {
      "Data Analyst": {
        "friction": 51.7,
        "sharedSkills": [
          {
            "skill": "Excel",
            "demandA": 60.8,
            "demandB": 60.8
          }
        ],
        "salaryDelta": 75333.0
      },
      "Software Engineer": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 113971.0
      },
      "Product Manager": {
        "friction": 95.4,
        "sharedSkills": [
          {
            "skill": "Agile",
            "demandA": 12.0,
            "demandB": 29.1
          }
        ],
        "salaryDelta": 88083.0
      },
      "Sales": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": -2037.0
      },
      "Customer Success": {
        "friction": 100.0,
        "sharedSkills": [],
        "salaryDelta": 123083.0
      }
    }
  }
};
