from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "id": "ai-clienteling-platform",
        "title": "AI Agentic Clienteling Platform",
        "tagline": "Multi-agent AI platform automating retail clienteling workflows",
        "company": "Salesfloor",
        "description": (
            "Led design and implementation of a multi-agent AI platform automating retail "
            "clienteling workflows — generating personalised associate tasks and communications "
            "end-to-end, from customer data qualification through content drafting. Defined a "
            "standardised agent communication protocol (A2A/JSON-RPC) with discoverable agent "
            "cards, enabling a central planner to orchestrate specialised agents and reuse them "
            "across future workflows."
        ),
        "tech": ["Python 3.12", "LangGraph", "LangChain", "MCP", "A2A", "LangSmith", "OpenTelemetry"],
        "highlights": [
            "Standardised A2A/JSON-RPC agent communication with discoverable agent cards",
            "Selective LLM usage — deterministic SQL and rules for filtering, LLMs only for reasoning-heavy tasks",
            "Full observability via LangSmith for LLM tracing and OpenTelemetry for distributed telemetry",
            "End-to-end debugging across agent hops",
            "Reusable architectural pattern with roadmap for production hardening, data integration, and AI governance",
        ],
        "icon": "🤖",
    },
    {
        "id": "crypto-trading-agent",
        "title": "Agentic Crypto Trading System",
        "tagline": "7 concurrent LLM agents with multi-agent debate reducing noise entries by 85%",
        "company": "Personal Project",
        "description": (
            "Deployed 7 concurrent trading pods on GKE, each running a distinct LLM "
            "(GPT-4o, Claude, Gemini, Deepseek, Grok + rule-based baseline), with a "
            "multi-agent debate mechanism achieving consensus before trade execution — "
            "reducing noise entries by 85% (from 12–21 trades to 1–2 per pod)."
        ),
        "tech": ["Python", "LangGraph", "CrewAI", "HuggingFace", "PyTorch", "GKE", "Helm", "Terraform"],
        "highlights": [
            "7 concurrent agents with multi-agent debate reducing noise entries by 85%",
            "Fine-tuned CryptoBERT and FinBERT with LoRA/PEFT achieving 95.4% validation accuracy",
            "70/30 weighted ensemble NLP inference across 30–40 RSS headlines per cycle",
            "Win rate improved from 17–25% to 100% with 2.5:1 reward/risk ratio",
            "Docker image cut by 49% (5.3GB → 2.7GB) with cold-start-free CPU inference",
            "Jenkins pipeline with GCP Cloud Build integration eliminating ephemeral storage bottlenecks",
        ],
        "icon": "📈",
    },
    {
        "id": "genai-service-desk",
        "title": "GenAI Service Desk Intelligence Platform",
        "tagline": "Natural-language querying over enterprise knowledge base reducing MTTR",
        "company": "Symcor",
        "description": (
            "Delivered a natural-language query interface over the enterprise knowledge base "
            "(tickets, runbooks, SOPs, FAQs), replacing manual documentation searches and "
            "reducing MTTR for recurring incidents."
        ),
        "tech": ["Python", "FastAPI", "OpenAI", "RAG", "ChromaDB", "LangChain"],
        "highlights": [
            "RAG pipeline with automated chunking, embedding, and incremental sync into ChromaDB",
            "Prompt-based endpoints via FastAPI supporting chat UI and programmatic service desk integration",
            "Replaced manual documentation searches, reducing MTTR for recurring incidents",
        ],
        "icon": "🎯",
    },
    {
        "id": "enterprise-knowledge-assistant",
        "title": "Enterprise GenAI Knowledge Assistant",
        "tagline": "RAG pipeline over Google Drive delivering source-attributed answers",
        "company": "",
        "description": (
            "Developed a RAG pipeline ingesting documents from Google Drive (PDFs, Docs, Sheets), "
            "delivering context-aware, source-attributed answers grounded in live business content."
        ),
        "tech": ["Python", "FastAPI", "OpenAI", "ChromaDB", "Google Drive API", "Kubernetes"],
        "highlights": [
            "Automated document sync and chunking via Google Drive API with Sentence Transformers embeddings",
            "Semantic search across enterprise corpora in ChromaDB",
            "Kubernetes deployment with auto-scaling, self-healing pods, persistent vector storage, TLS via cert-manager",
            "Multi-tenant role-scoped retrieval",
        ],
        "icon": "📚",
    },
]

EXPERIENCE = [
    {
        "role": "AI Engineer / MLOps",
        "company": "Salesfloor",
        "period": "Oct 2024 — Present",
        "bullets": [
            "Developed and shipped a headless agentic AI application in Python — LLM decision loops, tool-calling interfaces, prompt chains, and async task execution — deployed as containerised microservices integrating with clients' CRM systems",
            "Reduced manual DBA intervention by 60%+ by automating database operations (provisioning, backups, failover, schema migrations) with Python and infrastructure-as-code",
            "Coordinated iOS and Android release trains and delivered Jenkins CI/CD pipelines with automated testing, artifact promotion, and environment-specific deployment strategies",
            "Established MLOps observability practices: model performance monitoring, drift detection, and alerting across inference services",
        ],
    },
    {
        "role": "AI / MLOps Engineer (Contract)",
        "company": "Symcor Inc.",
        "period": "Dec 2022 — Present",
        "bullets": [
            "Delivered an AI-powered check fraud detection system on Databricks — trained and versioned ML classification models (MLflow) on financial transaction data, with PySpark feature engineering pipelines processing high-volume data into model-ready features",
            "Deployed fraud detection inference endpoints on Azure ML, integrated into the transaction pipeline with compliance-grade alerting and audit logging",
            "Developed the GenAI service desk intelligence platform (see Featured Projects), replacing manual knowledge searches with natural-language querying across enterprise documentation",
        ],
    },
    {
        "role": "Senior SRE / DevOps Engineer",
        "company": "Fullscript",
        "period": "Dec 2021 — Oct 2024",
        "bullets": [
            "Improved deployment frequency by 40% and cut production downtime by migrating .NET microservices to Kubernetes with Helm-managed workloads, RBAC, and ingress controllers",
            "Managed EKS/ECS infrastructure serving millions of requests; delivered GitLab CI/CD pipelines supporting 50+ engineers across multiple product teams",
            "Sustained reliability through Black Friday traffic spikes via auto-scaling and load testing; achieved SOC-2 compliance through Wiz security scanning integration",
        ],
    },
    {
        "role": "Senior AWS Specialist",
        "company": "TVO",
        "period": "Sep 2020 — Dec 2021",
        "bullets": [
            "Led AWS Well-Architected reviews across 5+ products, closing architectural gaps and designing a Landing Zone with Control Tower for hybrid multi-account governance",
            "Containerised React applications, deployed via S3/CloudFront CDN, and mentored junior DevOps engineers across Scrum/Kanban delivery cycles",
        ],
    },
    {
        "role": "Software Engineer (Infrastructure & Automation)",
        "company": "Thales Group",
        "period": "Jan 2018 — Sep 2020",
        "bullets": [
            "Developed Python automation frameworks replacing manual infrastructure runbooks, and built CloudWatch metric pipeline utilities improving incident detection across teams",
            "Reduced infrastructure costs by 25% through auto-scaling group configuration and ELB health checks; enforced IAM least-privilege policies across 20+ AWS accounts",
        ],
    },
    {
        "role": "Backend Engineer / Cloud Developer",
        "company": "Nexonia",
        "period": "Oct 2016 — Jan 2018",
        "bullets": [
            "Delivered Python backend services and REST API integrations for expense management workflows, and developed Lambda-based event-driven pipelines with SQS/SNS messaging and DLQ handling",
            "Configured multi-AZ RDS deployments (Aurora, MySQL) with automated failover achieving 99.9% availability",
        ],
    },
    {
        "role": "Systems & Automation Engineer",
        "company": "National Grid",
        "period": "Jul 2011 — Oct 2016",
        "bullets": [
            "Wrote Python monitoring tools, automation scripts, and internal dashboards for critical UK energy infrastructure — building early foundations in high-stakes, always-on software and fault-tolerant systems design",
        ],
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS, experience=EXPERIENCE)


@app.route("/project/<project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
